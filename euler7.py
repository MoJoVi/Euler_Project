"""Выписав первые шесть простых чисел, получим
2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?"""
from math import sqrt
n = 1  # Prime number counter
i = 1
while n < 10001:
    i += 2
    for k in range(3, int(sqrt(i)) + 1):
        if i % k == 0:
            break
    else:
        n += 1
print(i)
