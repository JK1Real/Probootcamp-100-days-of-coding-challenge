from flask import Flask, render_template, request




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    result = request.form
    return render_template('login.html', result=result)

if __name__=="__main__":
    app.run(debug=True)