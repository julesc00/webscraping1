from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup as bs


def get_html(url: str):
    try:
        html = urlopen(url)
        bs1 = bs(html.read(), "html5lib")
        print(bs1.get_text())
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    else:
        print("It worked!")


def get_html_from_file():
    with open("sample.html", "r") as fp:
        soup = bs(fp, "html.parser")
        print(soup.get_text())


def get_title(url: str):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        soup = bs(html.read(), "html.parser")
        title = soup.body.h1
    except AttributeError:
        return None

    return title


if __name__ == "__main__":
    URL = "http://pythonscraping.com/pages/page1.html"
    get_html(URL)
    get_html_from_file()

    title1 = get_title(URL)
    if title1 is None:
        print("Title couldn't be found.")
    else:
        print("Title: ", title1)
