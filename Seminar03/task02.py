# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

import os
os.system('clear')

num_list = [2, 9, 5, 8, 3, 1, 7, 6]
print(num_list)
new_num_list = []
for i in range(1):
    num_list.insert(0, num_list.pop())
print(num_list)

# list_num = list(input(numbers))
# k = int(input(('k')))

# list_num = list_num[-k:] + list_num[:-k]
# print(list_num)