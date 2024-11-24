'''
Selenium is a powerful tool used in software
development testing to automate web browsers.

Why Use Selenium?
    1. Testing Websites.
    2. Automating Repetitive Tasks: 
        a. like filling out forms
        b. clicking through multiple pages
        c. scraping data.

How Does Selenium Work?
Selenium uses "WebDrivers" to control different
browsers.

ChromeDriver for Google Chrome
GeckoDriver for Firefox
'''

# pip install selenium webdriver-manager
# Bewakoof Coders channel: 
# "https://www.youtube.com/@BewakoofCoders"
# Sentiment Analysis Video: 
# "https://www.youtube.com/watch?v=oHPWieW3c74"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    channel_url = "https://www.youtube.com/@BewakoofCoders"
    driver.get(channel_url)

    video_url = "https://www.youtube.com/watch?v=oHPWieW3c74"
    driver.get(video_url)

    play_button = driver.find_element(By.CLASS_NAME, 'ytp-play-button')
    play_button.click()

    video_duration = 15
    time.sleep(video_duration)
finally:
    driver.quit()