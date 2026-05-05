from flask import Flask, request
import requests
from urllib.parse import urlparse

app = Flask(__name__)

def is_safe(url):
    return urlparse(url).scheme in ["http", "https"]

@app.route("/crawl")
def crawl():
    url = request.args.get("url")

    if not url or not is_safe(url):
        return "invalid url"

    r = requests.get(url, timeout=5)
    return r.text  # ← これが「閲覧データ」
    
if __name__ == "__main__":
    app.run(debug=True)
