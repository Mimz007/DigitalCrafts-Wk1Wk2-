# Create a program that will ask for a username and then a password.

# If the username or password length is less than 6 charecters give a too short message.

# if the username or password length is greater than 12 charecters give a too long message

# Have the user confirm the password in again.

# If the passwords match give a sucess message

# if the passwords do not match give a mismatch message

# If the password is only numbers give a message that says it cannot be a number.

# (challange) have only one print statement in the whole program.

count = 0
number = input('choose a number between 10 - 101 \n')

try:
    number = int(number)
except ValueError:
    print('that will be a Negative.')
    exit()

    if int(number)< 10 or int(number) >101:
        print('number not in the range!')
    elif number == 42:
        print('You are a Genius')
   
    if number == -1:
        print('Well Hello SmartyPants')
    elif number < 10 or number > 101:
        print('not the instruction')
    elif number == 42:
        print('you have reached the top love')
    else:
        print('You followed instructions. %s was your number.' % number)



