#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)

mass = [1.1, 1.2, 3.1, 5, 10.01]
mass1 = []
for i in range(len(mass)):
    if mass[i] % 1 != 0:
        mass1.append(mass[i])
mass2 = [round(mass1[i] % 1, 2) for i in range(len(mass1))]
print(f"{mass2} => {max(mass2) - min(mass2)}")
