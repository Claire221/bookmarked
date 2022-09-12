from flask import render_template, request, redirect, url_for
from bookmarked import app, db
from bookmarked.models import Bookshelves, Users


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/profile")
def profile_page():
    return render_template("profile.html")


@app.route("/add_bookcase", methods=["GET", "POST"])
def add_bookcase():
    if request.method == "POST":
        bookshelves = Bookshelves(bookshelf_name=request.form.get("bookshelf_name"))
        db.session.add(bookshelves)
        db.session.commit()
        return redirect(url_for("add_bookcase"))
    return render_template("add_bookcase.html")