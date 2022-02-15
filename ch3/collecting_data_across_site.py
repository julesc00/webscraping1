from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

PAGES = set()
URL = "http://en.wikipedia.org"


def get_links(page_url: str):
    global PAGES
    global URL
    html = urlopen(f"{URL}{page_url}")
    soup = bs(html, "html.parser")

    try:
        print(soup.h1.get_text())
        print(soup.find(id="mw-content-text").find_all("p")[0])
        print(soup.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("This page is missing something! Continuing.")
    counter = 20

    while counter:
        for link in soup.find_all("a", href=re.compile("^(/wiki/)")):
            if "href" in link.attrs:
                if link.attrs["href"] not in PAGES:
                    # Encountered a new page
                    new_page = link.attrs["href"]
                    print("-" * 20)
                    print(new_page)
                    PAGES.add(new_page)
                    counter -= 1
                    get_links(new_page)

                with open("links.txt", "a") as f:
                    for page in PAGES:
                        page_str = URL + page + "\n"
                        f.write(page_str)


if __name__ == "__main__":
    with open("links.txt", "w") as f:
        f.write("Links\n")
    print("Text file created.")
    get_links("")
