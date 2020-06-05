try:
    coins_wanted = input('Do you want coins?\n')
except ValueError:
    print('Must answer yes or no')

coins = 0
more_coins = yes

while more_coins == 'yes':

    if coins_wanted == 'yes':
        coins += 1
        print('You have %s coins.' %coins)
        more_coins = input("Do you want more coins?\n")
        print(more_coins)
    elif coins_wanted != 'yes':
        print('Bye')
        exit()
    if more_coins != 'yes':
        print('Bye')
        exit()
    else:
        print("Enter yes or no")
    