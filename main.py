import flask
from lib import getkey
from lib import gethome

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    home = gethome()
    return home

@app.route("/gpg")
def gpg():
    gpgkey = getkey()
    return gpgkey

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port='8080')