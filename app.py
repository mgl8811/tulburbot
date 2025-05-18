
from flask import Flask, render_template, request
import pandas as pd
import requests

app = Flask(__name__)

# Google Sheet CSV URL (хуулж өөрийнхөө CSV URL-г хийнэ)
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTzIEULQG9QR9IYQGExNw6VEyjuX_tOYEGbOxLw3TnR9qYxe1HtbfCMzspQOmSvG7kSfOdGZf2QnhAf/pub?gid=0&single=true&output=csv"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        phone = request.form["phone"]
        df = pd.read_csv(CSV_URL)
        match = df[df["Дугаар"] == phone]
        if not match.empty:
            tulbur = match.iloc[0]["Үлдэгдэл"]
            result = f"{phone} дугаарын үлдэгдэл: {tulbur}₮"
        else:
            result = f"{phone} дугаар олдсонгүй!"
    return render_template("index.html", result=result)
