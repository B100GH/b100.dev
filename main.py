from flask import Flask
from lib import getkey
from lib import gethome
from lib import getblog
from lib import getresume

app = Flask(__name__)

@app.route("/")
def home():
    home = gethome()
    return home

@app.route("/gpg")
def gpg():
    gpgkey = getkey()
    return gpgkey

@app.route("/blog")
def blog():
    blog = getblog()
    return blog

@app.route("/resume")
def resume():
    resume = getresume()
    return resume


if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0',port='8080')