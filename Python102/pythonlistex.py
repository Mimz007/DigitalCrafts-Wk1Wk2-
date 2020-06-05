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
