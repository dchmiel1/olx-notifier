from time import sleep
from selenium import webdriver

OLX_URL = "https://www.olx.pl/dom-ogrod/meble/grojec/q-oddam-za-darmo/?search%5Bdist%5D=75&search%5Border%5D=created_at%3Adesc"


def scroll_page_slowly(driver):
    page_height = driver.execute_script("return document.body.scrollHeight")
    height = 0
    sleep(0.25)
    while height < page_height:
        height += 500
        driver.execute_script(f"window.scrollTo(0, {height});")
        sleep(0.25)


def fetch_offers_page():
    driver = webdriver.Chrome()
    driver.get(OLX_URL)
    scroll_page_slowly(driver)
    return driver.page_source
