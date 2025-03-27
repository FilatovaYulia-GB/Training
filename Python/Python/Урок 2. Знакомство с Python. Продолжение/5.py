#Реализуйте алгоритм перемешивания списка.

import random

# Определение размера списка и диапазона значений
LIST_SIZE_MIN = 5
LIST_SIZE_MAX = 20
RANGE_MIN = 0
RANGE_MAX = 10

# Создание исходного списка
initial_list = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(random.randint(LIST_SIZE_MIN, LIST_SIZE_MAX))]
print(f"Исходный список:\n {initial_list}")

# Перемешивание списка
random.shuffle(initial_list)
print(f"Список после перемешивания:\n{initial_list}")