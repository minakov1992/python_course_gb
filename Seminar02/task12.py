# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

import os 
os.system('clear') 

import random

MAX_WEIGHT = 5000
MIN_WEIGHT = 100


watermelon = int(input("Введите количество арбузов: "))
weigth = 0
max_weigth = MIN_WEIGHT
min_weigth = MAX_WEIGHT

for i in range(watermelon):
    weigth = random.randint(MIN_WEIGHT, MAX_WEIGHT)
    print(weigth, end=" ")
    if weigth > max_weigth:
        max_weigth = weigth
    if weigth < min_weigth:
        min_weigth = weigth
print(f"\nАрбуз Ивана Васильевича {max_weigth} г.")
print(f"Арбуз тёщи {min_weigth} г.")