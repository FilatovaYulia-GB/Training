#Создайте программу для игры с конфетами человек против человека.
#Условие игры: На столе лежит 117 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = 117  # Начальное количество конфет (можно заменить на ввод пользователя)

# Жеребьевка
flag = randint(0, 1)  
if flag == 0:
    turn = player1
else:
    turn = player2
print(f"Первым ходит {turn}")

counter1 = 0  # Счетчик конфет первого игрока
counter2 = 0  # Счетчик конфет второго игрока

while value > 0:
    if turn == player1:
        k = min(input_dat(player1), value)  # Забираем не больше оставшихся конфет
        counter1 += k
        value -= k
        turn = player2
        p_print(player1, k, counter1, value)
    else:
        k = min(input_dat(player2), value)  # Забираем не больше оставшихся конфет
        counter2 += k
        value -= k
        turn = player1
        p_print(player2, k, counter2, value)

if turn == player1:
    print(f"Выиграл {player2}")
else:
    print(f"Выиграл {player1}")
    