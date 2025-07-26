#this program download videos uploaded whith in 24 hours , skip user is not found , checks only starting effictive search
# updated previous one
#sucessfully runed but some error with instaloader

import json
import random
import time
import os
import logging
import sys
from datetime import datetime, timedelta, timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from instaloader import Instaloader, InstaloaderException, Post
from instagram_download.move_video_files import move_and_log_files

# Configure logging
logging.basicConfig(filename='instagram_reels_downloader.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver(profile_path, geckodriver_path):
    """Setup the Selenium WebDriver with the specified profile and geckodriver."""
    options = Options()
    options.headless = True  # Use headless mode to save resources

    profile = webdriver.FirefoxProfile(profile_path)
    options.profile = profile

    service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def scroll_to_load_content(driver):
    """Scroll down the page to load more content with dynamic waiting."""
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 8))  # Reduced max sleep time for better performance
        new_height = driver.execute_script("return document.body.scrollHeight")
        return new_height != last_height
    except Exception as e:
        logging.error(f"Error during scrolling: {e}")
        return False

def is_recent_post(post):
    """Check if the post was created within the last 24 hours."""
    post_time = post.date_utc.replace(tzinfo=timezone.utc)
    current_time = datetime.now(timezone.utc)
    time_difference = current_time - post_time
    return time_difference <= timedelta(hours=24)

def get_instagram_reels_links(driver, loader, username, num_reels, downloaded_links):
    """Fetch a set of Instagram reels links for a given username."""
    try:
        driver.get(f'https://www.instagram.com/{username}/reels')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        reels_links = set()
        while len(reels_links) < num_reels:
            if not scroll_to_load_content(driver):
                break  # Stop if no new content is loaded
            reels_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/reel/')]")
            logging.info(f"Found {len(reels_elements)} reel elements on the current page for {username}.")
            for elem in reels_elements:
                reel_link = elem.get_attribute('href')
                if reel_link and reel_link not in downloaded_links:
                    try:
                        shortcode = reel_link.split("/")[-2]
                        post = Post.from_shortcode(loader.context, shortcode)
                        if is_recent_post(post):
                            reels_links.add(reel_link)
                            if len(reels_links) >= num_reels:
                                return list(reels_links)
                        else:
                            logging.info(f"Reel {reel_link} is older than 24 hours. Skipping remaining reels for {username}.")
                            return list(reels_links)  # Return the current set if no recent reels are found
                    except InstaloaderException as e:
                        logging.error(f"Error loading post {reel_link}: {e}")
                    except Exception as e:
                        logging.error(f"Unexpected error processing reel {reel_link}: {e}")
            time.sleep(random.uniform(2, 5))  # Wait between requests to avoid being flagged
        return list(reels_links)[:num_reels]
    except Exception as e:
        logging.error(f"Error fetching reels for {username}: {e}")
        return []

def download_reels(loader, links, username):
    """Download Instagram reels given their links and save them in the specified directory."""
    user_folder = f'reels/{username}'
    os.makedirs(user_folder, exist_ok=True)

    downloaded_count = 0
    for link in links:
        try:
            shortcode = link.split("/")[-2]
            post = Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target=user_folder)
            logging.info(f"Downloaded: {link}")
            downloaded_count += 1
        except InstaloaderException as e:
            logging.error(f"Failed to download {link}: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while downloading {link}: {e}")

    return downloaded_count

def login_instaloader(loader, username, password, session_file):
    """Login to Instagram using Instaloader and save the session."""
    try:
        if os.path.exists(session_file):
            loader.load_session_from_file(username, session_file)
            logging.info(f"Loaded session from file for {username}")
        else:
            loader.login(username, password)
            loader.save_session_to_file(session_file)
            logging.info(f"Logged in and saved session for {username}")
    except InstaloaderException as e:
        logging.error(f"Login failed: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during login: {e}")
        raise

def load_json_file(file_path):
    """Load JSON data from a file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            logging.error(f"Error loading JSON file {file_path}: {e}")
            return {}
        except Exception as e:
            logging.error(f"Unexpected error loading JSON file {file_path}: {e}")
            return {}
    return {}

def save_json_file(file_path, data):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving JSON file {file_path}: {e}")
        sys.exit()

def main_download_reels(num_videos, download_configuration_file):
    """Main function to manage the downloading of Instagram reels with enhanced features."""
    data = load_json_file(download_configuration_file)
    json_file_path = data.get("usernames_file")
    last_username_file = data.get("last_username_file")
    downloaded_links_file = data.get("downloaded_links_file")
    instaloader_username = data.get("instaloader_username")
    instaloader_password = data.get("instaloader_password")
    session_file = data.get("session_file")
    profile_path = data.get("firefox_profile_path")
    geckodriver_path = data.get("geckodriver_path")

    driver = setup_driver(profile_path, geckodriver_path)
    loader = Instaloader()

    try:
        # Attempt login with retries
        for attempt in range(3):
            try:
                login_instaloader(loader, instaloader_username, instaloader_password, session_file)
                break
            except InstaloaderException as e:
                logging.error(f"Login attempt {attempt + 1} failed: {e}")
                if attempt == 2:
                    logging.error("Max login attempts reached. Exiting.")
                    return 0
                time.sleep(random.uniform(2, 5))  # Wait before retrying login

        print("Download started....")
        all_reels_links = []
        username_reels_count = {}
        downloaded_links = load_json_file(downloaded_links_file)
        last_username = load_json_file(last_username_file).get('last_username')

        driver.get('https://www.instagram.com/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        time.sleep(random.uniform(5, 10))

        with open(json_file_path, 'r') as file:
            usernames_dict = json.load(file)

        usernames = list(usernames_dict.values())
        start_index = usernames.index(last_username) + 1 if last_username in usernames else 0

        for i in range(start_index, start_index + len(usernames)):
            username = usernames[i % len(usernames)]  # Cycle through usernames
            if username not in downloaded_links:
                reels = get_instagram_reels_links(driver, loader, username, max(num_videos // len(usernames), 1), downloaded_links.get(username, []))
                username_reels_count[username] = len(reels)
                all_reels_links.extend(reels)
                downloaded_links.setdefault(username, []).extend(reels)
                save_json_file(last_username_file, {'last_username': username})
                time.sleep(random.uniform(2, 5))  # Wait between requests

                if len(all_reels_links) >= num_videos:
                    break

        all_reels_links = list(set(all_reels_links))[:num_videos]
        downloaded_count = download_reels(loader, all_reels_links, 'reels') if all_reels_links else 0

        save_json_file(downloaded_links_file, downloaded_links)

        logging.info(f"Total number of videos downloaded: {downloaded_count}")
        logging.info(f"Number of reels fetched from each username: {username_reels_count}")
        move_and_log_files(data)

        return downloaded_count

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit()

    finally:
        driver.quit()
        logging.info("Driver has been cleaned up.")


num_videos  = 2
download_configuration_file = r"D:\my_pro\instagram_to_youtube\youtube_channel\meems\download_configuration.json"
main_download_reels(num_videos, download_configuration_file)