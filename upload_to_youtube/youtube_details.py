
import time
import sys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from youtube_channel.check_up_policy_upload import youtube_upload_fail
#from youtube_channels.wispering_bee.configuration import *
def youtube_details(duration,driver,video_path,title,description,tags,made_for_kids,age_restriction,sort_by,visibility,category):   
    try:      
        print(f"Trying to upload  😎 ")
        #Login  and upload video
        upload_video(driver,video_path)
        #title 
        title_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'textbox')))
        title_box.clear()
        title_box.send_keys(title)
        # Description
        description_box = driver.find_element(By.CSS_SELECTOR, "#description-textarea > ytcp-form-input-container:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ytcp-social-suggestion-input:nth-child(1) > div:nth-child(1)")
        description_box.clear()
        description_box.send_keys(description)
        # Thumbnail
        #thumbnail_button = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[accept="image/*"]'))
        #    )
        #thumbnail_button.send_keys(thumbnail_path) 
        #playlists
        #Audience
        # Made for kids
        try:
            if made_for_kids:
                WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"tp-yt-paper-radio-button.ytkc-made-for-kids-select:nth-child(1) > div:nth-child(2) > ytcp-ve:nth-child(1)")))
                kids_radio_button = driver.find_element(By.CSS_SELECTOR, 'tp-yt-paper-radio-button.ytkc-made-for-kids-select:nth-child(1) > div:nth-child(2) > ytcp-ve:nth-child(1)')
                kids_radio_button.click()
            else:
                WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"tp-yt-paper-radio-button.ytkc-made-for-kids-select:nth-child(2) > div:nth-child(2) > ytcp-ve:nth-child(1)")))
                not_kids_radio_button = driver.find_element(By.CSS_SELECTOR, 'tp-yt-paper-radio-button.ytkc-made-for-kids-select:nth-child(2) > div:nth-child(2) > ytcp-ve:nth-child(1)')
                not_kids_radio_button.click()
        except Exception as e:
            print(f"An error occurred during made  for kids:in details {e}")
            youtube_upload_fail()
            
        #Age restriction(advanced)
        #Do you want to restrict your video to an adult audience? 
        try:
             if age_restriction:
                age_restriction_toggle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.section-label')))
                age_restriction_toggle.click()
                age_restriction_yes_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tp-yt-paper-radio-button.ytcp-age-restriction-select:nth-child(1) > div:nth-child(2) > ytcp-ve:nth-child(1)')))
                age_restriction_yes_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tp-yt-paper-radio-button.ytcp-age-restriction-select:nth-child(1) > div:nth-child(2) > ytcp-ve:nth-child(1)')))
                time.sleep(1)
                age_restriction_yes_button.click()
        except Exception as e:
                print(f"An age.................................... {e}")
                youtube_upload_fail()
        # Show more options
        try:
            time.sleep(10)
            show_more_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#toggle-button > ytcp-button-shape:nth-child(1) > button:nth-child(1) > yt-touch-feedback-shape:nth-child(2) > div:nth-child(1)')))
            driver.execute_script("arguments[0].scrollIntoView();", show_more_button)
            #show_more_button = driver.find_element((By.CSS_SELECTOR, '#toggle-button > ytcp-button-shape:nth-child(1) > button:nth-child(1) > yt-touch-feedback-shape:nth-child(2) > div:nth-child(1)'))
            show_more_button.click()
        except Exception as e:
            print(f"An error occurred during login:in show more options {e}")
            youtube_upload_fail()
        #paid promotion
        #Altered content
        #automatic chapters
        #featured places
        #automatic concepts

        #tags
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".chip-bar > div:nth-child(1) > input:nth-child(4)")))
            tags_box = driver.find_element(By.CSS_SELECTOR, '.chip-bar > div:nth-child(1) > input:nth-child(4)')
            tags_box.send_keys(tags)
            tags_box.send_keys(Keys.ENTER)
        except:
            tags_box = driver.find_element(By.CSS_SELECTOR,"input.text-input:nth-child(12)")
              
        #Language and captions certification
        #Recording date and location
        #License
        #allow embedding
        #Publish to subscriptions feed and notify subscribers
        #Shorts remixing
        # Category
        category_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#category > ytcp-select:nth-child(1) > ytcp-text-dropdown-trigger:nth-child(1) > ytcp-dropdown-trigger:nth-child(1) > div:nth-child(2) > div:nth-child(5)'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", category_dropdown)
        category_dropdown.click()
        time.sleep(1)
        
        category_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[{category}]/ytcp-ve/tp-yt-paper-item-body/div/div')))
        category_option.click()
        try:
            sort_by_toggle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.row:nth-child(4) > ytcp-form-select:nth-child(1) > ytcp-select:nth-child(1) > ytcp-text-dropdown-trigger:nth-child(1) > ytcp-dropdown-trigger:nth-child(1) > div:nth-child(2) > div:nth-child(5) > tp-yt-iron-icon:nth-child(2)')))
            sort_by_toggle.click()
            if sort_by =="top":
                sort_top_new = 1
            else:
                sort_top_new = 2
        
            sort_by_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/ytcp-text-menu[2]/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[{sort_top_new}]/ytcp-ve/tp-yt-paper-item-body/div/div')))
            sort_by_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/ytcp-text-menu[2]/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[{sort_top_new}]/ytcp-ve/tp-yt-paper-item-body/div/div')))
            time.sleep(1)
            sort_by_button.click()

        except Exception as e:
                print(f"An  error in sort_by{e}")
                youtube_upload_fail()
        #comments and ratings
        #comment moderation
        #comment off
        time.sleep(5)
        next = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        next.click()
        #video elements
        time.sleep(6)
        next.click()
        #checks
        time.sleep(9)
        next.click()

        #visibility
        if visibility == "private":
            visibility_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="private-radio-button"]' )))
            visibility_button.click()
        elif visibility == "unlisted":
            visibility_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tp-yt-paper-radio-button.style-scope:nth-child(13)")))
            visibility_button.click()
        else:
            visibility_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tp-yt-paper-radio-button.style-scope:nth-child(21)")))
            visibility_button.click()
    
        try:
            publish_or_save = driver.find_element(By.XPATH, '//html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
            publish_or_save.click()
        except:
            next = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
            next.click()
        sleep = duration *3
        time.sleep(sleep)
        # Replace with the XPath to your target element
        # Wait for a while to make sure the video gets uploaded
        # Close the browser
        # Add video details
        status_of_upload = 0 #if sucess else 1if fails 
        return status_of_upload
    except TimeoutException as e:
        print(f"An error occurred during upload :in details {e}")
        youtube_upload_fail
        status_of_upload = 1 
        driver.quit()
    except Exception as e:
        print(f"An  error in upload{e}")
        youtube_upload_fail
        status_of_upload = 1
        driver.quit()

        
def upload_video(driver, video_path,):
    try:
        driver.get("https://www.youtube.com/upload")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "Filedata"))).send_keys(video_path) 
        
        # Wait for the video to upload and processing to start
        time.sleep(9)  # Adjust sleep time as necessary       
        print("Video uploaded part is sucessfull")
    except Exception as e:
        print(f"An error occurred during video upload: {e}")
        driver.quit()



