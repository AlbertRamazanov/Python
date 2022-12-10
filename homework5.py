# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

"""my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)"""

# 2. Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# вариант человек против человека:
# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# Создайте программу для игры в ""Крестики-нолики"".
"""import random

pole = ['|', ' ', '|', ' ', '|', ' ', '|', '|', ' ', '|', ' ', '|', ' ', '|', '|', ' ', '|', ' ', '|', ' ', '|']

def print_pole():
    print(pole[0], pole[1], pole[2], pole[3], pole[4], pole[5], pole[6])
    print(pole[7], pole[8], pole[9], pole[10], pole[11], pole[12], pole[13])
    print(pole[14], pole[15], pole[16], pole[17], pole[18], pole[19], pole[20])


round = 0
ochered = random.randint(1, 2)
print(f'Чей ход: {ochered}')
player1 = 1
player2 = 2
end_game = False

# win_res = [[1, 3, 5],
#           [8, 10, 12],
#           [15, 17, 19],
#           [1, 8, 15],
#           [3, 10, 17],
#         [5, 12, 19],
#          [1, 10, 19],
#          [5, 10, 15]]

    def get_result():
    winner = ''
    if pole[1] == 'x' and pole[3] == 'x' and pole[5] == 'x':
         winner = player1
    elif pole[8] == 'x' and pole[10] == 'x' and pole[12] == 'x':
        winner = player1
    elif pole[15] == 'x' and pole[17] == 'x' and pole[19] == 'x':
        winner = player1
    elif pole[1] == 'x' and pole[8] == 'x' and pole[15] == 'x':
        winner = player1
    elif pole[3] == 'x' and pole[10] == 'x' and pole[17] == 'x':
        winner = player1
    elif pole[5] == 'x' and pole[12] == 'x' and pole[19] == 'x':
        winner = player1
    elif pole[1] == 'x' and pole[10] == 'x' and pole[19] == 'x':
        winner = player1
    elif pole[5] == 'x' and pole[10] == 'x' and pole[15] == 'x':
        winner = player1
        
    elif pole[1] == '0' and pole[3] == '0' and pole[5] == '0':
        winner = player2
    elif pole[8] == '0' and pole[10] == '0' and pole[12] == '0':
        winner = player2
    elif pole[15] == '0' and pole[17] == '0' and pole[19] == '0':
        winner = player2
    elif pole[1] == '0' and pole[8] == '0' and pole[15] == '0':
        winner = player2
    elif pole[3] == '0' and pole[10] == '0' and pole[17] == '0':
        winner = player2
    elif pole[5] == '0' and pole[12] == '0' and pole[19] == '0':
        winner = player2
    elif pole[1] == '0' and pole[10] == '0' and pole[19] == '0':
        winner = player2
    elif pole[5] == '0' and pole[10] == 'x' and pole[15] == '0':
        winner = player2

    return winner

while end_game == False:
    round +=1
    print_pole()
    print(f'Раунд: {round}')
    print(f'Чей ход: {ochered}')
    hod1 = int(input("Введите координату символа (1-я строка: 1, 3, 5, 2-я строка: 8, 10, 12, 3-я строка: 15, 17, 19): "))
    if ochered == player1:
        hod2 = input("Введите символ 'x': ")
        ind = hod1
        pole[ind] = hod2
        ochered = player2
    else:
        hod2 = input("Введите символ '0': ")
        ind = hod1
        pole[ind] = hod2
        ochered = player1

    winner = get_result()
    if winner != '':
        print_pole()
        print(winner)
        end_game = True
    else:
        end_game = False"""

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')