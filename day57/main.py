import requests
from flask import Flask, render_template

url="https://api.agify.io"
url2="https://api.genderize.io"

in_url="https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(url=in_url)
print(response.status_code)
try:
    blogs = response.json()
    print(blogs)
except Exception as e:
    print(f"error {e}")

headers={'Authorizati':'630ad9a0a8b1e7c28ec2e0360658a206'}
parameters={}

app=Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/<name>")
def guess_age(name):
    parameters["name"] =name
    response_for_age = requests.get(url=url,params=parameters, headers=headers)
    response_for_gender = requests.get(url=url2,params=parameters, headers=headers)
    age_details = response_for_age.json()
    gender_details = response_for_gender.json()
    print(age_details)
    print(gender_details)
    name = age_details["name"].title()
    print(name)
    return render_template("guess_age.html", name=name, gender=gender_details["gender"], age=age_details["age"])



@app.route("/blogs")
def blog():
    return render_template("blog.html", posts=blogs)


print(__name__)
if __name__=="__main__":
    app.run(debug=True)







# from flask import Flask, render_template
# from random import randint
# from datetime import date

# app = Flask(__name__)

# current_date = date.today().year
# # current_date = current_date.split("-")[0]
# print(current_date)
# @app.route('/')
# def home():
#     random_number = randint(1,16)
#     return render_template("index.html", num=random_number, today = current_date)


# if __name__ == "__main__":
#     app.run(debug=True)


