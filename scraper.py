from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from log import logger

OLX_URL = "https://www.olx.pl/dom-ogrod/meble/grojec/q-oddam-za-darmo/?search%5Bdist%5D=75&search%5Border%5D=created_at%3Adesc"

logger.info("Initializing web driver...")
options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("window-size=1024,768")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
logger.info("Web driver initialized")


def scroll_page_slowly(driver):
    page_height = driver.execute_script("return document.body.scrollHeight")
    height = 0
    sleep(0.25)
    while height < page_height:
        height += 500
        driver.execute_script(f"window.scrollTo(0, {height});")
        sleep(0.25)


def fetch_offers_page():
    driver.get(OLX_URL)
    logger.info("Page fetched")
    scroll_page_slowly(driver)
    logger.info("Scrolling finished")
    return driver.page_source
