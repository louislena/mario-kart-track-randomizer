import random

tracks = []
played_tracks = []
unplayed_tracks = []

with open("tracks.txt") as file:
    for line in file:
        tracks.append(line.rstrip())

with open("played_tracks.txt") as file:
    for line in file:
        played_tracks.append(line.rstrip())

for index, track in enumerate(tracks):
    if index not in played_tracks: 
        unplayed_tracks.append(track)

random_number = random.randint(0,len(unplayed_tracks))
print(unplayed_tracks[random_number])

with open("played_tracks.txt", "a") as myfile:
    myfile.write(str(random_number) + "\n")