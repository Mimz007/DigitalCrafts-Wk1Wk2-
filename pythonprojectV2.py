#VIRTUAL PET


unicorn_fav_food1 = "cake"
unicorn_fav_food2 = "flower"
unicorn_hated_food = "brocolli"
unicorn_happiness = 50
unicorn_hunger = 100
unicorn_food = unicorn_fav_food1 or unicorn_fav_food2 or unicorn_hated_food
pee_on_carpet = False

unicorn_name = input(" Name your Unicorn ")
print()

#tuple = (True, (pee_on_carpet, unicorn_happiness), unicorn_hunger)

def feed_unicorn(unicorn_name, unicorn_happy_level, unicorn_hunger_level):
    unicorn_food = input("What do you want to feed " + unicorn_name + " ?")
    print()

    if unicorn_food == unicorn_fav_food1 or unicorn_food == unicorn_fav_food2:
        unicorn_happy_level += 20
    elif unicorn_food == unicorn_hated_food:
        unicorn_happy_level -= 40
    elif unicorn_food == "sand":
        print("DON'T DO THAT YOU MEANIE")
        print()
        return True, unicorn_happy_level, unicorn_hunger_level
    else:
        unicorn_hunger_level -= 10

    print(unicorn_name + " eats the " + str(unicorn_food) + ".")

    if unicorn_happiness >= 80:
        print(unicorn_name + " is estatic!!!")
    elif unicorn_happiness >= 50:
        print(unicorn_name + " is happy ")
    elif unicorn_happiness >= 25:
        print(unicorn_name + " is a bit down ")
    else:
        print(unicorn_name + " is depressed ")
    print()

    unicorn_hunger_level -= 20

    return False, unicorn_happy_level, unicorn_hunger_level
    
def play_with_unicorn(unicorn_name, unicorn_happiness, unicorn_hunger):
    if unicorn_happiness <= 50:
        print(unicorn_name + "isnt in the mode to play")
        print()
        return unicorn_happiness, unicorn_hunger
    if unicorn_hunger > 60:
        print(unicorn_name + " is too hungry to play! ")
        unicorn_happiness = -20
        return unicorn_happiness, unicorn_hunger
    thrown_object = input(" What do you want to play with? ")
    print()
    print("You throw the " + thrown_object + ".")
    print()
    if unicorn_happiness >= 80:
        print(unicorn_name + " retrieves the " + thrown_object + "while wagging")
    elif unicorn_happiness >= 70:
        print(unicorn_name + " takes their time retrieving the  " + thrown_object + "while wagging")
    else:
        print(unicorn_name + " watches the " + thrown_object)
    print()
    unicorn_hunger += 20

    return unicorn_happiness, unicorn_hunger

while True:
    if not pee_on_carpet:
        unicorn_activity = input("Do you want to 'feed' or 'play' with " + unicorn_name + "?")
    else:
        unicorn_activity = input("Do you want to 'feed' or 'play with' " + unicorn_name + " or do you want to clean up 'pee on carpet'")
    print()
    
    if unicorn_activity == "feed":
       returned_values = feed_unicorn(unicorn_name, unicorn_happiness, unicorn_hunger)
       fed_unicorn_sand, unicorn_happiness, unicorn_hunger = returned_values

       if unicorn_hunger <= 0:
        print(unicorn_name + " pees on your carpet ")
        print()
        pee_boolean = True
        unicorn_hunger_level = 100       
               
    elif unicorn_activity == "play":
       returned_values = play_with_unicorn(unicorn_name, unicorn_happiness, unicorn_hunger)
       unicorn_happiness = returned_values [0]  #tuples (using indexes to get data out)
       unicorn_hunger = returned_values [1]

    elif unicorn_activity == "quit":
        print(unicorn_name + " goes back to bed. ")
        break

    elif unicorn_activity == "clean":
        if pee_on_carpet:
            print("You clean up" + unicorn_name + "'s pee")
            print()
            pee_on_carpet = False
        else:
            print("There's nothing to clean")
    
    elif unicorn_activity == "chasing rainbows":  #cheat code
        print(unicorn_name + "loves Chasing Rainbows" + unicorn_name + "loves you")
        unicorn_happiness = 100
        
    else:
        print("Please either 'feed' or 'play' with  " + unicorn_name + " or 'clean' or 'quit'")
        print()
        continue #returns to the top of the else block, deters punishment for typos, mistypes et. al

    if unicorn_hunger > 70:
        print(unicorn_name + " seems kinda hungry...")
        print()
        unicorn_happiness -= 10
    
    if pee_on_carpet:
        unicorn_happiness -= 10
    if unicorn_happiness <= 0: 
        print(unicorn_name + " bites you! and runs away")
        print("You Faint From A Brokenheart!")
        break

print("GAME OVER")       
#exit()
