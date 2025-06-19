from flask import Flask, render_template \
    , send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='assets')
# app.config.from_object("config")

@app.route("/")
@app.route("/home")
def Home():
    return render_template("home/index.html")

@app.route("/document")
def Document():
    return render_template("document/index.html")

@app.route("/replaypanel")
def ReplayPanel():
    return render_template("replaypanel/index.html")

@app.route("/about")
def About():
    return render_template("about/index.html")

@app.route("/lgrg")
def LoginRegister():
    return render_template("loginregister/index.html")

# for this singal debug
if __name__ == "__main__":
    app.run(debug=True, port=8080)