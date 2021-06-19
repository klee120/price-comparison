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
url = "https://www.smartandfinal.com/"


def item_url(search_term):
    base_url = "https://www.smartandfinal.com/shop/?query={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url(input("Enter an item: "))

driver.get(url)

hsoup = soup(driver.page_source, "html.parser")

products = hsoup.findAll("product-card")

with open("SmartFinal.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    headers = ["Name", "Current Price", "Unit Price", "Original Price"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for product in products:
        name = product.select(".product-name")[0].text
        pricess = product.select(".sr-only")
        current = pricess[0].text

        if len(pricess) > 1:
            original = pricess[1].text
            writer.writerow(
                {"Name": name, "Current Price": current, "Original Price": original,}
            )
        else:
            writer.writerow(
                {"Name": name, "Current Price": current,}
            )
