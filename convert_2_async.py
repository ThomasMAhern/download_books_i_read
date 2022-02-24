!pip3 install playwright
import playwright
from playwright.async_api import async_playwright




website_to_visit = 'https://www.pdfdrive.com/'
books = ['ultralearning']

# xpath_search_bar = '//*[@id="q"]'
xpath_search_bar = 'id=q'
xpath_search_button = '//*[@id="search-form"]/button/i'
selector_first_result_button = 'div.files-new > ul > li:nth-child(1) > div > div > div.file-right > a'
xpath_dropdown_button = '//*[@id="alternatives"]/div[1]/div/button'
xpath_download_button = '//*[@id="download-button-link"]'
xpath_get_pdf_button = '//*[@id="alternatives"]/div[1]/div/a'
xpath_popup = '//*[@id="pdfdriveAlerts"]/div/div/div/i'

async def get_2_dl_button():
    '''walks through search for book on site, then clicks download button'''
    await page.fill(xpath_search_bar, book_title) # take xpath and strings from books
    await page.click(xpath_search_button)
    await page.click(selector_first_result_button)
    await page.click(xpath_download_button)
    
async def akchtually_dl_it():
    '''Does tricky download shit, ensure: new_context(accept_downloads=True)'''
    async with page.expect_download() as download_info:
        await page.click(xpath_get_pdf_button)
    download = await download_info.value 
    path = await download.path() # waits for download to complete
    print(download.suggested_filename)
    await download.save_as(f'/Users/ioktwieaetiq/Downloads/{download.suggested_filename}')
    
    
    

async with async_playwright() as p: 
    browser = await p.chromium.launch(headless=False) # start a browser instance
#     browser = await p.chromium.launch() # start a headless browser instance
    context = await browser.new_context(accept_downloads=True) # create a new incognito browser context 
    page = await context.new_page() # create a new page inside context
    await page.goto(website_to_visit) # go to initial page
#     await page.pause()

        
    # Data Extraction Code Here
    for book_title in books:
        try:
            await get_2_dl_button()
            await akchtually_dl_it()
        except:
            print(f'This one failed: {book_title}')
        



#     await page.wait_for_timeout(1000)  # Wait for 1 second


