# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

import os
os.system('clear')


def summa(a, b):

    if b == 0:
        return a

    return summa(a + 1, b - 1)


result = summa(int(input('Число А: ')),
               int(input('Число В: ')))
print(f'Сумма: {result}')
