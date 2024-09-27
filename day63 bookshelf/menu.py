# import sqlite3
#
# db = sqlite3.connect("books-colllection.db")
#
# cursor = db.cursor()
#
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books values(1, 'Harry potter', 'J.K Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    review: Mapped[str]





# # Reading data fro sql
# with app.app_context():
#     result = db.session.execute(db.select(Books))
#     all_books = result.scalars().all()
#     print(all_books)
#
#     for book in all_books:
#         print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Review: {book.review}')
#
# # Read A Particular Record By Query
# with app.app_context():
#     book = db.session.execute(db.select(Books).where(Books.title == "Harry potter")).scalar()
#
# # Update A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# # Update A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# #Delete A Particular Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()