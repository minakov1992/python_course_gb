# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random
import os
os.system('clear')


size = int(input('Введите размер вашего списка: '))
min_limit = int(input('Введите минимальный предел: '))
max_limit = int(input('Введите максимальный предел: '))


my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
print(my_list)
number = int(input('Введите искомое число: '))

# count = 0
# for item in my_list:
#     if item == number:
#         count += 1
count = my_list.count(number)

close_number = my_list[0]
if count == 0:
    for item in my_list:
        if abs(number - item) < (number - close_number):
            close_number = item
print(f'Число "{number}" встречается {count} раз' if count > 0 else f'Ближайшее к  числу "{number}" число: "{close_number}"')
