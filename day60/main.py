from flask import Flask, render_template
import requests
import flask
from sending_emial import *

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")
    

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["POST","GET"])
def contact():
    if flask.request.method=="POST":
        result = flask.request.form

        send_emial(result=result)

        return render_template('contact.html',s='SUESSFULY SENT THE MESSAGE')
    return render_template("contact.html",s='Contact Me')



if __name__ == "__main__":
    app.run(debug=True, port=5001)
