from flask import Flask
import requests

app = Flask(__name__)

@app.route("/crawl")
def crawl():
    url = "https://www.google.com/"
    res = requests.get(url)
    return res.text[:1000]  # 先頭だけ表示

app.run()
