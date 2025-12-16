from bs4 import BeautifulSoup
from urllib.parse import urlparse

def is_local(path):
    if not path:
        return False
    parsed = urlparse(path)
    return parsed.scheme == "" and not path.startswith("//")

def assetmap(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    assets = []

    for tag in soup.find_all("link", href=True):
        if is_local(tag["href"]):
            assets.append(tag["href"])

    for tag in soup.find_all("script", src=True):
        if is_local(tag["src"]):
            assets.append(tag["src"])

    for tag in soup.find_all("img", src=True):
        if is_local(tag["src"]):
            assets.append(tag["src"])

    for tag in soup.find_all(["video", "audio", "source"], src=True):
        if is_local(tag["src"]):
            assets.append(tag["src"])

    return assets
