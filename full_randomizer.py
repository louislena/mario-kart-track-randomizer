from track_randomizer.code_track_randomizer import track_randomizer

from player_setup_randomizer.code_character_vehicle_wheels_gliders import player_setup

from item_randomizer.code_item_randomizer_code import item_randomizer

def full_randomizer():
    
    tracks = track_randomizer(6)
    setups = player_setup(2)
    items = item_randomizer()

    response = {
        "Setup" : setups,
        "Items" : items,
        "Tracks" : tracks
        }
    return response