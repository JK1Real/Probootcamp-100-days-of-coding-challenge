from flask import Flask, render_template
import requests
from post import Post

url="https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(url=url)
posts = response.json()

post_class = Post(posts=posts)

titles = [post_class.get_title(id=1), post_class.get_title(id=2)]

subtitles= [post_class.get_subtitle(id=1), post_class.get_subtitle(id=2)]

bodies = [post_class.get_body(id=1), post_class.get_body(id=2)]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", titles=titles, subtitles=subtitles)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = [post_class.get_body(id=1), post_class.get_body(id=2)]
    return render_template('post.html', titles=titles, subtitles=subtitles,posts=requested_post, index=index)


if __name__ == "__main__":
    app.run(debug=True)
