import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import jsonify

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
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

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    caf = [column.to_dict() for column in all_cafes]
    return jsonify(cafe=caf)


@app.route("/search")
def get_all_cafe_place():
    place = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location==place))
    all_cafes = result.scalars().all()
    caf = [column.to_dict() for column in all_cafes]
    if caf:
        return jsonify(cafe=caf)
    else:
        return jsonify(error ={
            "Not Found": "Sorry we don't have a cafe at that location"
        })


@app.route("/add_cafe", methods=["POST"])
def add_cafe():
    try:
        reques = request.get_json()
        new_cafe = Cafe(
            name=reques.get("name"),
            map_url=reques.get("map_url"),
            img_url=reques.get("img_url"),
            location=reques.get("loc"),
            has_sockets=bool(reques.get("sockets")),
            has_toilet=bool(reques.get("toilet")),
            has_wifi=bool(reques.get("wifi")),
            can_take_calls=bool(reques.get("calls")),
            seats=reques.get("seats"),
            coffee_price=reques.get("coffee_price"),
        )
        print("name",new_cafe.name)
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    except Exception as e:
        print(f"Error {e}")
        return jsonify(response={"Not success": "Not Successfully added the new cafe."})

@app.route("/update_price/<cafe_id>",methods=["PATCH"])
def update_cafe(cafe_id):
    try:
        cafe_details = db.get_or_404(Cafe, cafe_id)
        reques = request.get_json()
        cafe_details.coffee_price= reques.get("coffe_price")
        db.session.commit()
        print(cafe_details)
        return jsonify(response={"success": "Successfully updated the new cafe coffee price."})
    except Exception as e:
        print(f"Error {e}")
        return jsonify(response={"Not success": "Not Successfully added the new cafe coffe price."})


@app.route("/report_closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "secret":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
# HTTP GET - Read Record

#
# @app.route("/random", methods=["GET"])
# def get_random_cafe():
#     pass
# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
