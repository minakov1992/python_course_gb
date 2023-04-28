# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.


from random import randint
import os
os.system('clear')


def prompt(msg):
    a = int(input(msg))
    return a


def summarize(number, sum=0):
    for item in range(1, number//2 + 1):
        if number % item == 0:
            sum += item
    return sum


k = 10000
print(my_list := [i for i in range(k)])
for item in my_list:
    if item == summarize(summarize(item)) and item != summarize(item):
        print(item, summarize(item))
