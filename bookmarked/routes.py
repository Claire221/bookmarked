from flask import render_template
from bookmarked import app, db
from bookmarked.models import Bookshelves,Users

@app.route("/")
def home():
    return render_template("base.html")