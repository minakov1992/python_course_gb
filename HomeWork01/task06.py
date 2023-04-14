# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:
# 385916 -> yes
# 123456 -> no

import os 
os.system('clear') 

a = int(input('Введите шестизначное число: '))   
if (len(str(a)) == 6):
    a1 = a // 100000
    a2 = a // 10000 % 10
    a3 = a // 1000 % 100 % 10
    a4 = a // 100 % 1000 % 100 % 10
    a5 = a // 10 % 10000 % 1000 % 100 % 10
    a6 = a % 10
    b1 = (a1 + a2 + a3)
    b2 = (a4 + a5 + a6)
    if (b1 == b2):
        print('Ура! Вы являетесь обладателем счастливого билетика! Фортуна на вышей стороне :)')
    else:
        print('У вас самый обычный билетик :(')
else:
        print('Число не является шестизначным.')        