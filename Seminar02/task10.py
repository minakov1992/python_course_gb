# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

import os 
os.system('clear') 

# цикл while
fibonacci1 = fibonacci2 = 1
n = int(input("Номер элемента ряда Фибоначчи: "))
i = 0
while i < n - 2:
    fibonacci_sum = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci_sum
    i = i + 1
print("Значение этого элемента:", fibonacci2)

# # цикл for
# fibonacci1 = fibonacci2 = 1
# n = int(input("Номер элемента ряда Фибоначчи: "))
# print(fibonacci1, fibonacci2, end=' ')
# for i in range(2, n):
#     fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
#     print(fibonacci2, end=' ')

# # рекурсия
# n = int(input("Номер элемента ряда Фибоначчи: "))
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))