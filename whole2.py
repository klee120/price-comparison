from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys
import re
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.wholefoodsmarket.com"


def item_url(search_term):
    base_url = "https://www.wholefoodsmarket.com/search?text={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url("avocado")

driver.get(url)

e = driver.find_element_by_id("pie-store-finder-modal-search-field")
print(e)
# e.sendKeys(int(08544))
# e.sendKeys(Keys.ENTER)

# element = Select(driver.find_element_by_class_name("wfm-search-bar--list_isssstem"))
# ssselement.select_by_index(0)

hsoup = soup(driver.page_source, "html.parser")

# form = hsoup.select("wfm-search-bar")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"

# print(hsoup.prettify())

