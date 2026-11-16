from math import factorial, comb
from fractions import Fraction

books = 6
permutations = factorial(books)

print("1. Перестановки")
print("Количество способов расставить 6 книг:")
print(permutations)

students = 10
positions = 3

placements = factorial(students) // factorial(students - positions)

print("\n2. Размещения")
print("Количество способов выбрать 3 человека из 10 с учётом порядка:")
print(placements)

items = 9
chosen = 4

combinations = comb(items, chosen)

print("\n3. Сочетания")
print("Количество способов выбрать 4 предмета из 9 без учёта порядка:")
print(combinations)

favorable_outcomes = 2  # числа 5 и 6
total_outcomes = 6

probability_cube = Fraction(favorable_outcomes, total_outcomes)

print("\n4. Вероятность выпадения числа больше 4")
print("P(число больше 4) =", probability_cube)
print("В десятичной записи:", float(probability_cube))

red_balls = 7
blue_balls = 5
total_balls = red_balls + blue_balls

probability_red = Fraction(red_balls, total_balls)

print("\n5. Вероятность достать красный шар")
print("P(красный шар) =", probability_red)
print("В десятичной записи:", float(probability_red))

white_balls = 8
black_balls = 4
total_balls_2 = white_balls + black_balls

probability_two_white = Fraction(
    white_balls * (white_balls - 1),
    total_balls_2 * (total_balls_2 - 1)
)

print("\n6. Вероятность достать 2 белых шара")
print("P(2 белых шара) =", probability_two_white)
print("В десятичной записи:", float(probability_two_white))

total_cards = 36
aces = 4
red_cards = 18
spades = 9

probability_ace = Fraction(aces, total_cards)
probability_red = Fraction(red_cards, total_cards)
probability_spade = Fraction(spades, total_cards)

print("\n7. Вероятность с картами")
print("P(туз) =", probability_ace)
print("P(красная карта) =", probability_red)
print("P(пиковая масть) =", probability_spade)
