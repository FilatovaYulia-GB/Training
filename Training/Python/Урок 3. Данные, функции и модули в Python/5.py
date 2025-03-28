#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#*Пример:*
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

mass = [0]
userNumber = int(input('Введите число: '))
for j in range(1, userNumber + 1):
    mass.append(Fibonacci(j))
    mass.insert(0, NegaFibonacci(j))
print(mass)
