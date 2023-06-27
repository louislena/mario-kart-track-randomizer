
from flask import request
from flask_cors import CORS, cross_origin
from track_randomizer.code_track_randomizer import track_randomizer, reset_tracks

from player_setup_randomizer.code_character_vehicle_wheels_gliders import player_setup

from item_randomizer.code_item_randomizer_code import item_randomizer

from full_randomizer import full_randomizer

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class RandomTracks(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        track_amount = request.args.get('track_amount')
        if track_amount:
            return track_randomizer(int(track_amount))
        return track_randomizer(6)

class RandomItems(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        return item_randomizer()

class RandomSetup(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        setup_amount = request.args.get('setup_amount')
        if setup_amount:
            return player_setup(int(setup_amount))
        return player_setup(2)

class ResetTracks(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        return reset_tracks()

class FullRandomizer(Resource):
    @cross_origin(supports_credentials=True)
    def get(self):
        return full_randomizer()

api.add_resource(RandomItems, '/random-items')

api.add_resource(RandomTracks, '/random-tracks')

api.add_resource(RandomSetup, '/random-setup')

api.add_resource(ResetTracks, '/reset-tracks')

api.add_resource(FullRandomizer, '/random')


if __name__ == "__main__":
    app.run()
