# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

import os 
os.system('clear')

def simple_numbers(n):
    for i in range(2, n):
        if n % i == 0:
            result = 'Число составное'
            break
        else:
            result = 'Число простое'
    return (result)

n = int(input('Введите число: '))
print(simple_numbers(n))

# number = int(input('Введите число: '))
# def is_simple(num: int) -> bool:
#     if num in [1,2]:
#         return True
#     elif not num % 2:
#         return False
#     else:
#         for i in range(3, num//2 + 1, 2):
#             if num % i == 0:
#              return False
#     return True

# print(is_simple(number))
