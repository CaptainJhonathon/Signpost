from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
def Gateway():
    return render_template("debug.html", site_name="Gateway")

@app.route("/home")
def Home():
    return render_template("debug.html", site_name="Home page")

@app.route("/truthladder")
def TruthLadder():
    return render_template("debug.html", site_name="Truth Ladder")

@app.route("/chatting")
def Chatting():
    return render_template("debug.html", site_name="Chatting")

@app.route("/about")
def About():
    return render_template("debug.html", site_name="About")


# for this singal debug
if __name__ == "__main__":
    app.run(debug=True)