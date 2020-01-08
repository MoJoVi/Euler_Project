"""Тройка Пифагора - три натуральных числа a < b < c,
для которых выполняется равенство
a2 + b2 = c2
Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
Существует только одна тройка Пифагора, для которой
a + b + c = 1000.
Найдите произведение abc."""
res = 0
for n in range(1, 100):
    for m in range(n, n + 100):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if a + b + c == 1000:
            res = a * b * c
            break
        if a + b + c > 1000:
            break
    if res:
        print(res)
        break