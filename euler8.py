# Наибольшее произведение четырех последовательных цифр в нижеприведенном
# 1000-значном числе равно 9 × 9 × 8 × 9 = 5832. Найдите наибольшее
# произведение тринадцати последовательных цифр в данном числе.
from functools import reduce

s = open('euler8.txt').read().replace('\n', '')
numlist = []
answer = 0

for i in s:
    numlist.append(int(i))

    if len(numlist) == 13:
        summ = reduce(lambda x, y: x * y, numlist)

        if summ > answer:
            answer = summ
        numlist.pop(0)

print(answer)
