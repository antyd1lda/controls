import numpy as np
import math
from math import comb, factorial
from sympy import symbols, limit, diff, sin, exp, log, E

# 1. Матрицы и системы уравнений

A = np.array([[2, 3],
              [1, 4]])

B = np.array([[1, 2],
              [3, 1]])

print("1. Матрицы и системы уравнений")
print("A + B:")
print(A + B)

print("\nA - B:")
print(A - B)

print("\nA * B:")
print(A @ B)

det_A = np.linalg.det(A)
print("\nОпределитель A =", round(det_A, 2))

A_inverse = np.linalg.inv(A)
print("\nОбратная матрица A^-1:")
print(np.round(A_inverse, 2))

# 2. Решение системы методом Крамера
# 2x + 3y = 12
# x - y = 1

main_matrix = np.array([[2, 3],
                        [1, -1]])

right_side = np.array([12, 1])

det_main = np.linalg.det(main_matrix)

matrix_x = main_matrix.copy()
matrix_x[:, 0] = right_side
det_x = np.linalg.det(matrix_x)

matrix_y = main_matrix.copy()
matrix_y[:, 1] = right_side
det_y = np.linalg.det(matrix_y)

x = det_x / det_main
y = det_y / det_main

print("\n2. Решение системы уравнений методом Крамера")
print("x =", round(x, 2))
print("y =", round(y, 2))

# 3. Вероятность достать красный шар
red_balls = 8
blue_balls = 4
total_balls = red_balls + blue_balls

probability_red = red_balls / total_balls

print("\n3. Вероятность достать красный шар")
print("P(красный) =", probability_red)

# 4. Количество сочетаний из 7 по 3
combinations = comb(7, 3)

print("\n4. Количество способов выбрать 3 предмета из 7")
print("C(7, 3) =", combinations)

# 5. Количество перестановок 5 книг
permutations = factorial(5)

print("\n5. Количество способов расставить 5 книг")
print("P(5) =", permutations)

# 6. Вероятность достать 2 белых шара без возвращения
white_balls = 6
black_balls = 4
total = white_balls + black_balls

probability_two_white = (white_balls / total) * ((white_balls - 1) / (total - 1))

print("\n6. Вероятность достать 2 белых шара")
print("P(2 белых) =", round(probability_two_white, 4))

# 7. Предел функции
x = symbols("x")

limit_1 = limit((x**2 - 4) / (x - 2), x, 2)

print("\n7. Предел функции")
print("lim (x^2 - 4) / (x - 2), x -> 2 =", limit_1)

# 8. Первый замечательный предел
limit_2 = limit(sin(x) / x, x, 0)

print("\n8. Предел функции")
print("lim sin(x) / x, x -> 0 =", limit_2)

# 9. Производные функций
f = x**3 + 5*x**2 - 2*x + 7
g = sin(x)
h = exp(x)
k = log(x)

print("\n9. Производные функций")
print("f'(x) =", diff(f, x))
print("g'(x) =", diff(g, x))
print("h'(x) =", diff(h, x))
print("k'(x) =", diff(k, x))