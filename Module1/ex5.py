# number = 1
# sep = '_____'
# while number <= 10:
#    print(number)
#    print(sep)
#    number += 1


number = 100
dec_by = 10
while number >= 0:
    if number !=50 and number != 30:
        print('%s%% downloaded %s%% remaining.' % (100-number, number))
    number -= dec_by



