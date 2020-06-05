# Prompt the user for his name using the input function.
name = input('Hello Beautiful What is your name?')

# Say Hello to them
print(input('%s Hello! \n' % name))

# How Many characters are in the input
print('%s Your name has \n' % (len(name)) +'Letters in it, Awesome!')

# Place out put string in ALL CAPS
print('%s Your name has \n' % (len(name)), 'Letters in it, Awesome!')

# Prompt the user for the missing words to Madlip sentence using the input function
try:
    name2 = input('What is your name?')
    subject = input('What is subject?')
print("%s 's favorite subject in subject in school is %s" % (name,subject))

# Input a number from 0 - 6 a day of the week
Day = input('What Day of The Week Is It, enter a no. 0 - 6?')
if Day == 0:
    print('\n Sunday')
elif Day == 1:
    print('\n Monday')
elif Day == 2:
    print('\n Tuesday')
elif Day ==3:
    print('\n Wednesday')
elif Day ==4:
    print('\n Thursday')
elif Day ==5:
    print('\n Friday')
elif Day ==6:
    print('\n Saturday')
else :
    print('\n Please enter weekday number, 0-6.')

# Work or Sleep In
# Celsius to Fahrenheit
# Looping from 1-10
# n to M
#Print a Square
#Print a Square II

#MEDIUM EXERCISES
#Tip Calculator
bill_amount = int(input("How much was the bill?\n"))

#Create a program that lists your topy 3 favorite foods

favorite_foods = ['tamales', 'jollof', 'oxtail', 'moimoi','suya']
print(favorite_foods[0:5])
counter = 1
for descriptor in favorite_foods:
    print('%d, %s,' % (counter, descriptor))
    length = len(favorite_foods)
    if counter < length:
        print('Thenext one up is %s' % favorite_foods[counter])

    counter+=1

