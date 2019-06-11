"""Найдите первые десять цифр суммы следующих ста 50-значных чисел."""

print(str(sum([int(line) for line in open('euler13.txt').readlines()]))[:10])
