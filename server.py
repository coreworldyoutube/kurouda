from flask import Flask
from crawler import crawl

app = Flask(__name__)

@app.route("/crawl")
def run():
    return crawl("https://example.com")

app.run()
