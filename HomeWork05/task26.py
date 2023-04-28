# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('clear')


def exponation(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * exponation(a, b - 1))


result = exponation(int(input("Введите число: ")),
                    int(input("Введите степень: ")))
print(f'Результат: {result}')
