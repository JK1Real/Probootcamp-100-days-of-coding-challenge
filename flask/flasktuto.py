from flask import Flask
from selfmade_decorators import *

app = Flask(__name__)

print(__name__)

@app.route("/")
def hello_world():
    return 'Hello, World'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "bye"

@app.route("/<name>")
def greet(name):
    return f"hello {name} "

if __name__=="__main__":
    app.run(debug=True)


