"""Найдите первые десять цифр суммы следующих ста 50-значных чисел."""

print(str(sum([int(line) for line in open('euler013.txt').readlines()]))[:10])
