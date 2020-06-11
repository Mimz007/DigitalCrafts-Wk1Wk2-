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
#    print("Let the adventure begin")
#else:
#    print("You are not worthy of us")
#    exit()
#
#p1name = print(input("Whats Your Name "))
#print("Name your Unicorn")
#unicorn_name = input()
#print("What Specie is your Unicorn?")
#unicorn_type = input()
#print("is your unicorn a boy or a girl?")
#unicorn_sex = input()
#print(unicorn_name + " the " + unicorn_type + " is a good " + unicorn_sex + ".")
#print("How old is " + unicorn_name)
#unicorn_age = input()
#next_year_age = int(unicorn_age) + 1
#print("Next Year," + unicorn_name + " Will Be " + str(next_year_age) + " years old")

unicorn_name = "sissy"
unicorn_type = "zazzou"
unicorn_happiness = 50
unicorn_hunger = 50
unicorn_fav_food = "pizza"
unicorn_hated_food = "brocolli"

while unicorn_hunger or unicorn_happiness <= 50:
    print("Your " + unicorn_name + " is sad and hungry")
    unicorn_food = input("What kind of food do you want to give " + unicorn_name + " ?")
    print(input)
    if unicorn_food == "pizza":
        unicorn_happiness = unicorn_happiness + 100
    else:
        if unicorn_food == "soda":
            unicorn_happiness = unicorn_happiness - 30
        if unicorn_food == "brocolli":
            unicorn_happiness = unicorn_happiness - 40
        else:
            unicorn_happiness = unicorn_happiness - 50
    if unicorn_hunger > 50:
        print("Your Unicorn is not hungry")
    if unicorn_happiness >= 100:
        print("Your " + unicorn_name + " is estatic")
    else:
        if unicorn_happiness >= 100:
            print("Your " + unicorn_name + " is in High Spirits")
        else:
            if unicorn_happiness >=20:
                print("Your " + unicorn_name + "is not happy")
            else:
                print("Your " + unicorn_name + " is very sad")
print("\n")

print(unicorn_name + " eats the food")
print(unicorn_name + " the " + unicorn_type + "'s happiness is at " + str(unicorn_happiness))






#protection = {
#    "fly", 
#    "fire spit", 
#    "roll", 
#    "hide"
#    }
#play_options = {
#    "pet", 
#    "feed", 
#    "groom"
#    }
#mood = {
#    "hungry", 
#    "happy", 
#    "sad"
#    }
#
#def 
#

