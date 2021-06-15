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
url = "https://www.costco.com/"


def item_url(search_term):
    base_url = "https://www.costco.com/CatalogSearch?dept=All&keyword={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url(input("Enter an item: "))

driver.get(url)

# click change button to input zip code
# zip_code_button = driver.find_element_by_id("delivery-postal-change")
# zip_code_button.click()

# enter zip code


hsoup = soup(driver.page_source, "html.parser")

products = hsoup.findAll("div", class_="product-tile-set")

with open("Costco1.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "Current Price", "Unit Price", "Original Price"])
    for product in products:
        name = product.select(".description")[0].text.strip(" \r\n\t")
        # Link_link__1AZfr
        # unit = product.select(".ProductPrice_productPrice__unit__2jvkA")[0].text
        prices = product.select(".price")[0].text
        pricess = re.findall("\$[\d]*\.[\d][\d]", prices)[0]

        writer.writerow([name, pricess])

