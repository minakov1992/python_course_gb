# Дан список чисел. Определите, сколько в нем встречается различных чисел.

import os 
os.system('clear')

# a = [0, 1, 2, 2, 3, 4]
# print(len(set(a)))

print(set_num := input('Введите список чисел: '), len((set(set_num))))