#Small
#1. Madlib function
#Write a function that accepts two arguments: 
#a name and a subject.
#The function should return a String 
#with the name and subject interpolated in.
#Provide default arguments in case one or both are omitted.

#Scoping works in Python
#subject = "Civil Liberties"  #Global Scoping
#def state_name(): #Defined the function
#    subject = "Amy's favorite subject is" #Local Scoping definedd
#    print(subject) #printed the local scoping of the variable
#
#state_name()
#print(subject) #Global Scoping printed
#def mad_lib(name, subject):
#    print("%s Favorite subject is, %s" % (name, subject))
#
#mad_lib("Amy", "Civil Liberties")
#
#
#
#
#
##2 Celsius to Fahrenheit conversion
#The formula to convert a temperature from 
#Celsius to Fahrenheit is:
#
#F = (C * 9/5) + 32
#
#Write a function that takes a temperature in Celsius, 
#converts it Fahrenheit, and returns the value.
#print("\n")
#def cov_to_C(temp): #created a function (conv2cel) #parameter(named tem[])
#    return(temp+32.) * 5/9 #value returned
#print("32 Farenhieght in Celscius:", cov_to_C(32)) #call function

#3. Fahrenheit to Celsius conversion
#The formula to convert a temperature from 
#Fahrenheit to Celsius is:
#
#C = (F - 32) * 9/5
#
#Write a function that takes a temperature in Fahrenheit, 
#converts it to Celsius, and returns the value.
#print("\n")
#
#celcius = int("input(Enter the temperature"))
#def cov_to_f(temp):
#    c: (temp-32) * 5/9
#    return (c)
#print("32 Celcius in Farenhieght:", cov_to_f(32))
#
#4 is_even function
#Write a function that accepts a number as an 
#argument and returns a Boolean value. 
#Return True if the number is even; 
#return False if it is not even
#print("\n")
#
#def is_even(n):
#     res = False  #default to false
#    if n % 2 == 0:
#        res True
#        return res
#
#
#print(is_even)
#print(is_even(number))
#
#
#5. is_odd function
#Write an is_odd function that uses your 
#is_even function to determine if a number is odd. 
#(That is, do not do the calculation - 
# call a function that does the calculation.)
#
#Hint: You'll use the not keyword
def is_odd(num):
    return (int(n/2) * 2 == num)
if (is)

#6. only_evens function
#Write a function that accepts a List of numbers as an argument.
#
#Return a new List that includes only the even numbers.
#
#only_evens([11, 20, 42, 97, 23, 10])
## Returns [20, 42, 10]
#Hint: use your is_even() function to determine which numbers to include in your new List.

#Medium
##1. Find the smallest number
#Write a function smallest that accepts a List of numbers as an argument.
#
#It should return the smallest number in the List.
#
##2. Find the largest number
#Write a function largest that accepts a List of numbers as an argument.
#
#It should return the largest number in the List

#list_one = []
#num = int(input("Please Enter The # of Entries: "))
#for i in range (1, num + 1):
#    entry = float(input("Please enter a number: "))
#    list_one.append(entry)
#print("Smallest entry is: ", min(list_one), "\nLargest entry is: ", max(list_one))
#
#print("\n")

#3. Find the shortest String
#Write a function shortest that accepts a List of Strings as an argument.
#It should return the shortest String in the List.

print("\n")
#

#
##4. Find the longest String
#Write a function longest that accepts a List of Strings as an argument.
#
#It should return the longest String in the List.
#
#

