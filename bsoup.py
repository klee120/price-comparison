from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = "http://olympus.realpython.org"
page = urlopen(base_url + "/profiles")
html = page.read().decode("utf-8")

# Exercise: get the urls using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")
# a1, a2, a3 = soup.find_all("a")

# Exercise: extract Name and favorite color
for a in soup.find_all("a"):
    link = base_url + a["href"]
    print(link)

