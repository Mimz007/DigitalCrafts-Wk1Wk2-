#UNICORN YARD 


game_state = {}
game_state["unicorn_fav_foods"] = ["apples", "flowers"]
game_state["unicorn_hated_foods"] = ["brocolli", "cigars", "chitlins"]
game_state["unicorn_happiness"] = 50
game_state["unicorn_hunger"] = 100
game_state["unicorn_food"] = "unicorn_fav_food1" or "unicorn_fav_food2" or "unicorn_hated_food"
game_state["pee_on_carpet"] = False
game_state["unicorn_name"] = input(" Name your Unicorn ")
game_state["taking_care_of_unicorn"] = True

commands = {"feed": feed_unicorn}

print()

def feed_unicorn(game_state):
    unicorn_food = input("What do you want to feed " + game_state["unicorn_name"] + " ?")
    print()

    if unicorn_food in game_state["unicorn_fav_foods"]:
        game_state["unicorn_happiness"] += 20
    elif unicorn_food == game_state["unicorn_hated_foods"]:
        game_state["unicorn_happiness"] -= 40
    elif unicorn_food == "sand":
        print("DON'T DO THAT YOU MEANIE")
        print()
        return
    elif unicorn_food == "grass":
        print("Oh oh ohhh I'm loving it")
        game_state["unicorn_happiness"] +=10

    else:
        game_state["unicorn_happiness"] -= 10

    print(game_state["unicorn_name"] + " eats the " + str(unicorn_food) + ".")

    if game_state["unicorn_happiness"] >= 80:
        print(game_state["unicorn_name"] + " is estatic!!!")
    elif game_state["unicorn_happiness"] >= 50:
        print(game_state["unicorn_name"] + " is happy ")
    elif game_state["unicorn_happiness"] >= 25:
        print(game_state["unicorn_name"] + " is a bit down ")
    else:
        print(game_state["unicorn_name"] + " is depressed ")
    print()

    game_state["unicorn_hunger"] -= 20    
       
    if game_state["unicorn_hunger"] <= 0:
            print(game_state["unicorn_name"]+ " pees on your carpet ")
            print()
            game_state["pee_boolean"] = True
            game_state["unicorn_hunger"] = 100    

def play_with_unicorn(game_state):
    if game_state["unicorn_happiness"] <= 50:
        print(game_state["unicorn_name"] + "isnt in the mode to play")
        print()
        return
    if game_state["unicorn_hunger"] > 60:
        print(game_state["unicorn_name"] + " is too hungry to play! ")
        unicorn_happiness = -20
        return 
    thrown_object = input(" What do you want to play with? ")
    print()
    print("You throw the " + thrown_object + ".")
    print()

    if game_state["unicorn_happiness"] >= 80:
        print(
                game_state["unicorn_name"] + " retrieves the " + thrown_object 
                + "at lighning speed")
    elif game_state["unicorn_happiness"] >= 70:
        print(
                game_state["unicorn_name"] + " takes their time retrieving the  " 
                + thrown_object + "while wagging their tail")
    else:
        print(
                game_state["unicorn_name"] + " watches the " 
                + thrown_object + "falls and looks at you sadly")
    print()
    game_state["unicorn_hunger"] += 20

def put_unicorn_to_bed(game_state):
    print(game_state["unicorn_name " + "goes back to bed. :}"])
    game_state["taking_care_of_unicorn"] = False

def clean_up_pee(game_state):
    if game_state["pee_on_carpet"]:
        print("You clean up " + game_state["unicorn_name"] + " 's pee'. ")
        print()
        game_state["pee_on_carpet"] = False
    else:
        print("There's Nothing To Clean")

def cheat(game_state):
    print(game_state["unicorn_name"] + "loves Chasing Rainbows" 
         + game_state["unicorn_name"] + "loves you")
    game_state["unicorn_happiness"] = 100

        
while game_state["taking_care_of_unicorn"]:
    if not game_state["pee_on_carpet"]:
        unicorn_activity = input(
                    "Do you want to 'feed' or 'play' with " 
                    + game_state["unicorn_name"] + "?")
    else:
        unicorn_activity = input(
                "Do you want to 'feed' or 'play with' " 
                + game_state["unicorn_name"] + " or do you want to clean up 'pee on carpet'")
    print()
    
    if unicorn_activity == "feed":
       feed_unicorn(game_state)   
               
    elif unicorn_activity == "play":
       play_with_unicorn(game_state)
      
    elif unicorn_activity == "quit":
        put_unicorn_to_bed(game_state)

    elif unicorn_activity == "clean":
        clean_up_pee(game_state)
    
    elif unicorn_activity == "chasing rainbows":
        cheat(game_state)
        
    else:
        print("Please either 'feed' or 'play' with  " + game_state["unicorn_name"] + " or 'clean' or 'quit'")
        print()
        continue #returns to the top of the else block, deters punishment for typos, mistypes et. al

    if game_state["unicorn_hunger"] > 70:
        print(game_state["unicorn_name"] + " seems kinda hungry...")
        print()
        game_state["unicorn_happiness"] -= 10
    
    if game_state["pee_on_carpet"]:
        game_state["unicorn_happiness"] -= 10
    if game_state["unicorn_happiness"] <= 0: 
        print(game_state["unicorn_name"] + " bites you! and runs away")
        print("You Faint From A Brokenheart!")
        game_state["taking_care_of_pet"] = False
        break

print("GAME OVER")       
#exit()