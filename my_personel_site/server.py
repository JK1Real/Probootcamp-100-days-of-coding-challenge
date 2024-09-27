from flask import Flask, render_template


app=Flask(__name__)

# @app.route("/")
# def site():
#     return render_template('jerom.html')

# @app.route("/hobbies")
# def hobbies():
#     return render_template('hobbies.html')

@app.route("/")
def site():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)