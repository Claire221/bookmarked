from flask import render_template, request, redirect, url_for, flash, session
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


@app.route("/delete_bookcase/<bookshelf_id>")
def delete_bookcase(bookshelf_id):
    bookcase = Bookshelves.query.get_or_404(bookshelf_id)
    db.session.delete(bookcase)
    db.session.commit()
    return redirect(url_for("profile_page"))
