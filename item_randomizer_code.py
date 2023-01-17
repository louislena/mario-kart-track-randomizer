import random

item = []

with open("item_list.txt") as file:
    for line in file: 
            item.append(line.rstrip())

random_number = random.randint(0, 21)

x = random.sample(item, random_number) 

#print(x)

for i in range(7):
    tracks = []
    played_tracks = []
    unplayed_tracks = []

    with open("tracks.txt") as file:
        for line in file:
            tracks.append(line.rstrip())

    with open("played_tracks.txt") as file:
        for line in file:
            played_tracks.append(int(line.rstrip()))

    for index, track in enumerate(tracks):
        if index in played_tracks: 
            print("hei")
        else:
            unplayed_tracks.append(track)

    print(len(unplayed_tracks))

    random_number2 = random.randint(0,len(unplayed_tracks) - 1)

    print(unplayed_tracks[random_number2])

    with open("played_tracks.txt", "a") as myfile:
        myfile.write(str(random_number2) + "\n")




#random_value = random.choices(item, k = random_number)
#print(random_value)
