from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from bookmarked import app, db
from bookmarked.models import Bookshelves, Users


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = Users.query.filter(Users.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists. Please chose another")
            return redirect(url_for("register"))

        user = Users (
            username=request.form.get("username"),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        session["user"] = request.form.get("username").lower()
        flash("Account successfully created")

        return redirect(url_for("profile_page", username=session["user"]))

    return render_template("register.html")






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
