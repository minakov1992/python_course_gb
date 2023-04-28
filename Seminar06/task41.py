# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

import os 
os.system('clear')

from random import randint

my_list = [randint(10,20) for i in range(15)]
count = 0
print(my_list)

for i in range(1,len(my_list)-1):
    if my_list[i-1] < my_list[i] > my_list[i+1]:
        count += 1
print(f'Количество элементов в списке: {count}')

# решение 2
a = [1 for i in range(1, len(my_list)-1) if my_list[i-1] < my_list[i] > my_list[i+1]]
print(f'Количество элементов в списке: {len(a)}')