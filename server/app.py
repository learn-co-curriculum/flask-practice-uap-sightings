#!/usr/bin/env python3

from flask import Flask, abort, make_response, request
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

api = Api(app)

# Initialize the db instance
db.init_app(app)
# Define routes and views


@app.route("/")
def home():
    return make_response("The UAPID welcome our new extraterrestrial overlords!", 200)


@app.route("/sightings/location/<string:location>")
def show(location):
    s_list = Sighting.query.filter(Sighting.location == location).all()
    if len(s_list) == 0:
        return make_response("There are no sightings at that location", 404)
    return make_response([s.to_dict() for s in s_list], 200)


class Sightings(Resource):
    def get(self):
        sightings = [s.to_dict() for s in Sighting.query.all()]
        return make_response(sightings, 200)


class SightingById(Resource):

    def get(self, id):
        s = db.session.get(Sighting, id)
        if not s:
            abort(404)
        return make_response(s.to_dict(), 200)


api.add_resource(Sightings, "/sightings")
api.add_resource(SightingById, "/sightings/<int:id>")


@app.before_request
def total_sightings():
    print(f"Total sightings: {len(Sighting.query.all())}")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
