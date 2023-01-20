import random

print("Player 1")

character = []
chosen_character = []

with open("character.txt") as file:
    for line in file: 
            character.append(line.rstrip())

chosen_character = random.sample(character, 1) 
print("Character:", (chosen_character))



vehicle = []
chosen_vehicle = []

with open("vehicle.txt") as file:
    for line in file: 
            vehicle.append(line.rstrip())

chosen_vehicle = random.sample(vehicle, 1) 
print("Vehicle:", (chosen_vehicle))



wheels = []
chosen_wheels = []

with open("wheels.txt") as file:
    for line in file: 
            wheels.append(line.rstrip())

chosen_wheels = random.sample(wheels, 1) 
print("Wheels:", (chosen_wheels))



gliders = []
chosen_gliders = []

with open("gliders.txt") as file:
    for line in file: 
            gliders.append(line.rstrip())

chosen_gliders = random.sample(gliders, 1) 
print("Glider:", (chosen_gliders))


print("Player 2")
character = []
chosen_character = []

with open("character.txt") as file:
    for line in file: 
            character.append(line.rstrip())

chosen_character = random.sample(character, 1) 


print("Character:", (chosen_character))

vehicle = []
chosen_vehicle = []

with open("vehicle.txt") as file:
    for line in file: 
            vehicle.append(line.rstrip())

chosen_vehicle = random.sample(vehicle, 1) 

print("Vehicle:", (chosen_vehicle))

wheels = []
chosen_wheels = []

with open("wheels.txt") as file:
    for line in file: 
            wheels.append(line.rstrip())

chosen_wheels = random.sample(wheels, 1) 

print("Wheels:", (chosen_wheels))

gliders = []
chosen_gliders = []

with open("gliders.txt") as file:
    for line in file: 
            gliders.append(line.rstrip())

chosen_gliders = random.sample(gliders, 1) 

print("Glider:", (chosen_gliders))

item = []

with open("item_list.txt") as file:
    for line in file: 
            item.append(line.rstrip())

random_number = random.randint(0, 21)

chosen_item = random.sample(item, random_number) 

print("Items:")
print(chosen_item)

tracks = []
played_tracks = []
unplayed_tracks = []

print("Tracks:")

with open("tracks.txt") as file:
    for line in file:
        tracks.append(line.rstrip())

with open("played_tracks.txt") as file:
    for line in file:
        played_tracks = line.rstrip().split(",")

for index, track in enumerate(tracks):
    if track not in played_tracks:
        unplayed_tracks.append(track)

for i in range(6):

    if not unplayed_tracks:
        print("No more tracks")
        break

    else:
        random_number2 = random.randint(0,len(unplayed_tracks) - 1)

        current_track = unplayed_tracks[random_number2]

        unplayed_tracks.remove(current_track)

        print(current_track)

        with open("played_tracks.txt", "a") as myfile:
            myfile.write(current_track + ",")
