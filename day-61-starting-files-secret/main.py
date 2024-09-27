from flask import Flask, render_template

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, InputRequired

from flask_bootstrap import Bootstrap5


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')

    def validate_email(self, email):
        if '@' not in email.data:
            raise ValidationError('Email must contain "@"')


'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows ty pe:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the secret key
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app) # initialise bootstrap-flask

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
