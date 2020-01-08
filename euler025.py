"""Последовательность Фибоначчи определяется рекурсивным правилом:
Fn = Fn−1 + Fn−2, где F1 = 1 и F2 = 1.
Таким образом, первые 12 членов последовательности равны:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
Двенадцатый член F12 - первый член последовательности,
который содержит три цифры.
Каков порядковый номер первого члена последовательности Фибоначчи,
содержащего 1000 цифр?"""
from euler002 import fib

f = fib()
answer = count = 0

while len(str(answer)) < 1000:
    answer = next(f)
    count += 1
    
print(count)