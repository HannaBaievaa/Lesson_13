import random, time
from random_words import RandomWords

int_list = []
for i in range(0, 5000) :
    int_list.append(random.randint(0,1000))
#print("Unsorted integer list:",int_list)

float_list = []
for f in range(0, 5000) :
    float_list.append(random.uniform(0.1,100.0))
#print("Unsorted float list:", float_list)

w = RandomWords()
str_list = []
for s in range(0, 5000) :
    str_list.append(w.random_word())
#print("Unsorted words list:", str_list)

# Bubble sort
def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length -iIndex -1):
            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True
        if not swapped:
            break
    print("Sorted data:", data)

cor_time = time.time()
bubble_sort(int_list)
duration_time1 = time.time() - cor_time
print(f"Duration time int_list:", duration_time1)

print('*'*33)
cor_time = time.time()
bubble_sort(float_list)
duration_time2 = time.time() - cor_time
print(f"Duration time float_list:", duration_time2)

print('*'*33)
cor_time = time.time()
bubble_sort(str_list)
duration_time3 = time.time() - cor_time
print(f"Duration time str_list:", duration_time3)

print('*'*33)
def middle_time(ls, n):
    dur_time = 0
    for i in range(n):
        cor_time = time.time()
        bubble_sort(ls)
        dur_time += time.time() - cor_time
        mid_time = dur_time / n
        return f"Middle time of working cycle:,{mid_time}"

print(middle_time(int_list ,5))
