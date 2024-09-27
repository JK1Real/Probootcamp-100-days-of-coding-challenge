from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name   ', validators=[DataRequired()])
    Location_URL = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    openning_time = StringField('Openning time eg 8AM', validators=[DataRequired()])
    clossing_time = StringField('Openning time eg 4:30PM', validators=[DataRequired()])
    Coffe_rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕'])
    wifi_rating = SelectField('Wifi strength rating', choices=['💪', '✘', '💪💪💪', '💪💪💪'])
    power = SelectField('Power rating', choices=['🔌', '🔌🔌', '🔌🔌🔌'])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        with open(file='cafe-data.csv', mode='a', newline='\n', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                [form.cafe.data,
                 form.Location_URL.data,
                 form.openning_time.data,
                 form.clossing_time.data,
                 form.Coffe_rating.data,
                 form.wifi_rating.data,
                 form.power.data])

        return redirect('/cafes')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
