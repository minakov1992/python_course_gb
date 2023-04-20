# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

import os 
os.system('clear')


# решение 1
my_string = list(input('Введите строку: '))
print(my_string[0], end= " ")

for i in range(1, len(my_string) - 1):
    print(f"{my_string[i]}", end= " ")
    count = my_string[:i-1].count(my_string[i])
    if count > 0:
        print(f"_{count}", end= " ")
print()

# решение 2
text = list(input('Введите строку: '))
count_dict = {}
for letter in text:
    count_dict[letter] = count_dict.get(letter, 0) + 1
    print(f"{letter}" if count_dict.get(letter) == 0 else f"{letter}_{count_dict.get(letter) - 1}", end= " ")
print()
print(count_dict)