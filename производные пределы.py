from sympy import symbols, limit, diff, sin, exp, log, oo

x = symbols("x")

# 1. Пределы

limit_1 = limit((x**2 - 9) / (x - 3), x, 3)
limit_2 = limit(sin(5*x) / x, x, 0)
limit_3 = limit((3*x**2 + 2*x - 1) / (6*x**2 - x + 4), x, oo)

print("1. Пределы")
print("lim (x^2 - 9) / (x - 3), x -> 3 =", limit_1)
print("lim sin(5x) / x, x -> 0 =", limit_2)
print("lim (3x^2 + 2x - 1) / (6x^2 - x + 4), x -> infinity =", limit_3)

# 2. Производные

f = 4*x**3 - 5*x**2 + 2*x - 7
g = sin(x)
h = exp(x)
k = log(x)
m = (3*x**2 + 1)**4

print("\n2. Производные")
print("f(x) =", f)
print("f'(x) =", diff(f, x))

print("\ng(x) =", g)
print("g'(x) =", diff(g, x))

print("\nh(x) =", h)
print("h'(x) =", diff(h, x))

print("\nk(x) =", k)
print("k'(x) =", diff(k, x))

print("\nm(x) =", m)
print("m'(x) =", diff(m, x))

# 3. Значение производной в точке

function = x**2 + 3*x
derivative = diff(function, x)
value_at_point = derivative.subs(x, 2)

print("\n3. Значение производной")
print("f(x) =", function)
print("f'(x) =", derivative)
print("f'(2) =", value_at_point)