"""
Число 3797 обладает интересным свойством. Будучи само по себе простым
числом, из него можно последовательно выбрасывать цифры слева направо,
число же при этом остается простым на каждом этапе: 3797, 797, 97, 7.
Точно таким же способом можно выбрасывать цифры справа налево:
3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно
выбрасывать цифры как справа налево, так и слева направо,
но числа при этом остаются простыми.
ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
"""
from math import sqrt
import time


def is_prime(num):
    if num is 1:
        return False
    for div in range(2, int(sqrt(num)) + 1):
        if not num % div:
            return False
    return True


def tran(num):
    num = str(num)
    for ix in range(len(num)):
        if not is_prime(int(num[ix:])) or not is_prime(int(num[:ix + 1])):
            return False
    return True


start = time.time()
res = (num for num in range(11, 1000000, 2) if tran(num))
print(sum(next(res) for i in range(11)))
