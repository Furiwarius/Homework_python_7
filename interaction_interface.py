import os

import pandas as pd


def action_choice():
    # Выбор действия
    while True:
        print("Телефонный справочник\n1 - чтение\n2 - добавление\n3 - удалить\n4 - изменить\n5 - выход\n")
        new_input = input("Выберите действие: ")
        try:
            new_input = int(new_input)
            if new_input not in range(1, 6):
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


def deleting_number(handbook):
    # удаление
    while True:
        print(f"{handbook}\n")
        new_input = input("Укажите индекс или имя контакта, который хотите удалить\nили 'отмена' для отмены действия: ")

        if new_input.lower()=='отмена':
                print("Отмена\n")
                return handbook
        # если введен индекс
        if new_input.isdigit():
            if len(handbook)<=int(new_input):
                print("Вы ввели неверный индекс контакта\n")
                continue
            else:
                handbook.drop(labels=[int(new_input)], axis=0, inplace=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Номер удален\n")
                enter = input("\nНажмите Enter для продолжения\n")
                return handbook
        # если введено имя
        else:
            if new_input in list(handbook['name']):
                index = list(handbook['name']).index(new_input)
                handbook.drop(labels=[index], axis=0, inplace=True)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Номер удален\n")
                enter = input("\nНажмите Enter для продолжения\n")
                return handbook
            else:
                print("Контакта под таким именем у вас нет\n")
                enter = input("Нажмите Enter для продолжения\n")
                
            


def contact_change(handbook):
    # изменение
    while True:
        print(f"{handbook}\n")
        contact = input("Укажите индекс или имя контакта, который хотите изменить\nили 'отмена' для отмены действия: ")
        if contact.lower()=='отмена':
                print("Отмена\n")
                return handbook 

        # если введен индекс контакта
        if contact.isdigit():
            if len(handbook)<=int(contact):
                print("Вы ввели неверный индекс контакта\n")
                continue
            else:
                print("\n1 - имя\n2 - номер\n3 - город\n")
                data = input("Выберите, что вы хотите изменить: ")
                if data not in ['1','2','3']:
                    print("\nВы ввели непрвильную команду\n")
                    continue
                else:
                    new_value = input("Введите новые данные: ")
                    handbook[['name', 'number', 'city'][int(data)-1]][int(contact)] = new_value
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Контакт изменен\n")
                    enter = input("\nНажмите Enter для продолжения\n")
                    return handbook

        # если введено имя
        else:
            if contact in list(handbook['name']):
                print("\n1 - имя\n2 - номер\n3 - город\n")
                data = input("Выберите, что вы хотите изменить: ")
                if data not in ['1','2','3']:
                    print("\nВы ввели непрвильную команду\n")
                    continue
                else:
                    new_value = input("Введите новые данные: ")
                index = list(handbook['name']).index(contact)
                handbook[['name', 'number', 'city'][int(data)-1]][index] = new_value
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Контакт изменен\n")
                enter = input("\nНажмите Enter для продолжения\n")
                return handbook
            else:
                print("Контакта под таким именем у вас нет\n")
                enter = input("Нажмите Enter для продолжения\n")


def interface(handbook):
    while True:
        new_input = action_choice()
        if new_input == 1:
            # чтение
            if len(handbook)==0:
                print("Справочник пуст")
            else:
                print(f"\n{handbook}\n")
                enter = input("Нажмите Enter для продолжения\n")

        elif new_input == 2:
            # добавление
            handbook = adding_values(handbook)
            print(f"\n{handbook}\n")
            enter = input("Нажмите Enter для продолжения\n")
        elif new_input == 3:
            # удаление 
            handbook = deleting_number(handbook)
        elif new_input == 4:
            handbook = contact_change(handbook)
        elif new_input == 5:
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
