import os

import pandas as pd


def action_choice():
    # Выбор действия
    while True:
        print("Телефонный справочник\n1 - чтение\n2 - добавление\n3 - выход\n")
        new_input = input("Выберите действие: ")
        try:
            new_input = int(new_input)
            if new_input not in [1,2,3]:
                raise ValueError
            return new_input
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Такого действия нету: {new_input}")


def adding_values(handbook):
    # Добавление номера в справочник
    name_input = input("Введите имя: ")
    number_input = input("Введите номер: ")
    city_input = input("Введите город: ")

    new_contact = pd.DataFrame({'name':[name_input], 'number':[number_input], 'city':[city_input]})
    handbook = pd.concat([handbook, new_contact], ignore_index=True)
    return handbook
        

def interface(handbook):
    while True:
        new_input = action_choice()
        if new_input == 1:
            # чтение
            if len(handbook)==0:
                print("Справочник пуст")
            else:
                print(handbook)
                enter = input("Нажмите Enter для продолжения")

        elif new_input == 2:
            # добавление
            handbook = adding_values(handbook)
            print(handbook)
            enter = input("Нажмите Enter для продолжения")

        elif new_input == 3:
            print("Выход")
            break
    return handbook

def form_selection():
    while True:
        print("Телефонный справочник")
        print("Доступные форматы для чтения\n1 - csv\n2 - exel\n3 - txt\n4 - html\n5 - json\n")
        new_input = input("Выберите формат: ")
        if new_input not in ['1', '2', '3', '4', '5']:
            print(f"Такого действия нету: {new_input}")
            continue
        else:
            return new_input
