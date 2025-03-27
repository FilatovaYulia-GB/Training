

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def bot_turn(value):
    k = randint(1, 28)
    return k

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 1)  # Жеребьевка: 0 - первый игрок, 1 - бот
if flag == 0:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

counter1 = 0  # Счетчик конфет первого игрока
counter2 = 0  # Счетчик конфет бота

while value > 0:
    if flag == 0:
        k = min(input_dat(player1), value)  # Игрок берет не больше оставшихся конфет
        counter1 += k
        value -= k
        flag = 1
        p_print(player1, k, counter1, value)
    else:
        k = min(bot_turn(value), value)  # Бот берет не больше оставшихся конфет
        counter2 += k
        value -= k
        flag = 0
        p_print(player2, k, counter2, value)

if flag == 0:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
    