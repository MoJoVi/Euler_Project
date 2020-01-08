"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.

   3
  7 4
 2 4 6
8 5 9 3

То есть, 3 + 7 + 4 + 9 = 23.

Найдите максимальную сумму пути от вершины до основания следующего треугольника:
"""
with open('euler18.txt') as file:
    triangle = [[int(num) for num in line.split()] for line in file.readlines()]


def euler18(x, trian, ix):
    trian.pop(0)
    if trian:
        return max(euler18(x + trian[0][ix], trian[:], ix), euler18(x + trian[0][ix + 1], trian[:], ix + 1))
    else:
        return x


if __name__ == '__main__':
    print(euler18(triangle[0][0], triangle[:], 0))
