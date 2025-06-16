from flask import Flask, render_template \
    , send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static")
# app.config.from_object("config")

@app.route("/")
def Gateway():
    return send_from_directory(app.static_folder, 'index.html')
    # return render_template("debug.html", site_name="Gateway")

@app.route("/home")
def Home():
    return render_template("debug.html", site_name="Home page")

@app.route("/document")
def TruthLadder():
    return render_template("debug.html", site_name="Truth Ladder")

@app.route("/replaypanel")
def Chatting():
    return render_template("debug.html", site_name="Chatting")

@app.route("/about")
def About():
    return render_template("debug.html", site_name="About")


# for this singal debug
if __name__ == "__main__":
    app.run(debug=True)