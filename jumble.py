#Write a program that jumbles a random word from a list several different times and prints the result.
#Every action that "does" something must be in a function. (print, shuffle, get input etc need to be in a function, but data can be global)
#Every function should have a specific and clearly defined purpose.
#(challange) Have the user specify the number of times to shuffle the word. (all the challanges need to follow the rules 1 and 2)
#(extra challange) the user guesses the word and a score is kept.
#(Extra Extra challange) use recursion in place of any while loops. 

import random   #whenever you have to jumble words you have to ("import random")

def get_scrambled  #define a function
scambled =[]
for 
def setup(word = None):
    if not word:
        word = words[random.randint(0, len(words)-1)]
    sample_count = get_samples()
    if not sample_count:
        setup(word)
    else:
        return get_scrambled(word, sample_count)