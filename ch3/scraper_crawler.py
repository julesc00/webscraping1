from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup as bs
import re
import random
import datetime


URL = "http://en.wikipedia.org/wiki/Kevin_Bacon"


def scrape_wiki_bacon():
    try:
        html = urlopen(URL)
        soup = bs(html.read(), "html.parser")
        [print(link.attrs["href"]) for link in soup.find_all("a") if "href" in link.attrs]
    except URLError:
        return None


# random.seed(datetime.datetime.now())


def get_links(article_link: str):
    html = urlopen(f"http://en.wikipedia.org{article_link}")
    soup = bs(html, "html.parser")

    return soup.find(
        "div", {"id": "bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = get_links("/wiki/Nikola_Tesla")
while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)


PAGES = set()


def get_links2(page_url: str):
    global PAGES
    html = urlopen(f"http://en.wikipedia.org{page_url}")
    soup = bs(html, "html.parser")
    for link in soup.find_all("a", href=re.compile("^(/wiki/)")):
        if link.attrs["href"] not in PAGES:
            # We have encountered a new page
            new_page = link.attrs["href"]
            print(new_page)
            get_links2(new_page)


get_links2("")
