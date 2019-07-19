"""
Перестановка - это упорядоченная выборка объектов. К примеру, 3124 является
одной из возможных перестановок из цифр 1, 2, 3 и 4. Если все перестановки
приведены в порядке возрастания или алфавитном порядке, то такой порядок
будем называть словарным. Словарные перестановки из цифр 0, 1 и 2
представлены ниже:
012   021   102   120   201   210
Какова миллионная словарная перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?
"""
from itertools import permutations as p

print(next((num for ix, num in enumerate(''.join(i) for i in p('0123456789'))
            if ix == 999999)))
