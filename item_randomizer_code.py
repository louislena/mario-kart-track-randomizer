import random

item = []

with open("item_list.txt") as file:
    for line in file: 
            item.append(line.rstrip())

random_number = random.randint(0, 21)

chosen_item = random.sample(item, random_number) 

print(chosen_item)

tracks = []
played_tracks = []
unplayed_tracks = []

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


vehicle = []

with open("vehicle.txt") as file:
    for line in file: 
            item.append(line.rstrip())

random_vehicle = random.randint(0, )


