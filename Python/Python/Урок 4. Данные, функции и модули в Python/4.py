#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)
#Пример:
#k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
#k=3 => 2*x^3 + 4*x^2 + 4*x + 5

import itertools
from random import randint

k = int(input("Введите степень k: "))

coefficients = [randint(0, 100) for _ in range(k + 1)]  # Генерируем коэффициенты

polynomial = []  # Здесь будем собирать многочлен

signs = itertools.cycle(['+', '-'])  # Будем чередовать знаки '+', '-', начиная с '+'

for degree in range(k, -1, -1):
    coefficient = coefficients[k - degree]
    if coefficient != 0:  # Пропускаем нули
        if degree == 0:
            polynomial.append(str(coefficient))  # Свободный член
        elif degree == 1:
            polynomial.append(f"{coefficient}*x")
        else:
            polynomial.append(f"{coefficient}*x^{degree}")

        sign = next(signs)  # Берем следующий знак из чередующихся
        if polynomial[-1] != '=0':  # Проверяем, чтобы не было лишней операции
            polynomial.append(sign)

polynomial.append('=0')  # Завершаем уравнение

with open('file.txt', 'w') as record:
    record.write(' '.join(polynomial))  # Запись в файл

print("Многочлен записан в файл 'file.txt'")