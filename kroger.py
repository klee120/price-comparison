from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys
import re
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.kroger.com/"


def item_url(search_term):
    base_url = "https://www.kroger.com/search?query={ITEM}&searchType=default_search&fulfillment=all"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url("avocado")

driver.get(url)

hsoup = soup(driver.page_source, "html.parser")

print(hsoup.prettify())
