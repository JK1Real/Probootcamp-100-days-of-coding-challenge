from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from menu import db, Books

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the app with the extension
db.init_app(app)

# Ensure database tables are created
with app.app_context():
    db.create_all()


def fetch_books():
    # Reading data from sql
    with app.app_context():
        result = db.session.execute(db.select(Books))
        books = result.scalars().all()
        all_books = [{'id': book.id, 'title': book.title, 'author': book.author, 'rating': book.review} for book in
                     books]
    return all_books


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Delete A Particular Record By PRIMARY KEY
        book_id = id
        with app.app_context():
            book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
            # or book_to_delete = db.get_or_404(Book, book_id)
            db.session.delete(book_to_delete)
            db.session.commit()
            all_books = fetch_books()
            return render_template('index.html', book_shelf=all_books)
    all_books = fetch_books()
    print(all_books, "hello")
    return render_template('index.html', book_shelf=all_books)

@app.route('/delete<int:id>', methods =["GET", "POST"])
def delete_book(id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        if book_to_delete:
            db.session.delete(book_to_delete)
            db.session.commit()
            return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        Book_name = request.form.get('book_name')
        Book_author = request.form.get('book_author')
        Book_rating = request.form.get('rating')
        """ Create a table and adding values"""
        with app.app_context():
            books = Books(title=Book_name, author=Book_author, review=Book_rating)
            db.session.add(books)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/update_rating<int:id>')
def update_rating(id):
    all_books = fetch_books()
    return render_template("updaterating.html", book_data=all_books[id - 1])


@app.route('/updating_the_rating', methods=['GET', 'POST'])
def updated():
    # Update A Particular Record By Query
    with app.app_context():
        book_name = request.args.get('book_name')
        book_to_update = db.session.execute(db.select(Books).where(Books.title == book_name)).scalar()
        book_to_update.review = request.form.get('rating')
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
