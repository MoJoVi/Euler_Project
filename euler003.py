"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""
n = 600851475143
div = (i for i in range(2, int(n ** 0.5)) if n % i == 0)
x = next(div)

while n != x:
    n //= x
    x = next(div)

print(n)
