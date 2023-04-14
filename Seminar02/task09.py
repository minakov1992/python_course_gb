# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

import os 
os.system('clear') 

my_limit = int(input('Введите предел факториала: '))

fact = 1
count = 1
while count <= my_limit:
    fact *= count
    count += 1

print(fact)