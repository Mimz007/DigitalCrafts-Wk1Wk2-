#Create a program (using using only a single class) that creates a dice rolling system for a d6, d12, d20.
#Have the user choose one of the 3 dice and roll it. 
#Have each dice keep a record of how many times it was rolled and what was rolled.
#Have the user be able to request the average roll for a single dice.
#(Challange) Create a Cheat d20 dice that has a cheat_roll function that will ask for a target number and get within two of that number. However it can only be used once every 10 rolls. (this can be a subclass)
#(Extra Challange) Allow a user to 'create' their own dice of any size, and be able to use it in the program.
#(Extra Extra Challange) have a menu for each dice to have options like "show rolls, show averages,reset roll count.

import random

class Dice():
    def __init__(self,name,value):
        self.name = name
        self.value = value

dice_with_6 = Dice("6", random.randint(1,6))
dice_with_12 = Dice("12", random.randint(1,12))
dice_with_20 = Dice("6", random.randint(1,20))

count_dice_rolled = {}
count = 0

while True:
    try:
        user_input = int(input("please choose a number 6, 12 or 20"))
    except TypeError:
        print("You need to type a number only")
        user_input

create_your_own_dice =int(input("you have the option to cre"))

    if user_input == 6:
        rolled = dice_with_6.value
        count += 1
        count_dice_rolled.update({count:rolled})
        average_roll = rolled/count
        c

    elif user_input == 12:
            rolled = dice_with_12.value
            count +=1
            count_dice_rolled.update({count:rolled})
            average_roll = rolled/count
            print(average_roll)

    elif user_input == 20:
            rolled = dice_with_20.value
            count +=1
            count_dice_rolled.update({count:rolled})
            average_roll = rolled/count
            print(average_roll)

count+=1
    if count == 5:
        break
        







