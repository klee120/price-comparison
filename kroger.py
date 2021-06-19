from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys
import re
import csv
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from lxml import html

driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.kroger.com/"


def item_url(search_term):
    base_url = "https://www.kroger.com/search?query={ITEM}&searchType=default_search&fulfillment=all"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


# <div class="AutoGrid-cell min-w-0"

url = item_url("avocado")
driver.get(url)

# page = requests.get(url)

hsoup = soup(driver.page_source, "html.parser")
products = hsoup.findAll("min-w-0")
with open("Kroger.csv", mode="w") as f:
    writer = csv.writer(f, delimiter=",")
    headers = ["Name", "Current Price", "Unit Price", "Original Price"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for product in products:
        name = product.select("h3")[0].text
        current = product.select("data")[0].get("value")
        # current = pricess[0].texts
        writer.writerow({"Name": name, "Current Price": current})
        print(name)
        print(current)

        # if len(pricess) > 1:
        #     original = pricess[1].text
        #     writer.writerow(
        #         {"Name": name, "Current Price": current, "Original Price": original,}
        #     )
        # else:
        #     writer.writerow(
        #         {"Name": name, "Current Price": current}
        #     )


# print(products)


# print(products)
# print(hsoup.prettify())
# dom = etree.HTML(str(hsoup))
# products = dom.xpath(
#     '//*[@id="content"]/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]'
# )

# father.findNext({'id':'content'}).findNext('div').findNext('div').findNext('div').findNext('div')[2].findNext('div')[2].findNext('div')[3].findNext('div').findNext('div').findNext('div')[1]
# dom = tree.xpath(
#     '//*[@id="content"]/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]'
# )

# /html/body/div[1]/div/div[3]/div[1]/main/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div

# //*[@id="content"]/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]
# # products = hsoup.findAll(".kds-Card")
# # //*[@id="content"]/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]
# print(products)

# OPTION 0
# from bs4 import BeautifulSoup
# from lxml import etree
# import requests


# URL = "https://en.wikipedia.org/wiki/Nike,_Inc."

# HEADERS = ({'User-Agent':
# 			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
# 			(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
# 			'Accept-Language': 'en-US, en;q=0.5'})

# webpage = requests.get(URL, headers=HEADERS)
# soup = BeautifulSoup(webpage.content, "html.parser")
# dom = etree.HTML(str(soup))
# print(dom.xpath('//*[@id="firstHeading"]')[0].text)


# OPTION 1
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)
# This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# # OPTION 2
# from lxml import etree
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(open('path of your localfile.html'),'html.parser')
# dom = etree.HTML(str(soup))
# print dom.xpath('//*[@id="BGINP01_S1"]/section/div/font/text()')

