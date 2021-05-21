import mechanicalsoup
import time

browser = mechanicalsoup.Browser()
# real-time scraping

# refreshes every 10 seconds, and does this 4 times
for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]  # selects element with id = result
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    if i < 3:
        time.sleep(2)

