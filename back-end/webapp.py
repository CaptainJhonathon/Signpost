from flask import Flask, render_template \
    , send_from_directory, url_for
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='assets')
# app.config.from_object("config")

# # for Nginx reverse proxy
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
# # 

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

# for debug
if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1", ssl_context=("./back-end/tcert.pem","./back-end/tkey.pem"))

# to run uWSGI:
# ./uwsgi --http 127.0.0.1:8080 --master -p 2 -w webapp:app