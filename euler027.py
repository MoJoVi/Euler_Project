"""
Эйлер опубликовал свою замечательную квадратичную формулу:
n^2+n+41

Оказалось, что согласно данной формуле можно получить 40 простых чисел,
последовательно подставляя значения 0≤n≤39. Однако, при n=40,
402+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно, при n=41,
412+41+41 делится на 41 без остатка.

При помощи компьютеров была найдена невероятная формула n^2−79n+1601,
согласно которой можно получить 80 простых чисел для последовательных
значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:
n^2+an+b, где |a|<1000 и |b|≤1000

Найдите произведение коэффициентов a и b квадратичного выражения,
согласно которому можно получить максимальное количество простых чисел
для последовательных значений n, начиная со значения n=0.
"""
from math import ceil
import time


def is_prime(num):
    num = abs(num)
    for div in range(2, ceil(num ** 0.5)+1):
        if not num % div and num != div:
            return False
    return True


if __name__ == '__main__':
    limit = 80 ** 2 + 1000 * 80 + 1000 + 1
    primes = {num: True for num in range(3, limit, 2) if is_prime(num)}
    long = [0, 0]  # 0 - длина максимальной последовательности, 1 - произведение коэфициентов
    for a in range(-999, 1000):
        for b in range(-1000, 1000):
            long_num = [0, a * b]
            for num in range(0, 100):
                if primes.get(abs(num ** 2 + a * num + b), False):
                    long_num[0] += 1
                else:
                    break
            long = max(long_num, long)  # питон сравнивает числовые
            # последовательности по первому числу

    print(long[1])
