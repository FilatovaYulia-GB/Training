#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
                