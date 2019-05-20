"""Найдите первые десять цифр суммы следующих ста 50-значных чисел."""
answer = 0

for line in open('euler13.txt').readlines():
    answer += int(line.rstrip())

print(str(answer)[:10])
