from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys
import re
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# start webdriver
driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.safeway.com"

# create url with inputted search term
def item_url(search_term):
    base_url = "https://www.safeway.com/shop/search-results.html?q={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


# url with search term
url = item_url(input("Enter an item: "))

# go to specified url
driver.get(url)

# button to enter zip code
zip_code_button = driver.find_element_by_class_name("reserve-nav__button")
zip_code_button.click()

# enter zip code
zipcode = input("Zipcode: ")
enter = driver.find_element_by_class_name("fulfillment-content__search-wrapper__input")
enter.send_keys(zipcode)
enter.send_keys(Keys.ENTER)

# select closest store
driver.find_element_by_xpath(
    '//*[@id="fulfilmentInStore"]/div/div/div[1]/store-card/div[2]/div/a'
).click()

# scrape website
hsoup = soup(driver.page_source, "html.parser")
products = hsoup.findAll("product-item-v2")

# write to csv using dictionary
with open("Safeway.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    headers = ["Name", "Current Price", "Unit Price", "Original Price"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for product in products:
        name = product.select(".product-title")[0].text.strip(" \r\n\t")
        unit = product.select(".product-price-qty")[0].text
        unit = unit.replace("(", "").replace(")", "")
        prices = product.select(".product-price-con")[0].text
        pricess = re.findall("\$[\d]*\.[\d][\d]", prices)
        current = pricess[0]

        # using dictionary format (can skip columns)
        if len(pricess) == 2:
            original = pricess[1]
            writer.writerow(
                {
                    "Name": name,
                    "Current Price": current,
                    "Unit Price": unit,
                    "Original Price": original,
                }
            )
        else:
            writer.writerow(
                {"Name": name, "Current Price": current, "Unit Price": unit}
            )
