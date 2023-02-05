import random 


def player_setup(number_of_players):

    all_players = []

    for i in range(number_of_players):

        character = []
        chosen_character = []
        response = {} 

        with open("player_setup_randomizer/character.txt") as file:
            for line in file: 
                    character.append(line.rstrip())

        response["Character"] = random.sample(character, 1)[0]


        vehicle = []
        chosen_vehicle = []

        with open("player_setup_randomizer/vehicle.txt") as file:
            for line in file: 
                    vehicle.append(line.rstrip())

        response["Vehicle"] = random.sample(vehicle, 1)[0]

        wheels = []
        chosen_wheels = []

        with open("player_setup_randomizer/wheels.txt") as file:
            for line in file:
                    wheels.append(line.rstrip())

        response["Wheels"] = random.sample(wheels, 1)[0]

        gliders = []

        chosen_gliders = []

        with open("player_setup_randomizer/gliders.txt") as file:
            for line in file:
                    gliders.append(line.rstrip())

        response["Glider"] = random.sample(gliders, 1)[0]

        all_players.append(response)

    return all_players

