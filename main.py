from wakeonlan import send_magic_packet as wakeup
from time import sleep
from re import compile, escape
from os import system


output = 'Введите число команды:\n1.Включить все компьютеры из списка\n2.Создание/Добавить ПК в список\n3.Удалить ПК из списка\n4.Вывод списка MAC-addresses ПК\n9.Очистить\n0.Выход\nВвод: '
   
def wake_on_lan():
    try:
        with open('mac-addresses.txt') as file:
            mac_addresses = file.readlines()
    except FileNotFoundError:
        system('cls')
        print("Не удалось найти информацию о компьютерах.\nВозможно отсутствует файл или не был создан!\n")
        message()
    else:    
        for mac in mac_addresses:
            wakeup(mac.rstrip("\n"))
            print('ПК ' + mac.rstrip("\n") + ' был запущен!')
            sleep(5)
        file.close()
        print("Выполнено!\n")

def add_mac():
    add = input('Введите MAC-Address ПК: ')
    with open('mac-addresses.txt', 'a') as a:
        a.write(add + '\n')
    system('cls')
    print("Выполнено!\n")
    a.close()

def delete_mac():
    print('ВНИМАНИЕ!\nВводите полный MAC-Addresses.\nПри неполном вводе возможное удаление некоторых данных')
    delete = input('Введите MAC-Address ПК: ')
    try:
        with open('mac-addresses.txt') as d:
            lines = d.readlines()
    except FileNotFoundError:
        system('cls')
        print("Не удалось найти информацию о компьютерах.\nВозможно отсутствует файл или не был создан!\n")
        message()
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
        print("Не удалось найти информацию о компьютерах.\nВозможно отсутствует файл или не был создан!\n")
        message()
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
    if text == 1:
        wake_on_lan()
        message()
    elif text == 2:
        add_mac()       
        message()
    elif text == 3:
        delete_mac()
        message()
    elif text == 4:
        watch_list()
        message()
    elif text == 9:
        system('cls')
        message()
    elif text == 0:
        quit()
    else:
        system('cls')
        print('Неверное значение\n')
        message() 

message()