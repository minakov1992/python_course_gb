# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

import os 
os.system('clear') 

n = int(input('km per day: '))
m = int(input('total length: '))

# print(int(-1 * m // n * -1))
print(int((m + n - 1)//n))