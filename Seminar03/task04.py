# Напишите программу для печати всех уникальных значений в словаре.

import os
os.system('clear')

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]
# print("Все значения в словаре: ", my_list)
# u_value = set(val for dic in my_list for val in dic.values())
# print("Уникальные значения: ",u_value)

my_list = [{"V": "S001"}, {"V": "S002"},
           {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {" V ": "S009"},
           {" VIII ": "S007"}]
uniq = set()
for item in my_list:
    for value in item.values():
        uniq.add(value)
        
print(uniq)
