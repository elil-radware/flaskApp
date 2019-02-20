# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import json
from app import db
# import etcd3

# etcd = etcd3.client(host='localhost', port=35001)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(128))
    isbn = db.Column(db.Integer)

    def json(self):
        return {
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn
        }

    def add_book(_name, _price, _isbn):
        new_book = Book(name=_name, price=_price, isbn=_isbn)
        db.session.add(new_book)
        db.session.commit()

    def get_all_books():
        return [Book.json(book) for book in Book.query.all()]

    def get_book(_isbn):
        return Book.json(Book.query.filter_by(isbn=_isbn).first())

    def delete_book(_isbn):
        is_successful = Book.query.filter_by(isbn=_isbn).delete()
        db.session.commit()
        return bool(is_successful)

    def update_book_name(_isbn, _name):
        to_update = Book.query.filter_by(isbn=_isbn).first()
        to_update.name = _name
        db.session.commit()

    def update_book_price(_isbn, _price):
        to_update = Book.query.filter_by(isbn=_isbn).first()
        to_update.price = _price
        db.session.commit()

    def replace_book(_isbn, _name, _price):
        to_update = Book.get_book(_isbn)
        to_update.price = _price
        to_update.name = _name
        db.session.commit()

    def __repr__(self):
        book_obj = {
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn
        }
        return json.dumps(book_obj)