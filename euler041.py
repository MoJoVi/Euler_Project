"""
Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до
n используется в нем ровно один раз. К примеру, 2143 является 4-значным
пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?
"""
from itertools import permutations
from euler007 import is_prime

res = 0
for i in range(9):
    for num in permutations('987654321'[i:], 9 - i):
        num = int(''.join(num))
        if is_prime(num) and num % 2:
            res = num
            break
    if res:
        break

print(res)
