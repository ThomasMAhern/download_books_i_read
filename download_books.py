!pip3 install selenium
!pip3 install beautifulsoup4
!pip3 install fake_useragent

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from lxml import html
import requests
from bs4 import BeautifulSoup
import random

# so you don't get flagged as a bot
from fake_useragent import UserAgent

# for captcha clicking
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC





book_2_dl = 'dataclysm'
location_of_chrome_driver = '~/Downloads/chromedriver'
website_to_visit = 'https://www.pdfdrive.com/'

# start browser
driver = webdriver.Chrome(executable_path=location_of_chrome_driver)
driver.get(website_to_visit)

# search bar
search_bar = driver.find_element_by_xpath('//*[@id="q"]')
search_bar.send_keys(book_2_dl)

# click
search = driver.find_element_by_xpath('//*[@id="search-form"]/button/i')
search.click()

# select first result
result = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[2]/a/h2')
result.click()

# click download button
download_button = driver.find_element_by_xpath('//*[@id="download-button-link"]')
download_button.click()

# wait for resource to load
time.sleep(15)

# download pdf
get_pdf = driver.find_element_by_xpath('//*[@id="alternatives"]/div[1]/div/a')
get_pdf.click()

# x out of ad
fuck_ads = driver.find_element_by_xpath('//*[@id="pdfdriveAlerts"]/div/div/div/i')
fuck_ads.click()