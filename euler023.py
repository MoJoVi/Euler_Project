"""Идеальным числом называется число, у которого сумма его делителей
равна самому числу. Например, сумма делителей числа 28 равна
1 + 2 + 4 + 7 + 14 = 28, что означает, что число 28 является
идеальным числом.
Число n называется недостаточным, если сумма его делителей меньше n,
и называется избыточным, если сумма его делителей больше n.
Так как число 12 является наименьшим избыточным числом
(1 + 2 + 3 + 4 + 6 = 16), наименьшее число, которое может быть записано
как сумма двух избыточных чисел, равно 24. Используя математический
анализ, можно показать, что все целые числа больше 28123 могут быть записаны
как сумма двух избыточных чисел. Эта граница не может быть уменьшена
дальнейшим анализом, даже несмотря на то, что наибольшее число, которое
не может быть записано как сумма двух избыточных чисел, меньше этой границы.
Найдите сумму всех положительных чисел, которые не могут быть записаны как
сумма двух избыточных чисел."""
from math import sqrt

abund = []

for num in range(12, 28123):
    nums = set()
    nums.add(1)
    for div in range(2, int(sqrt(num)) + 1):
        if num % div == 0:
            nums.add(div)
            nums.add(num // div)
    if sum(nums) > num:
        abund.append(num)

abound_sums = set()
for i in abund[:len(abund) // 2]:
    for k in abund:
        num = i + k
        if num in abound_sums:
            continue
        elif num > 28123:
            break
        abound_sums.add(num)

print(sum(num for num in list(range(28124)) if num not in abound_sums))
