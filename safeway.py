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
url = "https://www.safeway.com"


def item_url(search_term):
    base_url = "https://www.safeway.com/shop/search-results.html?q={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url(input("Enter an item: "))

driver.get(url)

hsoup = soup(driver.page_source, "html.parser")

products = hsoup.findAll("product-item-v2")

with open("Safeway.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "Current Price", "Unit Price", "Original Price"])
    for product in products:
        name = product.select(".product-title")[0].text
        unit = product.select(".product-price-qty")[0].text
        unit = unit.replace("(", "").replace(")", "")
        prices = product.select(".product-price-con")[0].text
        pricess = re.findall("\$[\d]*\.[\d][\d]", prices)
        current = pricess[0]
        if len(pricess) == 2:
            original = pricess[1]
            print(f"{name}: {current}, {unit}, {original}")
            writer.writerow([name, current, unit, original])
        else:
            print(f"{name}: {current}, {unit}")
            writer.writerow([name, current, unit])
