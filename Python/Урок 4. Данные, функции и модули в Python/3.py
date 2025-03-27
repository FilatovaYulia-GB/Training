# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# Вводим последовательность чисел
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")

# Список для хранения неповторяющихся элементов
new_lst = []

# Добавляем уникальные элементы в новый список
for i in lst:
    if i not in new_lst:
        new_lst.append(i)

# Выводим результат
print(f"Список из неповторяющихся элементов: {new_lst}")