from wakeonlan import send_magic_packet as wakeup
from re import compile, escape
from os import system
from time import sleep


output = 'Введите число команды:\n1.Включить все компьютеры из списка\n2.Создание/Добавить ПК в список\n3.Удалить ПК из списка\n4.Вывод списка MAC-addresses ПК\n9.Очистить\n0.Выход\nВвод: '
   
def wake_on_lan():
    try:
        with open('mac-addresses.txt') as file:
            mac_addresses = file.readlines()
    except FileNotFoundError:
        system('cls')
        ErrorFile()
    else:    
        for mac in mac_addresses:
            try:
                wakeup(mac.rstrip("\n"))
            except ValueError:
                system('cls')
                print('Ошибка MAC-Адреса!\nПроверьте правильность MAC-Адреса')
                sleep(5)
                system('cls')
                message()
            print('ПК ' + mac.rstrip("\n") + ' был запущен!')
        file.close()
        print("Выполнено!\n")

def add_mac():
    try:
        add = int(input('Выберете подходящий вариант: \n1)Добавить один компьютер\n2)Добивать несколько комьютеров\n'))
    except ValueError:
        system('cls')
        print('Неверное значение\n')
        add_mac()
    match add:
        case 1:
            add = input('Введите MAC-Address ПК: ')
            with open('mac-addresses.txt', 'a') as a:
                a.write(add + '\n')
            system('cls')
            a.close()
            print("Выполнено!\n")
            message()
        case 2:
            system('notepad mac-addresses.txt')
            print("Выполнено!\n")
            message()
        case _:
            system('cls')
            print('Неверное значение\n')
            add_mac()

def delete_mac():
    print('ВНИМАНИЕ!\nВводите полный MAC-Addresses.\nПри неполном вводе возможное удаление некоторых данных или собственноручно удалить из mac-addresses.txt')
    delete = input('Введите MAC-Address ПК: ')
    try:
        with open('mac-addresses.txt') as d:
            lines = d.readlines()
    except FileNotFoundError:
        system('cls')
        ErrorFile()
    else:    
        pattern = compile(escape(delete))
        with open('mac-addresses.txt', 'w') as dw:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    dw.write(line)
    system('cls')
    print("Выполнено!\n")
    dw.close()
    d.close()

def watch_list():
    try:
        with open('mac-addresses.txt') as file:
            watch = file.readlines()
    except FileNotFoundError:
        system('cls')
        ErrorFile()
    else:
        for list in watch:
            print(list.strip("\n"))

def message():
    try:
        text = int(input(output))
    except ValueError:
        system('cls')
        print('Неверное значение\n')
        message()    
    match text:
        case 1:
            wake_on_lan()
            message()
        case 2:
            add_mac()       
            message()
        case 3:
            delete_mac()
            message()
        case 4:
            watch_list()
            message()
        case 9:
            system('cls')
            message()
        case 0:
            quit()
        case _:
            system('cls')
            print('Неверное значение\n')
            message() 
    
def ErrorFile():
    print("Ошибка.\nОтсутствует файл mac-addresses.txt\n")
    try:
        Error = int(input('Создать mac-addresses.txt? \n 1)Да \n 2)Нет \n'))
    except ValueError:
        system('cls')
        print('Неверное значение\n')
        ErrorFile()
    match Error:
        case 1:
            add_mac()
        case 2:
            message()
        case _:
            system('cls')
            print('Неверное значение\n')
            ErrorFile()    

message()