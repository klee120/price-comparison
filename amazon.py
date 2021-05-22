from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
# import re
import sys

item1 = sys.argv[1]

base_url = "https://www.amazon.com/s?k={ITEM}&ref=nb_sb_noss_1"
url = base_url.replace("{ITEM}", item1)

page = uReq(url)
html = page.read().decode("utf-8")

hsoup = soup(html, "html.parser")
# url = re.sub("{ITEM}", "", url)

products = hsoup.findAll("div", {"data-component-type": "s-search-result"})
print(products)