"""
Кристиан Гольдбах показал, что любое нечетное составное число можно
записать в виде суммы простого числа и удвоенного квадрата.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

Оказалось, что данная гипотеза неверна.

Каково наименьшее нечетное составное число, которое нельзя записать в
виде суммы простого числа и удвоенного квадрата?
"""
from euler007 import is_prime


def checker(num):
    first_nums = [2] + [n for n in range(3, num - 1, 2) if is_prime(n)]
    for first in first_nums:
        for second in range(int(num ** 0.5)):
            if first + 2 * (second ** 2) == num:
                return False
    return True


for num in (num for num in range(11, 10 ** 4, 2) if not is_prime(num)):
    if checker(num):
        print(num)
        break
