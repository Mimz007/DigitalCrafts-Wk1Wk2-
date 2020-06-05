#Create a program that asks for several numbers from a user and then adds them up.  You must use a list

num1 = input('Give me a number between 1 - 5')
print(num1)
num2 = input('Give me a second number between 1 - 5')
print(num2)
num3 = input('Give me a third number between 1 - 5')
print(num3)
result = float(num1) + float(num2) + float(num3)
print("THANK YOU")
print("%s Is Your Total \n" % result)

# Extra Challenge
number = [2]
numbers = [2, 4, 6]
result2 = number + numbers
print(result2)

exit()


