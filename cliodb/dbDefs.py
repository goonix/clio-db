from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

Base = db.Model


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# Artist definition
class Artist(Base):
    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Artist %r>' % self.name

# Album definition
class Album(Base):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    #artist = db.relationship(Artist, backref=db.backref('albums', uselist=True))
    artist = db.relationship(Artist, backref=db.backref('albums', lazy='dynamic'))

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def __repr__(self):
        return '<Album %r>' % self.name

# Track definition
class Track(Base):
    __tablename__ = 'track'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    album = db.relationship(Album, backref=db.backref('tracks', uselist=True))

    def __init__(self, name, rating, album):
        self.name = name
        self.rating = rating
        self.album = album

    def __repr__(self):
        return '<Track %r>' % self.name
