# Найдите первые десять цифр суммы следующих ста 50-значных чисел.
summ = 0

for line in open('euler13.txt').readlines():
    summ += int(line.rstrip())

print(str(summ)[:10])
