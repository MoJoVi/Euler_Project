"""В таблице 20×20 (внизу) четыре числа на одной диагонали выделены красным.

Произведение этих чисел 26 × 63 × 78 × 14 = 1788696.
Каково наибольшее произведение четырех подряд идущих чисел в таблице
20×20, расположенных в любом направлении (вверх, вниз, вправо, влево или
по диагонали)?"""
from functools import reduce

table = []
res = []

for line in open('euler11.txt').readlines():
    nums = [int(num) for num in line.replace('\n', '').split(' ')]
    table.append(nums)

for line in range(20):
    for col in range(20):
        res.append(reduce(lambda x, y: x * y, table[col][line: line + 4]))

for line in range(17):
    for col in range(20):
        res.append(reduce(lambda x, y: x * y,
                          [table[col][n] for n in range(line, line + 4)]))
    for col in range(17):
        res.append(reduce(lambda x, y: x * y,
                          [table[col + n][line + n] for n in range(4)]))

    for col in range(3, 20):
        res.append(reduce(lambda x, y: x * y,
                          [table[line + n][col - n] for n in range(4)]))

print(max(res))
