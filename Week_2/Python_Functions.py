##Types of Functions
#print("Hi") #print function 
##print function can handle multiple arguments inside of it
#my_list = ["1", "2", "4"] #List Function
#len(my_list) #lenght takes only one arguments
#print(type(my_list)) #a function executed inside of the argument of a function
# #How to create a function
#def my_func():                      #How you start a function is with def.  Function declared
#    return "I created a function"   #when you declare a function, you have to do something with it
#
#results = my_func() 
#print(results) #this line prints the value returned in
#
##when you Def its call a parameters
##Arguments is what you are given
##Always place a ":" at the end of a statment

#def droid_count(start_count, destroyed_count):
#    results = "start_count" - "destroyed_count"
#    return results
#
#print(droid_count(100,23))
#
#yoda_quotes = ["define a function that just prints something with no return"]
#
#def count_quotes():
#    print(len(yoda_quotes))
#
#result = count_quotes
#print(result)

quote = "The ability to speak does not make you intelligent."
def make_quote():
    quote = "This is not true" #quote has to be declared in order to print
    print(quote)

make_quote()
print(quote)