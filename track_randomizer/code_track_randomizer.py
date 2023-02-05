import random

def track_randomizer(number_of_tracks):

    tracks = []
    played_tracks = []
    unplayed_tracks = []
    response = []

    with open("track_randomizer/tracks.txt") as file:
        for line in file:
            tracks.append(line.rstrip())

    with open("track_randomizer/played_tracks.txt") as file:
        for line in file:
            played_tracks = line.rstrip().split(",")

    for track in tracks:
        if track not in played_tracks:
            unplayed_tracks.append(track)

    for i in range(number_of_tracks):

        if not unplayed_tracks:
            reset_tracks()
            return track_randomizer(number_of_tracks)
            
        else:
            random_number2 = random.randint(0,len(unplayed_tracks) - 1)

            current_track = unplayed_tracks[random_number2]

            unplayed_tracks.remove(current_track)

            response.append(current_track)

            with open("track_randomizer/played_tracks.txt", "a") as myfile:
                myfile.write(current_track + ",")
                
    return response

def reset_tracks():

    with open("track_randomizer/played_tracks.txt", "w") as myfile:
                    myfile.write("")

    return "List reset complete <3"