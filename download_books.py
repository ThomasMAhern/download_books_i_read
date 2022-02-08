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














books = ["The Mind's Eye",
    "The Genius in All of Us: Why Everything You've Been Told About Genetics, Talent, and IQ Is Wrong",
    "Being Wrong: Adventures in the Margin of Error",
    "The Invisible Gorilla: And Other Ways Our Intuitions Deceive Us",
    "The Shallows: What the Internet Is Doing to Our Brains",
    "Phantoms in the Brain: Probing the Mysteries of the Human Mind",
    "NurtureShock: New Thinking About Children",
    "Everyday Survival: Why Smart People Do Stupid Things",
    "Outliers: The Story of Success",
    "The God Delusion",
    "Traffic: Why We Drive the Way We Do and What It Says About Us",
    "The Unthinkable: Who Survives When Disaster Strikes - and Why",
    "The Tipping Point: How Little Things Can Make a Big Difference",
    "The Selfish Gene",
    "Made to Stick: Why Some Ideas Survive and Others Die",
    "Blink: The Power of Thinking Without Thinking",
    "The Man Who Mistook His Wife for a Hat and Other Clinical Tales",
    "Future Crimes",
    "Blueprint: How DNA makes us who we are",
    "I Contain Multitudes: The Microbes Within Us and a Grander View of Life",
    "Invisible Women: Data Bias in a World Designed for Men",
    "Behave: The Biology of Humans at Our Best and Worst"]




















## Selenium
# and then I tried better but less functionality



def clicked(xpath):
    '''Click on a xpath element'''
    driver.find_element_by_xpath(xpath).click()
    
def fill_a_field(xpath, string):
    '''Send text values into an input field'''
    driver.find_element_by_xpath(xpath).send_keys(string)# def get_a_book(book_title):

def navigate_to_book_dl(book_name):
    '''Give book name, it clicks through to result'''
    fill_a_field(xpath_search_bar, book_name)
    clicked(xpath_search_button)
    clicked(xpath_first_result_button)

def actually_download():
    '''From book page, click and wait for download'''
    clicked(xpath_download_button)
    time.sleep(15) # wait for it to tasty the pdf file
    clicked(xpath_get_pdf_button) # actually click the download
    time.sleep(6) # wait for it to finish downloading
    
# Where are the things?
location_of_chrome_driver = '~/Downloads/chromedriver'
website_to_visit = 'https://www.pdfdrive.com/'
# books = ['dataclysm']

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
for book in books:    
    navigate_to_book_dl(book)
    actually_download()

driver.close()

































## Playwright


# and then I tried my hand at playwright

website_to_visit = 'https://www.pdfdrive.com/'
# books = ['dataclysm', 'oh the places']

xpath_search_bar = 'id=q'
xpath_search_button = '//*[@id="search-form"]/button/i'
selector_first_result_button = 'body > div.dialog > div.dialog-main > div.dialog-left > div.files-new > ul > li:nth-child(1) > div > div > div.file-right > a'
xpath_dropdown_button = '//*[@id="alternatives"]/div[1]/div/button'
xpath_download_button = '//*[@id="download-button-link"]'
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
    for book_title in books:
        try:
            await page.fill(xpath_search_bar, book_title) # take xpath and strings from books
            await page.click(xpath_search_button)
            await page.click(selector_first_result_button)
            await page.click(xpath_download_button)

            # download tricky bullshit
            async with page.expect_download() as download_info:
                await page.click(xpath_get_pdf_button)
            download = await download_info.value
            # waits for download to complete
            path = await download.path()
            print(download.suggested_filename)
            await download.save_as(f'~/Downloads/{download.suggested_filename}') 
        except:
            print(f'This one failed: {book_title}')
    
    
    
#     await page.wait_for_timeout(1000)  # Wait for 1 second
    # dispose context once it is no longer needed.
    await context.close()
    await browser.close()
    
    
    
    
    
    
    
    
    




# from playwright.async_api import async_playwright

# hooray learned about context managers.... or more specifically, how to get rid of one

playwright = async_playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("http://whatsmyuseragent.org/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()

# is same as 

async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context(accept_downloads= True)
    page = await context.new_page()
    await page.goto('http://whatsmyuseragent.org/')
    await page.screenshot(path="example.png")