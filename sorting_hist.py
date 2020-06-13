word = input("Give me a word dog.\n")
word_list = {}
for letter in word:
    if(letter in word_list):
        word_list[letter] += 1
    else:
            word_list[letter] = 1

print(word_list)

top_3 =[]  
for i in range(0,2):
    highest = None
    highest_value = 0
    for word in word_list:
        if word_list[word] > highest:
            highest_value = word_list[word]
            highest = letter

print(highest, highest_value)
del word_list[letter]

