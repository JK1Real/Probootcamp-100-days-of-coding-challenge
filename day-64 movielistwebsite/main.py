from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
import requests
from for_api import moviesfromapi, movie_details

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


# CREATE TABLE


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[str]
    description: Mapped[str]
    rating: Mapped[int]
    ranking: Mapped[int]
    review: Mapped[str]
    img_url: Mapped[str]


# Making a function to easily add row to the table when ever we want


def add_movie_to_table(title, year, description, rating, ranking, review, img_url):
    with app.app_context():
        db.create_all()

        new_movie = Movie(
            title=title,
            year=year,
            description=description,
            rating=rating,
            ranking=ranking,
            review=review,
            img_url=img_url
        )
        db.session.add(new_movie)
        db.session.commit()


# Entering first movie to table


# add_movie_to_table(
#             title="Phone Booth",
#             year=2002,
#             description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#             rating=7.3,
#             ranking=10,
#             review="My favourite character was the caller.",
#             img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#
# )

# Entering second movie to table


# add_movie_to_table(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#
# )

def get_all_movie_list_from_database():
    with app.app_context():
        movies = db.session.execute(db.select(Movie))
        movie_list = movies.scalars().all()
        movies_list = [{'id': movie.id, 'title': movie.title, 'year': movie.year, 'description': movie.description,
                        'rating': movie.rating, 'ranking': movie.ranking, 'review': movie.review,
                        'img_url': movie.img_url} for movie in movie_list]
    return movies_list


@app.route("/")
def home():
    movies = get_all_movie_list_from_database()
    return render_template("index.html", movies=movies)


class MyForm(FlaskForm):
    new_rating = StringField('Your rating out of 10 eg 7.5', validators=[DataRequired()])
    new_review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField("Done")

@app.route("/edit<int:id>", methods=["GET", "POST"])
def edit(id):
    movie_to_update = Movie.query.get_or_404(id)
    form = MyForm()
    if form.validate_on_submit():
        movie_to_update.rating = form.new_rating.data
        movie_to_update.review = form.new_review.data

        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", id=id, form=form)


@app.route("/delete<int:id>")
def delete(id):
    movie_to_delete = Movie.query.get_or_404(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


class Movie_title(FlaskForm):
    movie_name = StringField('Movie', [validators.DataRequired()])
    submit = SubmitField("Add")


@app.route("/add_movie_title", methods=["GET", "POST"])
def add():
    movie = Movie_title()
    if movie.validate_on_submit():
        movie_name = movie.movie_name.data
        print(movie_name)
        movie_list = moviesfromapi(movie_name)
        return render_template('select.html',movies=movie_list)
    return render_template('add.html', form=movie)

@app.route("/addingmovie<int:id>")
def towardshome(id):
    movie_detail = movie_details(id)
    add_movie_to_table(
                title=movie_detail['original_title'],
                year=movie_detail['release_date'],
                description=movie_detail['overview'],
                rating=movie_detail['vote_average'],
                ranking=10,
                review="My favourite character was the caller.",
                img_url=f"https://image.tmdb.org/t/p/w500{movie_detail['backdrop_path']}"

    )
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
