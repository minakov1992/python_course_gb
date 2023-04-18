# Дан список, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов списка,
# больших предыдущего (элемента с предыдущим номером)

import os
os.system('clear')

num_list = [2, 9, 8, 5, 4, 6, 4, 5, 5, 8, 9]
print(num_list)
count = 0
k = len(num_list) - 1
for i in range(k):
    if num_list[i] < num_list[i + 1]:
        count += 1
print(count)
