import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import jsonify

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Optional, but recommended

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

# Cafe TABLE Configuration
class Cafe(db.Model):
    __tablename__ = "cafe"  # Explicitly specify the table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
#
# Accessing and querying the existing database
with app.app_context():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    for cafe in all_cafes:
        print(cafe.id, cafe.name, cafe.map_url, cafe.img_url, cafe.location, cafe.seats,
              cafe.has_toilet, cafe.has_wifi, cafe.has_sockets, cafe.can_take_calls, cafe.coffee_price)

# @app.route('/')
# def get_current_user():
#  #   with app.app_context():
#         result = db.session.execute(db.select(Cafe))
#         all_cafes = result.scalars().all()
#         random_cafe = random.choice(all_cafes)
#         return jsonify(
#             id=random_cafe.id,
#             name=random_cafe.name,
#             map_url=random_cafe.map_url,
#             img_url=random_cafe.img_url,
#             location=random_cafe.location,
#             seats=random_cafe.seats,
#             has_toilet=random_cafe.has_toilet,
#             has_wifi=random_cafe.has_wifi,
#             has_sockets=random_cafe.has_sockets,
#             can_take_calls=random_cafe.can_take_calls,
#             coffee_price=random_cafe.coffee_price
#         )
#
# if __name__=="__main__":
#     app.run(debug=True)
