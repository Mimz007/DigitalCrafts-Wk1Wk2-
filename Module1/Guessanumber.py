#Guess The Number Game
#Hard code secret number to 5
#Use While Loop until desired number is added
#Print "You Win!" when correct number is enter
#If wrong number prompt for number again

magic_number = 5
greeting = input('Hello What is Your Name?')
print(input('%s Welcome To the Game! \n' % greeting))
ask_magicnumber= int(input('I am thinking of a number 1-10, Guess the number \n'))

while magic_number != ask_magicnumber:
    if ask_magicnumber == magic_number:
        print("GENIUS!, You win")
        exit()
    if ask_magicnumber != magic_number:
        print("NOPE!, Wrong Ans")
        print(ask_magicnumber)
    if int(ask_magicnumber) < 1 or int(ask_magicnumber) >10:
        print('Please enter a number ranging 1 - 10')
    else:
        print(ask_magicnumber)
    
