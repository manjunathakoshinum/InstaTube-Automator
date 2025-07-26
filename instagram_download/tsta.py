import json
import random
import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import instaloader
from instaloader import InstaloaderException, Instaloader
import sys

# Setup logging
logging.basicConfig(filename='instagram_reels_downloader.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver(profile_path, geckodriver_path):
    """Setup the Selenium WebDriver with the specified profile and geckodriver."""
    try:
        options = Options()
        options.headless = False  # Set to True if you want the browser to be invisible

        profile = webdriver.FirefoxProfile(profile_path)
        options.profile = profile

        service = Service(executable_path=geckodriver_path)
        return webdriver.Firefox(service=service, options=options)
    except Exception as e:
        logging.error(f"Error setting up WebDriver: {e}")
        raise

def scroll_to_load_content(driver):
    """Scroll down the page to load more content."""
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 5))  # Dynamic wait time for slower networks
        new_height = driver.execute_script("return document.body.scrollHeight")
        return new_height != last_height
    except Exception as e:
        logging.error(f"Error during scrolling: {e}")
        return False

def get_instagram_reels_links(driver, username, num_reels, downloaded_links):
    """Fetch a set of Instagram reels links for a given username."""
    try:
        driver.get(f'https://www.instagram.com/{username}/')
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        reels_links = set()
        found_reel = False

        while len(reels_links) < num_reels:
            if scroll_to_load_content(driver):
                reels_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/reel/')]")
                logging.info(f"Found {len(reels_elements)} reel elements on the current page for {username}.")
                for elem in reels_elements:
                    reel_link = elem.get_attribute('href')
                    if reel_link and reel_link not in downloaded_links:
                        reels_links.add(reel_link)
                        if len(reels_links) >= num_reels:
                            return list(reels_links)  # Return early if we have enough links
                found_reel = True
                if not found_reel:
                    break  # Stop if no new content is loaded
            else:
                break  # Stop if no new content is loaded

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


def load_data(downalod_configuration_file):
    if os.path.exists(downalod_configuration_file):
        with open(downalod_configuration_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print(f"error occured with downlaod configuration file in download{downalod_configuration_file}")

def main_download_reels(num_videos,download_configuration_file):
    """Main function to manage the downloading of Instagram reels."""
    data = load_data(download_configuration_file)
    json_file_path = data["usernames_file"]
    last_username_file = data["last_username_file"]
    downloaded_links_file = data["downloaded_links_file"]
    instaloader_username = data["instaloader_username"]
    instaloader_password = data["instaloader_password"] 
    session_file = data["session_file"]
    profile_path = data["firefox_profile_path"]  # Update with your Firefox profile path
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
                return
            logging.info(f"Retrying login ({login_attempts}/{max_login_attempts})...")
            time.sleep(random.uniform(5, 10))  # Wait before retrying login

    all_reels_links = []
    username_reels_count = {}
    downloaded_links = load_downloaded_links(downloaded_links_file)

    try:
        driver.get('https://www.instagram.com/')
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        with open(json_file_path, 'r') as file:
            usernames_dict = json.load(file)

        for username in usernames_dict.values():
            if username not in downloaded_links:
                reels = get_instagram_reels_links(driver, username, max(num_videos // len(usernames_dict), 1), downloaded_links.get(username, []))
                username_reels_count[username] = len(reels)
                all_reels_links.extend(reels)
                downloaded_links.setdefault(username, []).extend(reels)
                time.sleep(random.uniform(2, 5))  # Wait between requests to avoid being flagged

                if len(all_reels_links) >= num_videos:
                    break

        # Ensure we only take num_videos links
        all_reels_links = list(set(all_reels_links))[:num_videos]
        if all_reels_links:
            downloaded_count = download_reels(loader, all_reels_links, 'reels')

        save_downloaded_links(downloaded_links_file, downloaded_links)

        logging.info(f"Total number of videos downloaded: {downloaded_count}")
        logging.info(f"Number of reels fetched from each username: {username_reels_count}")

        return downloaded_count

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit()

    finally:
        driver.quit()
        logging.info("Driver has been cleaned up.")

num_videos = 10  # Number of videos to download
d = r"D:\instagram_to_youtube\youtube_channel\movies\download_configuration.json"
main_download_reels(num_videos,d)