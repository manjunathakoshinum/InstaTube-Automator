from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re 
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options

    
    
def search_get_title(search_element,driver):
    driver.get('https://www.blackbox.ai/')
    WebDriverWait(driver,35).until(EC.presence_of_element_located((By.XPATH,'//*[@id="chat-input-box"]')))
    search_box_xpath = '//*[@id="chat-input-box"]' # XPath for the YouTube search box
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    search_box.send_keys(search_element)  # Type the search query
    search_box.send_keys(Keys.RETURN) # Type the search query
    
    try:
         
        WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div[3]")))
        
        time.sleep(2)

    finally:
        element_xpath = '/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div[1]/div/div[2]'  # Replace with the XPath to your target element
        element = driver.find_element(By.XPATH, element_xpath)
        text = element.text.strip()
        match = re.search(r'\[(.*?)\]', text)
        extracted_text = match.group(1) if match else 'No text found in brackets'
        return extracted_text

def get_valid_title(title_command,content,driver): 
    print("getting title")
    if content ==None:
        title = search_get_title(title_command,driver)
    else:
        search_content = f"{content} use this content for getting idea about the video incorporate to amke compitative tilte {title_command} ,only one title"
        title = search_get_title(search_content,driver)
    if title:
        if len(title)<10:
            pass              
    return title
# Call the function

