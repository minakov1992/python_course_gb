# 39. Даны два массива чисел.
# Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве

import os 
os.system('clear')

import random

# from random import randint

# def prompt(msg):
#     a = int(input(msg))
#     return a

# def new_list(minn, maxx, length):
#     a = [randint(minn, maxx) for i in range(length)]
#     return a

# def uniq_list(list1, list2):
#     uniq_list = list()
#     for item in list1:
#         if item not in list2:
#             uniq_list.append(item)
#     return uniq_list

# first_list = new_list(1, 10, 10)
# second_list = new_list(1, 5, 10)

# print(first_list, second_list, uniq_list(first_list, second_list), sep="\n")

# list1 = [random.randint(0, 20) for _ in range(20)]
# list2 = [random.randint(0, 20) for _ in range(10)]
# print(list1)
# print(list2)

# new_list = [i for i in list1 if i not in list2]
# print(new_list)


list1 = [random.randint(0, 20) for _ in range(20)]
list2 = [random.randint(0, 20) for _ in range(10)]
print(f'{list1} {list2}')
for i in list:
    if i not in list2:
        print(i, end =" ")