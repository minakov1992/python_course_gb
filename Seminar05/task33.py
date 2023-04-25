# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

import random
import os
os.system('clear')


# size = int(input('Введите количество оценок: '))
# min_value = int(input('Введите минимальную оценку: '))
# max_value = int(input('Введите максимальную оценку: '))

# my_list = [random.randint(min_value, max_value) for _ in range(size)]
# print(my_list)

# for i in range(len(my_list)):
#     if my_list[i] == max_value:
#         my_list[i] = min_value
# print(my_list)

# # решение 2
# mark_list = [random.randint(1,5) for _ in range(10)]
# print(mark_list)
# mark_list = [min(mark_list) if i == max (mark_list) else i for i in mark_list]
# print(mark_list)

# решение 3
print(mark_list := [random.randint(1,5) for _ in range(10)])
print([min(mark_list) if i == max (mark_list) else i for i in mark_list])