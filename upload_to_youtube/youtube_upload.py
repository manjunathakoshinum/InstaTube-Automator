import logging
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from ..youtube_channels.wispering_bee.configuration import *
from .youtube_details import youtube_details
#from download_upload_setup import *
#from new_check_policy import youtube_channel
import os
def setup_selenium_with_profile(profile_path):
    options = Options()
    options.headless = False  # Set to True if you want to run headless
    options.profile = profile_path
    service = Service(executable_path="D:\\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def login_to_youtube(driver):
    try:
        driver.get('https://studio.youtube.com')
        WebDriverWait(driver, 20).until(EC.title_contains("YouTube Studio"))
        if "YouTube Studio" not in driver.title:
            print("Please login manually.")
            input("Press Enter after logging in...")
        else:
            print("You are already logged in.")
                 
        
    except Exception as e:
        print(f"An error occurred during login: {e}")

        driver.quit()
        sys.exit(1)
    
def youtube_upload_video(duration,FIREFOX_PROFILE_PATH,video_file,title,description,tags,made_for_kids,age_restriction,sort_by,visibility,category):
    driver = None
    try:
        # Setup Selenium and login
        driver = setup_selenium_with_profile(FIREFOX_PROFILE_PATH)
        driver.maximize_window()
        driver.execute_script("document.body.style.zoom='100%'")
        login_to_youtube(driver)
        upload_status = youtube_details(duration,driver,video_file,title,description,tags,made_for_kids,age_restriction,sort_by,visibility,category)
        return upload_status 
        #video elements incomplete
        #video_elemnts(driver)
        #video checks incomplete
        #video_checks()
        #video_visibility(driver)


    except Exception as e:
        logging.error(f"An error occurred during login: {e}")
    finally:
        if driver:
            driver.quit()
