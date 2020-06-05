# Create a program that ask for 2 numbers and then divides the first number from the second number.

# Handle any possible errors without using any 'if'.

# If the result is a valid option, print "The result is X" where X is the value.

# Otherwise give an error that describes the issue.

# (challange) Still without using if. Let the user know which value is causing and exemption.

# (Extra Challange) Still without using ifs, If the first or second value is not a valid integer, have the program keep asking UNTIL the user supplies a valid integer. (think about the bolded word)

try:
    first_num = int(input('Number 1\n'))
    second_num = int(input('Number 2\n'))
    print('The result is %s.' % (first_num/second_num))

except ValueError:
    print('You entered a text')
    exit()

except ZeroDivisionError:
    print('You deivided by zero')
    print('Your Numbers were %s and %s')

    exit()



