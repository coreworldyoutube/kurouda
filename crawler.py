from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/view")
def view():
    url = request.args.get("url")
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return r.text
