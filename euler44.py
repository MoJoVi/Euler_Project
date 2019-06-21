"""Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2.
Первые десять пятиугольных чисел:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако,
их разность, 70 − 22 = 48, не является пятиугольным числом.
Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность
являются пятиугольными числами и значение D = |Pk − Pj| минимально,
и дайте значение D в качестве ответа."""
from math import fabs

next_pentagon = map(lambda n: n * (3 * n - 1) // 2, range(1, 1000000))

pentagon_list = {}
res = 0
for num in next_pentagon:
    pentagon_list[num] = 1
    for div in pentagon_list:
        summ = num - div
        dif = fabs(summ - div)
        if summ != div\
                and pentagon_list.get(dif, False)\
                and pentagon_list.get(summ, False):
            res = int(dif)
            break
    if res:
        break
print(res)
