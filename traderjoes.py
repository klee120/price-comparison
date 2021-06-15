from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys
import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.traderjoes.com"


def item_url(search_term):
    base_url = "https://www.traderjoes.com/home/search?q={ITEM}&section=products"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)

# use stdin
url = item_url("avocado")
driver.get(url)

hsoup = soup(driver.page_source, "html.parser")
print(hsoup.prettify())

# products = hsoup.select(".Section_section__oNcdC").findAll('article')
products = hsoup.find("li")
print(products)
# paragraphs = soup.find('article').find("div", {'class': 'bd'}).find_all('p')

# products = hsoup.findAll("article", class_= "SearchResultCard_searchResultCard__3V-_h")

with open("TraderJoes.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "Current Price", "Unit Price", "Original Price"])
    for product in products:
        name = product.select(".SearchResultCard_searchResultCard__title__2PdBv")[0].text
        # Link_link__1AZfr
        unit = product.select(".ProductPrice_productPrice__unit__2jvkA")[0].text
        prices = product.select(".ProductPrice_productPrice__price__3-50j")[0].text
        
        print(f"{name}: {prices}, {unit}")
        writer.writerow([name, prices, unit])
