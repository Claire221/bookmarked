import os
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from bookmarked import app, db, mongo
from bookmarked.models import Bookshelves, Users

from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

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
            password=request.form.get("password")
            # password=generate_password_hash(request.form.get("password"),salt_length=1)
        )

        db.session.add(user)
        db.session.commit()

        session["user"] = request.form.get("username").lower()
        flash("Account successfully created")

        return redirect(url_for("profile_page", username=session["user"]))

    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = Users.query.filter(Users.username == request.form.get("username").lower()).all()


        if existing_user:
            if existing_user[0].password == request.form.get("password"):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile_page", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password, Please try again")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password, Please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/profile")
def profile_page():
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.id).all())
    books = mongo.db.books.find()

    return render_template("profile.html", bookshelves=bookshelves, books=books)


@app.route("/add_bookcase", methods=["GET", "POST"])
def add_bookcase():
    if request.method == "POST":
        bookshelf = Bookshelves(
            bookshelf_name=request.form.get("bookshelf_name"),
            bookshelf_description=request.form.get("bookshelf_description"),
            created_by=session["user"]
        )
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for("show_shelves"))

    return render_template("add_bookcase.html")



@app.route("/bookshelves")
def show_shelves():
    user_id = list(Users.query.order_by(Users.id).all())
    bookcase_id = list(Bookshelves.query.order_by(Bookshelves.id).all())
    print(user_id)
    print(bookcase_id)

    # session_user = session["user"]
    # print(session_user)

    bookshelves = list(Bookshelves.query.order_by(Bookshelves.id).all())
    return render_template("bookcases.html", bookshelves=bookshelves)

@app.route("/delete_bookcase/<bookshelf_id>")
def delete_bookcase(bookshelf_id):
    bookcase = Bookshelves.query.get_or_404(bookshelf_id)
    db.session.delete(bookcase)
    db.session.commit()
    return redirect(url_for("profile_page"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": request.form.getlist("genre"),
            "description": request.form.get("book-description"),
            "createdBy": session["user"],
            "bookshelf": request.form.get("bookshelf"),
            "comments": "",
            "created_by": session["user"]
        }

        print(book)
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        
    bookshelves = list(Bookshelves.query.order_by(Bookshelves.id).all())
    return render_template("add_book.html", bookshelves=bookshelves)