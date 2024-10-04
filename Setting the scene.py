place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: action = ("cross a river")
    print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceedin the dark? ")
    if action== "light a torch":
        print ("You found the pirate's booty!")
    else: action = ("proceed in the dark")
    print("You stumble in the dark in fall!")
