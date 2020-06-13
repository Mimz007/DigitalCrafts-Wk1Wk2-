#RECURSON IS a function within a function
def clint_func():
    print("Yes")
    clint_func()

clint_func()

def calculate_sum(number_list):
    result = 0
    for number in number_list:
        result += number
    return result