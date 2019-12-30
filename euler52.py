"""
Найдите такое наименьшее положительное целое число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.
"""
print(next(x for x in range(10, 10**6) if sorted(str(2 * x)) == sorted(str(3 * x)) == sorted(str(4 * x)) == sorted(str(5 * x)) == sorted(str(6 * x))))
