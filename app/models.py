from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
class Bookshelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    title = db.Column(db.String(60), unique=True, nullable=False)
    author = db.Column(db.String(60), unique=True, nullable=False)
    year = db.Column(db.String(60), unique=True, nullable=False)
    pages = db.Column(db.String(60), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __init__(self, name, title, author, year, pages, owner_id):
        self.name = name
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.owner_id = owner_id
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
