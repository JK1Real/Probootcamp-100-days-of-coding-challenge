from flask import Flask, render_template
import requests

api_url = "https://api.npoint.io/4aeaaa73be24cbaff4d6"

response = requests.get(api_url)

print(response.status_code)

posts = response.json()

#print(reply)


app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", post=posts[post_id-1])

if __name__=="__main__":
    app.run(debug=True)