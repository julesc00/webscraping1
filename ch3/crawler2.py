import re
import datetime
import random
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup

PAGES = set()


# Retrieve a list of all internal links found on a page
def get_internal_links(bs, include_url):
    include_url = f"{urlparse(include_url).scheme}://{urlparse(include_url).netloc}"
    internal_links = []
    # Find all links that begin with a "/"
    for link in bs.find_all("a", href=re.compile("^(/|.*'+include_url+')")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internal_links:
                if link.attrs["href"].startswith("/"):
                    internal_links.append(include_url+link.attrs["href"])
                else:
                    internal_links.append(link.attrs["href"])

    return internal_links


# Retrieves a list of all external links found on a page
def get_external_links(bs, exclude_url):
    external_links = []
    # Finds all links that start with "http" that do not contain a current url
    for link in bs.find_all("a", href=re.compile('^(https|www)((?!'+exclude_url+').)*$')):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in external_links:
                external_links.append(link.attrs["href"])
    return external_links


def get_random_external_link(starting_page):
    try:
        html = urlopen(starting_page)
        bs = BeautifulSoup(html, "html.parser")
        external_links = get_external_links(bs, urlparse(starting_page).netloc)
        if len(external_links) == 0:
            print("No external links, looking around the site for one")
            domain = f"{urlparse(starting_page).scheme}{urlparse(starting_page).netloc}"
            internal_links = get_internal_links(bs, domain)
            return get_random_external_link(
                internal_links[random.randint(0, len(internal_links) - 1)]
            )
        else:
            return external_links[random.randint(0, len(external_links) - 1)]
    except URLError:
        print("Something bad happened :(")


def follow_external_only(starting_site):
    try:
        external_link = get_random_external_link(starting_site)
        print(f"Random external link is: {external_link}")
        follow_external_only(external_link)
    except URLError:
        print("External link error occurred.")


follow_external_only("https://linkedin.com/")
