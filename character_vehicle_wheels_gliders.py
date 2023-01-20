import random 

character = []
chosen_character = []

with open("character.txt") as file:
    for line in file: 
            character.append(line.rstrip())

#random_vehicle = random.randint(0, 29)

chosen_character = random.sample(character, 1) 

print(chosen_character)


vehicle = []
chosen_vehicle = []

with open("vehicle.txt") as file:
    for line in file: 
            vehicle.append(line.rstrip())

chosen_vehicle = random.sample(vehicle, 1) 

print(chosen_vehicle)

wheels = []
chosen_wheels = []

with open("wheels.txt") as file:
    for line in file: 
            wheels.append(line.rstrip())

chosen_wheels = random.sample(wheels, 1) 

print(chosen_wheels)

gliders = []
chosen_gliders = []

with open("gliders.txt") as file:
    for line in file: 
            gliders.append(line.rstrip())

chosen_gliders = random.sample(gliders, 1) 

print(chosen_gliders)


