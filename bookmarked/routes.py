import random
from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from bookmarked import app, db, mongo
from bookmarked.models import Bookshelves, Users


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        if existing_user:
            if existing_user[0].password == request.form.get("password"):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(
                    url_for("profile_page", username=session["user"]))

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
        existing_user = Users.query.filter(
            Users.username == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists. Please chose another")
            return redirect(url_for("register"))

        user = Users(
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

    user_bookshelves = Bookshelves.query.filter(
        Bookshelves.created_by == session_user).all()
    # bookshelves = list(
    #     Bookshelves.query.order_by(Bookshelves.bookshelf_name).all())

    # for bookshelf in user_bookshelves:
    #     print(user_bookshelves)

    users_books = []
    bookshelf_names = []
    books = mongo.db.books.find()

    if books:
        for b in books:
            if b["createdBy"] == session_user:
                users_books.append(b)

    return render_template(
        "profile.html", bookshelves=user_bookshelves,
        books=users_books, user=session_user)


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
    all_bookshelves = Bookshelves.query.filter(
        Bookshelves.created_by == session_user).all()

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
        genres = request.form.get("genre")
        genre = genres.split(", ")
        book = {
            "title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": genre,
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
    all_bookshelves = Bookshelves.query.filter(
        Bookshelves.created_by == session_user).all()
    return render_template("add_book.html", bookshelves=all_bookshelves)


@app.route("/delete-book/<book_id>")
def delete_book(book_id):
    """
    Function to delete the book
    """
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})

    return redirect(url_for("profile_page"))


@app.route("/books/<bookcase_id>")
def sort_books(bookcase_id):
    """
    Function to sort books into bookcases
    """
    session_user = session["user"]
    bookshelf = Bookshelves.query.filter(
        Bookshelves.id == bookcase_id)


    books_list = list(mongo.db.books.find())
    users_books = []
    books_title = []

    for b in books_list:
        if ["createdBy"] == session_user:
            users_books.append(b)

    for books in books_list:
        if books["bookshelf"] == bookcase_id:
            books_title.append(books)


    return render_template(
        "books.html", bookshelves=bookshelf,
        books=books_title)


@app.route("/test/<book_id>")
def display_books(book_id):
    """
    Function to display books
    """
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("display_book.html", book=book)


@app.route("/edit-book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    """
    Function to edit a book
    """
    if request.method == "POST":
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        genres = request.form.get("genre")
        genre = genres.split(", ")
        comments = []
        submit = {
            "title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "genre": genre,
            "description": request.form.get("book-description"),
            "createdBy": session["user"],
            "bookshelf": request.form.get("bookshelf"),
            "comments": comments,
            "created_by": session["user"],
            "colour": request.form.get("colour")
        }

        mongo.db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": submit}
        )
        flash("Book Successfully Updated")
    
    session_user = session["user"]
    bookshelves = Bookshelves.query.filter(
        Bookshelves.created_by == session_user).all()
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    book_genres = " ".join(str(book) for book in book["genre"])

    return render_template(
        "edit_book.html", book=book, bookshelves=bookshelves, current_genres=book_genres)


@app.route("/comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    """
    Function to add comments to books
    """
    if request.method == "POST":
        comments = request.form.get("book_comment")
        mongo.db.books.find_one({"_id": ObjectId(book_id)})

        # book_comment = {
        #     "comments": comments
        # }

        mongo.db.books.update_one(
            {'_id': ObjectId(book_id)},
            {"$push": {"comments": comments}}
        )
        flash("Comment Successfully Added")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("display_book.html", book=book)


@app.route("/comment/<book_id>", methods=["GET", "POST"])
def delete_comment(book_id):
    mongo.db.books.update_one(
        {'_id': ObjectId(book_id)},
        {"$pull": {"comments": comment}}
    )
    print(comment)
    return render_template("display_book.html", book=book)


@app.route("/generate-book", methods=["GET", "POST"])
def generate_book():
    """
    Function to generate a book
    """
    session_user = session["user"]
    bookshelves = Bookshelves.query.filter(
        Bookshelves.created_by == session_user).all()

    books = list(mongo.db.books.find())
    authors = []
    genres = []
    genre_list = []
    x = []
    for book in books:
        if book["createdBy"] == session_user:
            if book["author"] not in authors:
                authors.append(book["author"])

    for book in books:
        if book["createdBy"] == session_user:
            if book["genre"] not in genres:
                genres.extend(book["genre"])

    for genre in genres:
        if genre.capitalize() not in genre_list:
            genre_list.append(genre.capitalize())

    return render_template(
        "generate_book.html", bookshelves=bookshelves,
        authors=authors, books=books, genres=genre_list)


@app.route("/generated-bookshelf", methods=["GET", "POST"])
def bookshelf_book():
    """
    Function to generate a book from Bookshelves
    """
    if request.method == "POST":
        bookshelf_id = request.form.get("bookshelf")
        chosen_bookshelf = Bookshelves.query.filter(
            Bookshelves.id == bookshelf_id)

        books = list(mongo.db.books.find())
        bookshelf_books = []

        for book in books:
            if book["bookshelf"] == bookshelf_id:
                bookshelf_books.append(book)

        if bookshelf_books:
            random_number = random.randint(0, len(bookshelf_books) - 1)
            chosen_book = bookshelf_books[random_number]
        else:
            chosen_book = None
    return render_template(
        "generated_book.html", bookshelf=chosen_bookshelf,
        book=chosen_book)


@app.route("/generated-author", methods=["GET", "POST"])
def author_book():
    """
    Function to generate a book from all Authors
    """
    if request.method == "POST":
        author = request.form.get("author")

        books = list(mongo.db.books.find())
        author_books = []

        for book in books:
            if book["author"] == author:
                author_books.append(book)

        if len(author_books) > 0:
            random_number = random.randint(0, len(author_books) - 1)
            chosen_book = author_books[random_number]
        elif len(author_books) == 0:
            chosen_book = author_books
        else:
            chosen_book = None

    return render_template(
        "generated_book.html", authors=author, book=chosen_book)


# Function to generate a book from all Genres

@app.route("/generated-tag", methods=["GET", "POST"])
def tag_book():
    """
    Function to generate a book from all Authors
    """
    if request.method == "POST":
        tag = request.form.get("genre").lower()
        chosen_tag = tag.capitalize()
        books = list(mongo.db.books.find())
        genre_books = []

        for b in books:
            if tag in b["genre"]:
                genre_books.append(b)

        if len(genre_books) > 0:
            random_number = random.randint(0, len(genre_books) - 1)
            chosen_book = genre_books[random_number]
        elif len(genre_books) == 0:
            chosen_book = genre_books
        else:
            chosen_book = None

    return render_template(
        "generated_book.html", book=chosen_book, tag=chosen_tag)

@app.route("/generated-books", methods=["GET", "POST"])
def random_book():
    """
    Function to generate a book from all Books
    """
    if request.method == "POST":
        session_user = session["user"]
        books = list(mongo.db.books.find())
        chosen_book = None

        if books:
            for book in books:
                if book["createdBy"] == session_user:
                    random_number = random.randint(0, len(books) - 1)
                    chosen_book = books[random_number]
        else:
            chosen_book = None

    return render_template("generated_book.html", book=chosen_book)


# Function to search for books
@app.route("/search-book", methods=["GET", "POST"])
def search_book():
    """
    Function to search books
    """
    if request.method == "POST":
        session_user = session["user"]
        search = request.form.get("search")

        all_books = list(mongo.db.books.find())
        users_books = []
        searched_books = []

        for book in all_books:
            if book["createdBy"] == session_user:
                # print(book["title"])
                if search in book["title"]:
                    print(book["title"])

        # for book in users_books:
        #     if any(search in book for s in search):
        #         searched_books.append(book)
        for book in users_books:
        #     print("First Test")
            print(book)
            print(type(book))
        #     print("Second Test")
        #     print(search)
            if search in book:
                searched_books.append(book)


    return render_template("search-page.html", searched_books=searched_books, search=search)