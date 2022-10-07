import random as r
import time as t

print('Bienvenido al horoscopo')

def menu():
    print('#######################')
    print('Selecciona el numero correspodiente a tu signo')
    print('1 Aries') 
    print('2 Tauro') 
    print('3 Géminis') 
    print('4 Cáncer') 
    print('5 Leo')
    print('6 Virgo') 
    print('7 Libra') 
    print('8 Escorpio') 
    print('9 Sagitario') 
    print('10 Capricornio') 
    print('11 Acuario')
    print('12 Piscis')
    print('13 Color de la suerte')
    print('0 Salir')    
    print('#######################')

def file_reader(archivo):
    file = open(archivo , 'r', encoding='UTF-8')
    for line in file:
        print(line)
    t.sleep(3)

user_input = ''

colors= ['azul', 'rojo', 'verde', 'amarillo', 'negro', 'rosa']

while user_input != '0':
    menu()

    user_input = input()
    if user_input == '1':
        file = file_reader('signs/aries.txt')
    elif user_input == '2':
        file = file_reader('signs/taurus.txt')
    elif user_input == '3':
        file = file_reader('signs/gemini.txt')
    elif user_input == '4':
        file = file_reader('signs/cancer.txt')
    elif user_input == '5':
        file = file_reader('signs/leo.txt')
    elif user_input == '6':
        file = file_reader('signs/virgo.txt')
    elif user_input == '7':
        file = file_reader('signs/libra.txt')
    elif user_input == '8':
        file = file_reader('signs/scorpio.txt')
    elif user_input == '9':
        file = file_reader('signs/sagittarius.txt')
    elif user_input == '10':
        file = file_reader('signs/capricornus.txt') 
    elif user_input == '11':
        file = file_reader('signs/aquarius.txt') 
    elif user_input == '12':
        file = file_reader('signs/pisces.txt') 
    elif user_input == '13':
        print('Tu color de la suerte es:', r.choice(colors))
        t.sleep(3)
    elif user_input == '0':
        print('Pulsaste salir. Chau Chau')
        t.sleep(3)
    else:
        print('Opcion invalida')











