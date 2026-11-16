import matplotlib.pyplot as plt


#функций
def f(x):
    return 2 * x + 1


def g(x):
    return x ** 2 - 4


def h(x):
    return abs(x) - 2


def main():
    print("КОНТРОЛЬНАЯ РАБОТА: ФУНКЦИИ И ГРАФИКИ")
    print("=" * 50)

    #1 значения
    print("\n1. Таблица значений")
    print(f"{'x':>5} | {'2x + 1':>10} | {'x² - 4':>10} | {'|x| - 2':>10}")
    print("-" * 47)

    for x in range(-3, 4):
        print(f"{x:>5} | {f(x):>10} | {g(x):>10} | {h(x):>10}")

    # 2 заранее написанные ответы
    print("\n2. Свойства функций")

    print("\nf(x) = 2x + 1")
    print("Область определения: все действительные числа.")
    print("Область значений: все действительные числа.")
    print("Нуль функции: x = -0.5.")
    print("Пересечение с Oy: (0; 1).")
    print("Строго возрастает на всей числовой прямой.")
    print("Наибольшего и наименьшего значений нет.")

    print("\ng(x) = x² - 4")
    print("Область определения: все действительные числа.")
    print("Область значений: [-4; +∞).")
    print("Нули функции: x = -2 и x = 2.")
    print("Пересечение с Oy: (0; -4).")
    print("Убывает на (-∞; 0], возрастает на [0; +∞).")
    print("Наименьшее значение: -4 при x = 0.")

    print("\nh(x) = |x| - 2")
    print("Область определения: все действительные числа.")
    print("Область значений: [-2; +∞).")
    print("Нули функции: x = -2 и x = 2.")
    print("Пересечение с Oy: (0; -2).")
    print("Убывает на (-∞; 0], возрастает на [0; +∞).")
    print("Наименьшее значение: -2 при x = 0.")

    # 3. подготовление точек
    x_values = [i / 100 for i in range(-500, 501)]

    functions = [
        ("f(x) = 2x + 1", f, [-0.5], "royalblue"),
        ("g(x) = x² - 4", g, [-2, 2], "forestgreen"),
        ("h(x) = |x| - 2", h, [-2, 2], "darkorange"),
    ]

    # 4. стрение графиков
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for ax, (title, function, roots, color) in zip(axes, functions):
        y_values = [function(x) for x in x_values]

        ax.plot(x_values, y_values, color=color, label=title)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axvline(0, color="black", linewidth=0.8)

        ax.scatter(
            roots, [0] * len(roots),
            color="red", zorder=5, label="Нули функции"
        )
        ax.scatter(
            [0], [function(0)],
            color="purple", zorder=5, label="Пересечение с Oy"
        )

        ax.set_title(title)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, alpha=0.4)
        ax.legend(fontsize=8)

    fig.suptitle("Контрольная работа: функции и графики")
    fig.tight_layout()

    fig.savefig("grafiki_funktsiy.png", dpi=150)
    print("\nГрафики сохранены в файл grafiki_funktsiy.png.")

    plt.show()


if __name__ == "__main__":
    main()
