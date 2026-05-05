import requests

ALLOWED_DOMAIN = "example.com"

def fetch_code(url):
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.text

def is_safe(url):
    return ALLOWED_DOMAIN in url

def run_code(code):
    # 危険：本来はsandbox必須
    exec(code)

url = "https://www.google.com/"

if is_safe(url):
    code = fetch_code(url)
    run_code(code)
else:
    print("拒否: 許可されていないURL")
