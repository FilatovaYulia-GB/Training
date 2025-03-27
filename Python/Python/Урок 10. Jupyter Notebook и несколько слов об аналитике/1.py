# дана функция f(x) = sin(x)^2 - cos(x)^2
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

from sympy import symbols, sin, cos, diff, plot, solve, pi, Interval, S
from sympy.calculus.util import continuous_domain, function_range
import numpy as np
import matplotlib.pyplot as plt

# Определение переменной x
x = symbols('x')

# Определение функции f(x)
f = sin(x)**2 - cos(x)**2

# Упростим функцию (по тригонометрической формуле)
f = -cos(2*x)

# 1. Найдем корни функции (решения f(x) = 0)
roots = solve(f, x, domain=S.Reals)

print("Корни функции:", roots)

# 2-3. Найдем интервалы возрастания и убывания
df_dx = diff(f, x)  # Производная = 2*sin(2*x)

# Найдем критические точки (где производная = 0)
critical_points = solve(df_dx, x, domain=S.Reals)
print("Критические точки:", critical_points)

# Определим знак производной на интервалах
# Для этого создадим тестовые точки между критическими точками
test_points = []
for i in range(len(critical_points)-1):
    test_point = (critical_points[i] + critical_points[i+1])/2
    test_points.append(test_point)

# Добавим точки до первой и после последней критической точки
test_points.insert(0, critical_points[0] - pi/2)
test_points.append(critical_points[-1] + pi/2)

# Определим возрастание/убывание
increasing = []
decreasing = []
for point in test_points:
    val = df_dx.subs(x, point)
    if val > 0:
        increasing.append(point)
    elif val < 0:
        decreasing.append(point)

print("Функция возрастает на интервалах, содержащих точки:", increasing)
print("Функция убывает на интервалах, содержащих точки:", decreasing)

# 4. Построим график
p = plot(f, (x, -2*pi, 2*pi), 
        xlabel='$x$', 
        ylabel='$f(x)$', 
        title=r'$f(x)=\sin^2(x)-\cos^2(x)$',
        show=False)
p.show()

# 5. Найдем вершины (экстремумы)
# Вторая производная
d2f_dx2 = diff(df_dx, x)
vertices = []
for cp in critical_points:
    val = d2f_dx2.subs(x, cp)
    if val > 0:
        typ = "минимум"
    elif val < 0:
        typ = "максимум"
    else:
        typ = "перегиб"
    vertices.append((cp, f.subs(x, cp), typ))
    
print("Вершины (экстремумы):", vertices)

# 6-7. Промежутки, где f > 0 и f < 0
# Найдем нули функции
zeros = solve(f, x, domain=S.Reals)

# Определим знак функции между нулями
positive_intervals = []
negative_intervals = []

for i in range(len(zeros)-1):
    test_point = (zeros[i] + zeros[i+1])/2
    if f.subs(x, test_point) > 0:
        positive_intervals.append((zeros[i], zeros[i+1]))
    else:
        negative_intervals.append((zeros[i], zeros[i+1]))

print("Функция положительна на интервалах:", positive_intervals)
print("Функция отрицательна на интервалах:", negative_intervals)