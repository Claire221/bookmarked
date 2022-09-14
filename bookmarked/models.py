from bookmarked import db


class Bookshelves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookshelf_name = db.Column(db.String(25), unique=True, nullable=False)
    bookshelf_description = db.Column(db.Text, nullable=False)
    created_by = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.created_by 


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), unique=True, nullable=False)
    password = db.Column(db.String(8), unique=True, nullable=False)

    def __repr__(self):
        return self.username
