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






























# and then I tried better but less functionality



def clicked(xpath):
    driver.find_element_by_xpath(xpath).click()
    
def fill_a_field(xpath, string):
    driver.find_element_by_xpath(xpath).send_keys(string)
    
location_of_chrome_driver = '~/Downloads/chromedriver'
website_to_visit = 'https://www.pdfdrive.com/'

# set the xpaths
xpath_search_bar = '//*[@id="q"]'
xpath_search_button = '//*[@id="search-form"]/button/i'
xpath_first_result_button = '/html/body/div[3]/div[1]/div[1]/div[4]/ul/li[1]/div/div/div[2]/a/h2'
xpath_download_button = '//*[@id="download-button-link"]'
xpath_get_pdf_button = '//*[@id="alternatives"]/div[1]/div/a'


# start browser
driver = webdriver.Chrome(executable_path=location_of_chrome_driver)
driver.get(website_to_visit)

# run the things
fill_a_field(xpath_search_bar, 'dataclysm')
clicked(xpath_search_button)
clicked(xpath_first_result_button)
clicked(xpath_download_button)
time.sleep(15) # wait for it to tasty the pdf file
clicked(xpath_get_pdf_button) # actually click the download
time.sleep(6) # wait for it to finish downloading
driver.close()




































# and then I tried my hand at playwright
website_to_visit = 'https://www.pdfdrive.com/'
# books = ['dataclysm', 'oh the places']

xpath_search_bar = '//*[@id="q"]'
xpath_search_button = '//*[@id="search-form"]/button/i'
xpath_first_result_button = 'h2'
xpath_get_pdf_button = '//*[@id="alternatives"]/div[1]/div/a'
xpath_popup = '//*[@id="pdfdriveAlerts"]/div/div/div/i'


async with async_playwright() as p: 
    # start a browser instance
    browser = await p.webkit.launch()#headless=False)
    # create a new incognito browser context
    context = await browser.new_context(accept_downloads= True)    
    # create a new page inside context.
    page = await context.new_page()
    # go to initial page
    await page.goto(website_to_visit)
    
    
    
# Data Extraction Code Here
    for i in books:
        try:
            await page.fill(xpath_search_bar, i) # take xpath and strings from books
            await page.click(xpath_search_button);
            await page.click(xpath_first_result_button);
            await page.click(xpath_download_button);

            # download tricky bullshit
            async with page.expect_download() as download_info:
                await page.click(xpath_get_pdf_button)
            download = await download_info.value
            # waits for download to complete
            path = await download.path()
            print(download.suggested_filename)
            await download.save_as(f'~/Downloads/{download.suggested_filename}') 
        except:
            print(f'could not find {i}')
    
    
    
#     await page.wait_for_timeout(1000)  # Wait for 1 second
    # dispose context once it is no longer needed.
    await context.close()
    await browser.close()