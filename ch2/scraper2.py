from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bs
import re

URL = "http://www.pythonscraping.com/pages/warandpeace.html"
PAGE_3_URL = "https://www.pythonscraping.com/pages/page3.html"

def get_html():
    try:
        html = urlopen(URL)
        soup = bs(html.read(), "html.parser")

        name_list = soup.findAll("span", {"class": "green"})
        [print(name.get_text()) for name in name_list]

    except URLError:
        return None


def get_h_tags():
    try:
        html = urlopen(URL)
        soup = bs(html.read(), "html.parser")
        h_lists = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        [print(h_tag) for h_tag in h_lists]

        green_red_spans = soup.find_all("span", {"class": {"green", "red"}})
        [print(span.get_text()) for span in green_red_spans]
    except URLError:
        return None

    try:
        prince_items = tuple(soup.find_all(text="the prince"))
        print(len(prince_items))
        title = soup.find(id="title")
        title2 = soup.find_all(id="text")
        print(f"Title: {title}, Title 2: {title2}")
    except URLError:
        return None


def get_prices():
    try:
        html = urlopen(PAGE_3_URL)
        soup = bs(html.read(), "html.parser")
        # [print(child) for child in soup.find("table", {"id": "giftList"}).children]
        # [print(sibling) for sibling in soup.find("table", {"id": "giftList"}).tr.next_siblings]
        print(
            soup.find("img",
                      {"src": "../img/gifts/img3.jpg"})
            .parent.previous_sibling.get_text()
        )
    except URLError:
        return None


def get_images():
    try:
        html = urlopen(PAGE_3_URL)
        soup = bs(html.read(), "html.parser")
        images = soup.find_all(
            "img",
            {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")}
        )
        [print(img["src"]) for img in images]
    except URLError:
        return None


# get_html()
# get_h_tags()
# get_prices()
get_images()
