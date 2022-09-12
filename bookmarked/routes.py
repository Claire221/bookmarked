from flask import render_template, request, redirect, url_for
from bookmarked import app, db
from bookmarked.models import Bookshelves, Users


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/profile")
def profile_page():
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.id).all())
    return render_template("profile.html", bookshelves=bookshelves)


@app.route("/add_bookcase", methods=["GET", "POST"])
def add_bookcase():
    if request.method == "POST":
        bookshelf = Bookshelves(
            bookshelf_name=request.form.get("bookshelf_name"),
            bookshelf_description=request.form.get("bookshelf_description")
        )
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for("profile_page"))

    return render_template("add_bookcase.html")

