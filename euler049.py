"""
Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый
член возрастает на 3330, необычна в двух отношениях:
(1) каждый из трех членов является простым числом,
(2) все три четырехзначные числа являются перестановками друг
друга.

Не существует арифметических прогрессий из трех однозначных,
двухзначных и трехзначных простых чисел, демонстрирующих это
свойство. Однако, существует еще одна четырехзначная возрастающая
арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена
этой прогрессии?
"""
from Euler_Project.euler027 import is_prime

for num in range(1488, 10000 - 6660):
    str_num = sorted(str(num))
    for n in range(num, num + 7000, 3330):
        if not is_prime(n) or sorted(str(n)) != str_num:
            break
    else:
        print(num, num + 3330, num + 6660, sep='')
        break