import random

#VIRTUAL PET GAME:
#You can come up with your own solution or you can use the walk through provided in the learning portal.
#https://learn.digitalcrafts.com/immersive/lessons/solving-problems-using-code/object-oriented-programming/#learning-objectives
#If you are doing the walk through do the excersies small and medium.
#If you have time add the ability to have multiple pets, consider ascii art.
#Keep building and making it better until time is up.


#print("Welcome 2 UNICORN VILLAGE") #welcome message
#ready = input("Are you ready to play? ")  
#
#print("\n")
#
#if ready == "yes" or "Yes":
#    print("Let the fun begin")
#else:
#    print("You are not worthy of us")
#    exit()
#
#p1name = print(input(" Whats Your Name "))
#print("What Specie is your Unicorn?")
#unicorn_type = input()
#print("is your unicorn a boy or a girl?")
#unicorn_sex = input()
#print(unicorn_name + " the " + unicorn_type + " is a good " + unicorn_sex + ".")
#print("How old is " + unicorn_name)
#unicorn_age = input()
#next_year_age = int(unicorn_age) + 1
#print("Next Year," + unicorn_name + " Will Be " + str(next_year_age) + " years old")
#unicorn_type = "zazzou"

def scold_player(unicorn_name):
    print("Don't do that to" + unicorn_name + "you Meanie!")
    print()
    return "Yo!"

unicorn_fav_food1 = "rainbow cake"
unicorn_fav_food2 = "lotus flower"
unicorn_hated_food = "brocolli"
unicorn_happiness = 50
unicorn_hunger = 100
unicorn_food = unicorn_fav_food1 or unicorn_fav_food2
pee_on_carpet = False


unicorn_name = input(" Name your Unicorn ")
print()

while True:
    if not pee_on_carpet:
        unicorn_activity = input("Do you want to 'feed' or 'play' with " + unicorn_name + "?")
    else:
        unicorn_activity = input("Do you want to 'feed' or 'play with' " + unicorn_name + " or do you want to clean up 'pee on carpet'")
    print()
    
    if unicorn_activity == "feed":
        unicorn_food = input("What do you want to feed " + unicorn_name + " ?")
        print()

        if unicorn_food == unicorn_fav_food1 or unicorn_food == unicorn_fav_food2:
            unicorn_happiness += 20
        elif unicorn_food == unicorn_hated_food:
            unicorn_happiness -= 40
        elif unicorn_food == "sand":
            return_value = scold_player(unicorn_name)
            print(return_value)
            continue  #returns to the top of the top of the while loo[]
        else:
            unicorn_happiness -= 10

        print(unicorn_name + " eats the " + unicorn_food + ".")

        if unicorn_happiness >= 80:
            print(unicorn_name + " is estatic!!!")
        elif unicorn_happiness >= 50:
            print(unicorn_name + " is happy ")
        elif unicorn_happiness >= 25:
            print(unicorn_name + " is a bit down ")
        else:
            print(unicorn_name + " is depressed ")
        print()

        unicorn_hunger -= 20

        if unicorn_hunger <= 0:
            print(unicorn_name + " pees on your carpet ")
            print()
            pee_on_carpet = True
            unicorn_hunger = 100

        
    elif unicorn_activity == "play":
        if unicorn_happiness >= 50:
            if unicorn_hunger > 60:
                print(unicorn_name + " is too hungry to play! ")
                unicorn_happiness = -20
            else:
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
        else:
            print(unicorn_name + " isn't in the mood to play ...")
            print()

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
    
    elif unicorn_activity == "chasing rainbows":
        print(unicorn_name + "loves Chasing Rainbows" + unicorn_name + "loves you")
        unicorn_happiness = 100
        
    else:
        print("Please either 'feed' or 'play' with  " + unicorn_name + " or 'clean' or 'quit'")
        print()
        continue

    if unicorn_hunger > 70:
        print(unicorn_name + " seems kinda hungry...")
        print()
        unicorn_happiness -= 10
    
    if pee_on_carpet:
        unicorn_happiness -= 10
    if unicorn_happiness <= 0: 
        print(unicorn_name + " bites you! and pees on your carpet")
        print("You SCREAM from ANGER!")
        break

print("GAME OVER")       
exit()
