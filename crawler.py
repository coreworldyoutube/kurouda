import requests

def crawl(url):
    res = requests.get(url)
    return res.text[:500]
