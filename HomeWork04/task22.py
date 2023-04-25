# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import os 
os.system('clear')

n = (int(input("Введите количество N элементов: ")))
list_n = []
for i in range(n):
    num = int(input(f"Введите {i+1} число: "))
    list_n.append(num)
print(f'Список N элементов: {list_n}')

m = (int(input("Введите количество M элементов: ")))
list_m = []
for i in range(m):
    num = int(input(f"Введите {i+1} число: "))
    list_m.append(num)
print(f'Список M элементов: {list_m}')


total_list = list_n + list_m

print(f'Все заданные числа: {total_list}')

check_list = []
for i in total_list:
    if total_list.count(i) > 1 and i not in check_list:
        check_list.append(i)
print(sorted(set(check_list)))