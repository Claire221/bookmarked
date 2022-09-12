from bookmarked import db

class Bookshelves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookshelf_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
      return self.bookshelf_name 

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)

