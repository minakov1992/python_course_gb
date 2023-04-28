# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

import os 
os.system('clear')

from random import randint

def new_list(minn, maxx, length):
    a = [randint(minn, maxx) for i in range(length)]
    return a

def uniq_dictionary(list1):
    uniq_dict = {}
    for number in list1:
        uniq_dict[number] = uniq_dict.get(number, 0) +1
    print(uniq_dict)
    return uniq_dict

def unic_pairs(dict_n, dict, count = 0):
    for values in dict_n.values:
        if values//2 == 0:
            count += 1

a = new_list(1, 10, 15)
print(a)
new_list =  uniq_dictionary(a)
b = unic_pairs(new_list)
print(b)


# решение 2
import random
my_list = [random.randint(0,5) for _ in range(10)]
print(my_list)
repeats = sum([my_list.count(i)//2 for i in set(my_list)])
print(repeats)