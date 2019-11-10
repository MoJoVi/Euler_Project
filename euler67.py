"""
Начиная с вершины представленного ниже треугольника и переходя к прилежащим
числам в следующем ряду, максимальная возможная сумма пройденных чисел по
пути от вершины до основания равна 23.
   3
  7 4
 2 4 6
8 5 9 3

Т.е., 3 + 7 + 4 + 9 = 23.
Найти максимальную сумму при переходе от вершины до основания треугольника,
представленного текстовым файлом  triangle.txt, в котором содержится
треугольник с одной сотней строк.
"""
with open('triangle.txt') as file:
    triangle = [[int(num) for num in line.split()] for line in file.readlines()]

for ix in range(1, len(triangle)):
    for elem_ix in range(len(triangle[ix - 1])):
        triangle[ix][elem_ix] += max(triangle[ix - 1][elem_ix], triangle[ix - 1][elem_ix - 1])

print(max(triangle[-1]))
