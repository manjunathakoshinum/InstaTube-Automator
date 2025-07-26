#this program download videos uploaded whith in 24 hours , skip user is not found , checks only starting effictive search
#  its running sucessfully but some error with isntaloader
import json
import random
import time
import os
import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from instaloader import Instaloader, InstaloaderException, Post
from datetime import datetime, timedelta, timezone
import instaloader
from instagram_download.move_video_files import move_and_log_files

# Configure logging
logging.basicConfig(filename='instagram_reels_downloader.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver(profile_path, geckodriver_path):
    """Setup the Selenium WebDriver with the specified profile and geckodriver."""
    try:
        options = Options()
        # options.headless = False  # Set to True for headless browsing

        profile = webdriver.FirefoxProfile(profile_path)
        options.profile = profile

        service = Service(executable_path=geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
        return driver
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {e}")
        raise

def scroll_to_load_content(driver):
    """Scroll down the page to load more content with dynamic waiting."""
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 23))  # Randomized sleep to mimic human behavior
        new_height = driver.execute_script("return document.body.scrollHeight")
        return new_height != last_height
    except Exception as e:
        logging.error(f"Error during scrolling: {e}")
        return False

def get_instagram_reels_links(driver, loader, username, num_reels, downloaded_links):
    """Fetch a set of Instagram reels links for a given username."""
    try:
        driver.get(f'https://www.instagram.com/{username}/reels')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        reels_links = set()
        while len(reels_links) < num_reels:
            if scroll_to_load_content(driver):
                reels_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/reel/')]")
                logging.info(f"Found {len(reels_elements)} reel elements on the current page for {username}.")
                for elem in reels_elements:
                    reel_link = elem.get_attribute('href')
                    if reel_link and reel_link not in downloaded_links:
                        # Check if the reel was posted within the last 24 hours
                        shortcode = reel_link.split("/")[-2]
                        post = Post.from_shortcode(loader.context, shortcode)
                        if is_recent_post(post):
                            reels_links.add(reel_link)
                            if len(reels_links) >= num_reels:
                                return list(reels_links)  # Return early if enough links are found
                        else:
                            logging.info(f"Reel {reel_link} is older than 24 hours, skipping remaining reels for {username}.")
                            return list(reels_links)  # Stop if older reel is found
            else:
                break  # Stop if no new content is loaded
        time.sleep(random.uniform(2, 25))
        return list(reels_links)[:num_reels]
    except Exception as e:
        logging.error(f"Error fetching reels for {username}: {e}")
        return []

def is_recent_post(post):
    """Check if the post was created within the last 24 hours."""
    post_time = post.date_utc.replace(tzinfo=timezone.utc)  # Ensure post time is timezone-aware
    current_time = datetime.now(timezone.utc)  # Use timezone-aware datetime for current time
    time_difference = current_time - post_time
    return time_difference <= timedelta(hours=24)

def download_reels(loader, links, username):
    """Download Instagram reels given their links and save them in the specified directory."""
    user_folder = f'reels/{username}'
    os.makedirs(user_folder, exist_ok=True)

    downloaded_count = 0
    for link in links:
        try:
            shortcode = link.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
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

def load_downloaded_links(file_path):
    """Load the list of downloaded links from a JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            logging.error(f"Error loading JSON file: {e}")
            return {}
    return {}

def save_downloaded_links(file_path, data):
    """Save the list of downloaded links to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving downloaded links: {e}")
        sys.exit()

def load_last_username(file_path):
    """Load the last chosen username from a JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file).get('last_username')
        except json.JSONDecodeError as e:
            logging.error(f"Error loading last username JSON file: {e}")
            return None
    return None

def save_last_username(file_path, username):
    """Save the last chosen username to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump({'last_username': username}, file, indent=4)
    except Exception as e:
        logging.error(f"Error saving last username: {e}")
        sys.exit()

def load_data(download_configuration_file):
    if os.path.exists(download_configuration_file):
        with open(download_configuration_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print(f"error occurred with download configuration file in download{download_configuration_file}")

def main_download_reels(num_videos, download_configuration_file):
    """Main function to manage the downloading of Instagram reels with enhanced features."""
    data = load_data(download_configuration_file)
    json_file_path = data["usernames_file"]
    last_username_file = data["last_username_file"]
    downloaded_links_file = data["downloaded_links_file"]
    instaloader_username = data["instaloader_username"]
    instaloader_password = data["instaloader_password"]
    session_file = data["session_file"]
    profile_path = data["firefox_profile_path"]
    geckodriver_path = data["geckodriver_path"]
    driver = setup_driver(profile_path, geckodriver_path)
    loader = Instaloader()

    # Attempt login with retries
    login_attempts = 0
    max_login_attempts = 3
    while login_attempts < max_login_attempts:
        try:
            login_instaloader(loader, instaloader_username, instaloader_password, session_file)
            break
        except InstaloaderException:
            login_attempts += 1
            if login_attempts >= max_login_attempts:
                logging.error("Max login attempts reached. Exiting.")
                driver.quit()
                sys.exit()
            logging.info(f"Retrying login ({login_attempts}/{max_login_attempts})...")
            time.sleep(random.uniform(2, 25))  # Wait before retrying login
    print("download started....")
    all_reels_links = []
    username_reels_count = {}
    downloaded_links = load_downloaded_links(downloaded_links_file)

    if not downloaded_links:
        logging.info("Downloaded links are empty. Proceeding as a fresh run.")

    last_username = load_last_username(last_username_file)

    try:
        driver.get('https://www.instagram.com/')
        time.sleep(random.uniform(5, 34))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        with open(json_file_path, 'r') as file:
            usernames_dict = json.load(file)

        usernames = list(usernames_dict.values())
        start_index = 0

        if last_username:
            if last_username in usernames:
                start_index = (usernames.index(last_username) + 1) % len(usernames)
            else:
                logging.warning(f"Last username '{last_username}' not found in the list. Starting from the beginning.")

        for i in range(start_index, start_index + len(usernames)):
            username = usernames[i % len(usernames)]  # Cycle through usernames
            if username not in downloaded_links:
                reels = get_instagram_reels_links(driver, loader, username, max(num_videos // len(usernames), 1), downloaded_links.get(username, []))
                username_reels_count[username] = len(reels)
                all_reels_links.extend(reels)
                downloaded_links.setdefault(username, []).extend(reels)
                save_last_username(last_username_file, username)
                time.sleep(random.uniform(2, 25))  # Wait between requests to avoid being flagged

                if len(all_reels_links) >= num_videos:
                    break

        # Ensure we only take num_videos links
        all_reels_links = list(set(all_reels_links))[:num_videos]
        if all_reels_links:
            downloaded_count = download_reels(loader, all_reels_links, 'reels')

        save_downloaded_links(downloaded_links_file, downloaded_links)

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
download_configuration_file = r"path to \instagram_to_youtube\youtube_channel\meems\download_configuration.json"
main_download_reels(num_videos, download_configuration_file)