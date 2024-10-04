attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
if attendees <= 100: 
    print("We recommend using the " + venue + " with an audio system with this number of attendees.")
if attendees >= 101:
    print("We reccomend using the " + venue + " with an audio system and a projector with this many attendees.")