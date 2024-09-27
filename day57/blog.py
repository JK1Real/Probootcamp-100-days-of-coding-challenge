from flask import Flask, render_template
import requests

in_url="https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(url=in_url)
print(response.status_code)
try:
    blogs = response.json()
    print(blogs)
except Exception as e:
    print(f"error {e}")

app=Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/blogs")
def blog():
    return render_template("blog.html", posts=blogs)

if __name__=="__main__":
    app.run(debug=True)