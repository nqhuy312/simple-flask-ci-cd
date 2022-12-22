from flask import Flask
from datetime import datetime


app = Flask(__name__)


data = {
    "toys": [
        {
            "name": "car",
            "date": datetime.now()
        },
        {
            "name": "ball",
            "date": datetime.now()
        },
        {
            "name": "doll",
            "date": datetime.now()
        }
    ]
}


@app.route("/")
def index():
    return "Home Page!"


@app.route("/toys")
def get_toys():
    return data


if __name__ == "__main__":
    app.debug = True
    app.run()

