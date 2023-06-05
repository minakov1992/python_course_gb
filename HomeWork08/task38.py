# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

from os import path
import os
os.system('clear')


data_base = "phonebook.txt"
all_data = []
last_id = 0

if not path.exists(data_base):
    with open(data_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(data_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])
        return all_data


def show_all_contacts():
    if not all_data:
        print("Пусто.")
    else:
        print(*all_data, sep="\n")


def add_new_contact():
    global last_id
    array = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    answers = []
    for i in array:
        answers.append(data_collection(i))
    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))
        with open(data_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("Контакт добавлен!\n")
    else:
        print("Данные уже существуют!")


def delete_contact():
    global all_data
    symbol = "\n"
    show_all_contacts()
    del_record = input("Введите ID: ")
    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]
        with open(data_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Неверные данные!")


def redact_contact(data_tuple):
    global all_data
    symbol = "\n"
    record_id, num_data, data = data_tuple
    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Данные уже существуют!")
                return
            all_data[i] = " ".join(v)
            break
    with open(data_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена!\n")


def search_contact():
    search_data = exist_contact(0, input("Найти: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Неверные данные!")


def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates


def data_collection(num):
    while True:
        contact_id = input(f"{num}: ")
        if num in "Фамилия Имя Отчество":
            if contact_id.isalpha():
                break
        if num == "Телефон":
            if contact_id.isdigit() and len(contact_id) == 11:
                break
        contact_id = input(f"Данные неверные!\n"
                           f"Используйте только буквы алфавита."
                           f" Длина номера должна быть из 11 цифр.\n"
                           f"{num}: ")
    return contact_id


def main_menu():
    read_records()
    print("Телефонный справочник:\n"
          "1. Открыть телефонную книгу\n"
          "2. Добавить контакт\n"
          "3. Найти контакт\n"
          "4. Изменить контакт\n"
          "5. Удалить контакт\n"
          "6. Экспорт / Импорт\n"
          "7. Выход\n")
    while True:
        menu = int(input("Выбирите действие: "))
        if menu == 1:
            show_all_contacts()
        elif menu == 2:
            add_new_contact()
        elif menu == 3:
            search_contact()
        elif menu == 4:
            work = edit_menu()
            if work:
                redact_contact(work)
        elif menu == 5:
            delete_contact()
        elif menu == 6:
            exp_imp_menu()
        elif menu == 7:
            play = False
        elif menu == _:
            print("Попробуйте снова!\n")


def edit_menu():
    add_dict = {"1": "Фамилия",
                "2": "Имя",
                "3": "Отчество",
                "4": "Телефон"}
    show_all_contacts()
    record_id = input("Введите ID: ")
    if exist_contact(record_id, ""):
        print("\nРедактировать:")
        change = input("1. Фамилия\n"
                       "2. Имя\n"
                       "3. Отчество\n"
                       "4. Телефон\n"
                       "5. Выход\n")
        while True:
            if change == 1 | 2 | 3 | 4:
                return record_id, change, data_collection(add_dict[change])
            elif change == 5:
                return 0
            elif change == _:
                print("Данные не распознаны, повторите ввод.")
    else:
        print("Неверные данные")


def exp_bd(name):
    symbol = "\n"
    if not path.exists(name):
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')


def ipm_bd(name):
    global data_base
    if path.exists(name):
        data_base = name
        read_records()


def exp_imp_menu():
    print("\nМеню экспорта/импорта:")
    move = input("1. Импорт\n"
                 "2. Экспорт\n"
                 "3. Выход\n")
    while True:
        if move == 1:
            ipm_bd(input("Введите название файла: "))
        elif move == 2:
            exp_bd(input("Введите название файла: "))
        elif move == 3:
            return 0
        elif move == _:
            print("Данные не распознаны, повторите ввод.")


main_menu()
