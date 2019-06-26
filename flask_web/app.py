from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "home page"


@app.route("/index")
def index():
    return "index page"
