from flask import Flask, request, jsonify
import requests
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAIN = "example.com"

def is_safe(url):
    parsed = urlparse(url)
    return parsed.netloc == ALLOWED_DOMAIN

@app.route("/crawl")
def crawl():
    url = request.args.get("url")

    if not url:
        return "no url"

    if not is_safe(url):
        return "拒否: 許可されていないURL"

    r = requests.get(url, timeout=5)
    return r.text

if __name__ == "__main__":
    app.run(debug=True)
