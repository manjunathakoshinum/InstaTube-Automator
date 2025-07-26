
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from preprocessing.get_tags import get_valid_tags
from preprocessing.get_title import get_valid_title
from preprocessing.get_description import get_valid_description
import time
import random
def launch_firefox(geckodriver_path):
    # Set up Firefox options
    options = Options()
    #options.add_argument('--headless')  #if you dont want remove itUncomment this line if you want to run Firefox in headless mode

    # Path to geckodriver executable

    # Set up the service
    service = FirefoxService(executable_path=geckodriver_path)

    # Create a new instance of Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)
    return driver
    # Open a website to test
    
def get_valid_title_description_tags(content,geckodriver_path,command_for_title,command_for_description,command_for_tags,commad_for_hashtags):
    driver = launch_firefox(geckodriver_path)
    time.sleep(5)
    title = get_valid_title(command_for_title,content,driver)
    time.sleep(5)
    description = get_valid_description(command_for_description,content,commad_for_hashtags,driver)
    tags = get_valid_tags(command_for_tags,content,driver)
    driver.quit()
    return title,description,tags
    
    
    
    