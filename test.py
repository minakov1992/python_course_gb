# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#         print(summa)


# sum_numbers(5)


def sum_str(*args):
    res = 0
    for i in args:
        res += i
    return res

a = sum_str(1, 5, 9)
print(a)
