# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.


import os
os.system('clear')


def reverse_list(n):
    if n == 1:
        return '1'
    else:
        return f'{n} -> {reverse_list(n-1)}'
    return ('1' if n == 1 else f'{n} -> {reverse_list(n-1)}')

num = int(input())
print(reverse_list(num))

def reverse(text: str):
    if len(text) == 1:
        return text
    return text[-1] + reverse(text[:-1])

text = input()
print(reverse(text))