from flask import Flask, render_template \
    , send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object("config")

@app.route("/")
@app.route("/home")
def Home():
    return render_template('index.html')

@app.route("/document")
def Document():
    return render_template("debug.html", site_name="Document")

@app.route("/replaypanel")
def ReplayPanel():
    return render_template("debug.html", site_name="ReplayPanel")

@app.route("/about")
def About():
    return render_template("debug.html", site_name="About")


# for this singal debug
if __name__ == "__main__":
    app.run(debug=True, port=8080)