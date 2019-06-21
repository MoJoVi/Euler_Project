"""Наибольшее произведение четырех последовательных цифр в нижеприведенном
1000-значном числе равно 9 × 9 × 8 × 9 = 5832. Найдите наибольшее
произведение тринадцати последовательных цифр в данном числе."""
from functools import reduce

with open('euler8.txt'):
    s = open('euler8.txt').read().replace('\n', '')
    nums = [reduce(lambda x, y: int(x) * int(y), s[i:i+13])
            for i in range(len(s) - 13)]
print(max(nums))
