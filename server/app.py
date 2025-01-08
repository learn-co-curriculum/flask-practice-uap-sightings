#!/usr/bin/env python3

from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

# import model and db instance
from models import Sighting, db

# Initialize Flask app
app = Flask(__name__)

# configure the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize the db instance
db.init_app(app)
# Define routes and views


@app.route("/")
def home():
    return make_response("The UAPID welcome our new extraterrestrial overlords!", 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
