#Lists can also be called array
#lists are an ordered/sequenced number of things
# mylist = {} is an empty list
#lists start with zero

#Examples of a List
#
han_description = ['stuck-up','half-witted', 'scruffy-looking', 'nerf herder']
lukes_real_hands = ['left']

people_who_like_jar_jar = []

print(han_description[1])
print(lukes_real_hands[0])

print(han_description[-1])
print(han_description)
print(han_description[1:3])
print(han_description[2:])
print(han_description[:3])
print(han_description[:-3:-1])
print(han_description[-1:])

# WHILE LOOP THROUGH THE ARRAY
han_description = ['stuck-up','half-witted', 'scruffy-looking', 'nerf herder']
list_size = len(han_description)

index = 0
print('Why you:')

while index < list_size:
    print('%d, %s' % (index+1, han_description[index])
    index += 1

