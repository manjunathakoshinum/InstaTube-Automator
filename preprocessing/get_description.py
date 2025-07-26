import json
import random
import time
import re 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService

def search_get_description(search_element,driver):
    driver.get('https://www.blackbox.ai/')
    WebDriverWait(driver,35).until(EC.presence_of_element_located((By.XPATH,'//*[@id="chat-input-box"]')))
    search_box_xpath = '//*[@id="chat-input-box"]' # XPath for the YouTube search box
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    search_box.send_keys(search_element)  # Type the search query
    search_box.send_keys(Keys.RETURN) # Type the search query 
    WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div[3]")))

    # Wait until the body element is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Extract the text
    page_text = driver.find_element(By.TAG_NAME, 'body').text

    brackets_text = re.findall(r'\[([^\]]*)\]', page_text)
    result_string = ' '.join(brackets_text)
    # Close the browser
    #driver.quit()
    return result_string
    
    
    
def trim_text(text, max_length=4800):
    # Split the text into words
    words = text.split()
    
    # If the text is already within the limit, return it
    if len(text) <= max_length:
        return text
    
    # Initialize the trimmed text
    trimmed_text = ""
    
    # Add words to the trimmed text until the length limit is reached
    for word in words:
        # Check if adding this word would exceed the length limit
        if len(trimmed_text) + len(word) + 1 > max_length:
            break
        
        # Append the word to the trimmed text
        if trimmed_text:
            trimmed_text += " "
        trimmed_text += word
    
    return trimmed_text

def get_valid_description(description_command,content,commad_for_hashtags,driver):
    print("getting description..")
    if content ==None:
        search_content = description_command
    else:
        search_content = f"{description_command}use this content for getting idea you can add tags or content in ths incorporate to and incluede some  related things {content} about the video , description"
    description = search_get_description(search_content,driver)
    if description:
        if len(description)<3500:
            hashtags = search_get_description(commad_for_hashtags,driver)
            description  = description + hashtags 
            if len(description)>4800:
                description = trim_text(description)
        if len(description)>4800:
            description = trim_text(description)
        return description
    return None
            
            
   
   
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
        
    
    
    
    
    
    
    
    
    
    
# Example usage
# Example usage
#initial_text = "rt of natureâ€™s most enigmatic and stunning locations, where the earth reveals its hidden marvels. This expedition will guide you through environments that defy human imagination, from the bioluminescent wonders of glowing caves to the surreal landscapes of high-altitude deserts. Traverse through dense jungles echoing with the calls of exotic birds, and navigate rivers that cut through ancient rock formations. Each step brings a new discovery, a new story waiting to be told, and a deeper understanding of the intricate tapestry that makes up our planet's most mysterious places.Untamed Beauty "
#json_file = r'D:\new_instagram_to_youtube\nature_details\descriptions\description.json'
#tag_file = r'D:\new_instagram_to_youtube\nature_details\descriptions\Nature_hashtag.txt'
#json_data = load_json(json_file)
#tags = load_tags(tag_file)
#generated_text = generate_text(initial_text, json_data, tags)
#print(generated_text)
#print(f"Length of generated text: {len(generated_text)}")
