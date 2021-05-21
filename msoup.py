import mechanicalsoup

# Mechanical Soup helps with interacting with web pages to get
# desired information (e.g. submitting forms, clicking buttons)

# headless web browser, which is a web browser with no graphical interface
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(
    url
)  # status code returned by request (200 = success, 440= doesn't exist, 500  server error)
login_html = login_page.soup  # stores html

# 2 set user and password of desired form
form = login_html.select("form")[0]  # of the list of forms, choose first one
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3 submit form
profiles_page = browser.submit(form, login_page.url)

# prints url = means successful
print(profiles_page.url)

print(profiles_page.soup.title)

links = profiles_page.soup.select("a")

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")

