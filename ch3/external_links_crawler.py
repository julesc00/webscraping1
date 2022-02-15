import re
import datetime
import random
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup

ALL_EXT_LINKS = set()
ALL_INT_LINKS = set()


def get_all_external_links(site_url: str):
    html = urlopen(site_url)
    domain = f"{urlparse(site_url).scheme}://{urlparse(site_url).netloc}"
    bs = BeautifulSoup(html, "html.parser")
    internal_links = get
