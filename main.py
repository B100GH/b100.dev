import flask
from lib import getkey

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    
    return 

@app.route("/gpg")
def gpg():
    gpgkey = getkey()
    return gpgkey

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port='8080')