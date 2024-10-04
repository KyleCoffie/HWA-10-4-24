#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

catering = str (input("Catering? Y/N?"))
if catering == "Y" : 
    food_choice = (input("vegetarian or non-vegetarian?"))
    if food_choice == "vegetarian":
        print ("I reccomend Veggie Delight!")
    else:
        print("Try Gourmet Meals Caters")
else:
    print ("If stirring your family's mac and cheese doesnt sound like someone walking in the rain with flipsflops on I wont be attending.")