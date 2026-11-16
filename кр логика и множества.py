def main():

    print("Задание 1. Логические операции")
    a, b = True, False
    print("A =", a, "; B =", b)
    print("НЕ A:", not a)
    print("A И B:", a and b)
    print("A ИЛИ B:", a or b)
    print("A -> B:", (not a) or b)
    print("A <-> B:", a == b)


    print("\nЗадание 2. Таблица истинности")
    print("A B | F = (A И B) ИЛИ НЕ A")
    for a in (False, True):
        for b in (False, True):
            f = (a and b) or (not a)
            print(f"{int(a)} {int(b)} | {int(f)}")


    print("\nЗадание 3. Операции над множествами")
    x = {1, 2, 3, 4, 5}
    y = {4, 5, 6, 7}
    print("X =", sorted(x))
    print("Y =", sorted(y))
    print("Объединение X | Y:", sorted(x | y))
    print("Пересечение X & Y:", sorted(x & y))
    print("Разность X - Y:", sorted(x - y))
    print("Разность Y - X:", sorted(y - x))
    print("Симметрическая разность X ^ Y:", sorted(x ^ y))


    print("\nЗадание 4. Принадлежность и включение")
    u = set(range(1, 11))
    z = {2, 3}
    print("Число 3 принадлежит X:", 3 in x)
    print("Z =", sorted(z))
    print("Z является подмножеством X:", z <= x)
    print("Количество элементов X:", len(x))
    print("Универсальное множество U:", sorted(u))
    print("Дополнение X относительно U:", sorted(u - x))


    print("\nЗадание 5. Законы де Моргана")
    law_1 = (u - (x | y)) == ((u - x) & (u - y))
    law_2 = (u - (x & y)) == ((u - x) | (u - y))
    print("U - (X | Y) == (U - X) & (U - Y):", law_1)
    print("U - (X & Y) == (U - X) | (U - Y):", law_2)


if __name__ == "__main__":
    main()
