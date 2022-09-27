import os
import random

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


@app.route("/logout")
def logout():
    flash("You successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/profile")
def profile_page():
    session_user = session["user"]

    user_bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()
    # bookshelves = list(Bookshelves.query.order_by(Bookshelves.bookshelf_name).all())

    # for bookshelf in user_bookshelves:
    #     print(user_bookshelves)
        
    users_books = []
    bookshelf_names = []

    books = mongo.db.books.find()
            
    for b in books:
        if b["createdBy"] == session_user:
            users_books.append(b)

    return render_template("profile.html", bookshelves=user_bookshelves, books=users_books, user=session_user)


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

    return render_template("add_bookshelf.html")

@app.route("/bookshelves")
def show_shelves():
    session_user = session["user"]
    all_bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()


    return render_template("bookshelves.html", bookshelves=all_bookshelves)

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
            "comments": [None],
            "created_by": session["user"],
            "colour": request.form.get("colour")
        }

        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        
    session_user = session["user"]
    all_bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()
    return render_template("add_book.html", bookshelves=all_bookshelves)

#Function to delete book
@app.route("/delete-book/<book_id>")
def delete_book(book_id):
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})

    return redirect(url_for("profile_page"))


# Function to sort books into bookcases
@app.route("/books/<bookcase_id>")
def sort_books(bookcase_id):
    session_user = session["user"]
    bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()

    books_list = list(mongo.db.books.find())
    users_books = []
    books_title = []
     
    for b in books_list:
        if ["createdBy"] == session_user:
            users_books.append(b)

    for books in books_list: 
        if books["bookshelf"] == bookcase_id:
            books_title.append(books)

    return render_template("books.html", bookshelves=bookshelves, books=books_title)



# Function to display books 
@app.route("/test/<book_id>")
def display_books(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("display_book.html", book=book)


#Function to edit a book
@app.route("/edit-book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        genres = request.form.getlist("genre")
        genre_list = []
        comments = []
        submit = {
            "title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": genre_list,
            "description": request.form.get("book-description"),
            "createdBy": session["user"],
            "bookshelf": request.form.get("bookshelf"),
            "comments": comments,
            "created_by": session["user"],
            "colour": request.form.get("colour")
        }
        
        for genre in genres:
            genre_list.append(genre)
            
        mongo.db.books.update_one({"_id": ObjectId(book_id)},  {"$set": submit})
        flash("Book Successfully Updated")

    session_user = session["user"]
    bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("edit_book.html", book=book, bookshelves=bookshelves)


# Function to add comments to books
@app.route("/comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    if request.method == "POST":
        comments = request.form.get("book_comment")
        mongo.db.books.find_one({"_id": ObjectId(book_id)})

        # book_comment = {
        #     "comments": comments
        # }

        mongo.db.books.update_one({ '_id': ObjectId(book_id) },{ "$push": {"comments": comments} })
        flash("Comment Successfully Added")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("display_book.html", book=book)


@app.route("/comment/<book_id>", methods=["GET", "POST"])
def delete_comment(book_id):
    mongo.db.books.update_one({ '_id': ObjectId(book_id) },{ "$pull": {"comments": comment} })

    return render_template("display_book.html", book=book)

# Function to generate a book
@app.route("/generate-book", methods=["GET", "POST"])
def generate_book():
    session_user = session["user"]
    bookshelves = Bookshelves.query.filter(Bookshelves.created_by == session_user).all()

    books = list(mongo.db.books.find())
    authors = []
    genres = []
    genre_list =[]
    
    for book in books:
        if book["createdBy"] == session_user:
            if book["author"] not in authors:
                authors.append(book["author"])

    for book in books:
        if book["createdBy"] == session_user:
            if book["genre"] not in genres:
                genres.append(book["genre"])

    # for g in genres:
    #     print(g)


    return render_template("generate_book.html", bookshelves=bookshelves, authors=authors, books=books, genres=genres)



# Function to generate a book from Bookshelves 
@app.route("/generated-bookshelf", methods=["GET", "POST"])
def bookshelf_book():
    if request.method == "POST":
        bookshelf_id = request.form.get("bookshelf")
        chosen_bookshelf = Bookshelves.query.filter(Bookshelves.id == bookshelf_id)
        # chosen_bookshelf = Bookshelves.query.filter(Bookshelves.id == request.form.get("bookshelf"))

        books = list(mongo.db.books.find())
        bookshelf_books = []

        for book in books:
            if book["bookshelf"] == bookshelf_id:
                bookshelf_books.append(book)

        if bookshelf_books: 
            random_number = random.randint(0, len(bookshelf_books) -1)
            chosen_book = bookshelf_books[random_number]
        else:
            chosen_book = None
    return render_template("generated_book.html", bookshelf=chosen_bookshelf, book=chosen_book)


# Function to generate a book from all Authors
@app.route("/generated-author", methods=["GET", "POST"])
def author_book():
    if request.method == "POST":
        author = request.form.get("author")

        books = list(mongo.db.books.find())
        author_books = []

        for book in books:
            if book["author"] == author :
                author_books.append(book)

        if len(author_books) > 0: 
            random_number = random.randint(0, len(author_books) -1)
            chosen_book = author_books[random_number]
        elif len(author_books) == 0:
            chosen_book = author_books
        else:
            chosen_book = None
        
        print("Test")
        print(author)
        # print(author_books)
        # print(chosen_book)
    return render_template("generated_book.html", authors=author, book=chosen_book)


# Function to generate a book from all Genres

# Function to generate a book from all Books
@app.route("/generated-books", methods=["GET", "POST"])
def random_book():
    if request.method == "POST":
        session_user = session["user"]
        books = list(mongo.db.books.find())
        chosen_book = None

        if books: 
            for book in books:
                if book["createdBy"] == session_user:
                    random_number = random.randint(0, len(books) -1)
                    chosen_book = books[random_number]
        else:
            chosen_book = None

    return render_template("generated_book.html", book=chosen_book)


# Function to search for books