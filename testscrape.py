from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# or html = page.read().decode("utf-8")

# REG EXPRESSIONS AND
# Exercise: extract title of the page
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Remove HTML tags
print(title)

# Exercise: extract Name and favorite color
for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start = string_start_idx + len(string)

    next_tag_offset = html[text_start:].find("<")
    text_end = text_start + next_tag_offset

    raw_text = html[text_start:text_end]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)

# using Beautiful Soup!
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())  # gets only the text from the website
img1, img2 = soup.find_all("img")  # returns each element into img1 and img2
print(img1.name)  # gets name of img1
print(img1["src"])  # can get attributes as if a dictionary
print(soup.title)  # prints <title>Profile: Dionysus</title> cleans up for you!!
print(soup.title.string)  # just Profile: Dionysus
print(
    soup.find_all("img", src="/static/dionysus.jpg")
)  # prints full element of img whose src is as specified

