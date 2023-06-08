import random
from random_words import RandomWords

int_list = []
for i in range(0, 5000) :
    int_list.append(random.randint(0,1000))
print("Unsorted integer list:",int_list)

float_list = []
for f in range(0, 5000) :
    float_list.append(random.uniform(0.1,100.0))
print("Unsorted float list:", float_list)

w = RandomWords()
str_list = []
for s in range(0, 5000) :
    str_list.append(w.random_word())
print("Unsorted words list:", str_list)

