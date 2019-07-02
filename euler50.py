"""
Простое число 41 можно записать в виде суммы шести последовательных
простых чисел:
41 = 2 + 3 + 5 + 7 + 11 + 13
Это - самая длинная сумма последовательных простых чисел, в результате
которой получается простое число меньше одной сотни.
Самая длинная сумма последовательных простых чисел, в результате которой
получается простое число меньше одной тысячи, содержит 21 слагаемое и
равна 953.
Какое из простых чисел меньше одного миллиона можно записать в виде
суммы наибольшего количества последовательных простых чисел?
"""
ix, primes = 1, [2, 3]
for num in range(5, 1000000, 2):
    if primes[ix] ** 2 == num:
        ix += 1
        continue
    for div in primes[:ix + 1]:
        if not num % div:
            break
    else:
        primes.append(num)

k = 0
for max_slice, num in enumerate(primes):
    k += num
    if k >= 1000000:
        break

max_len = 0
res = 0
for max_ix in range(max_slice, 0, -1):
    for first in range(max_slice):
        slice = primes[first: max_ix]
        sum_slice = sum(slice)
        len_slice = len(slice)
        if sum_slice >= 1000000:
            break
        elif len_slice > max_len and sum_slice in primes:
            max_len, res = len_slice, sum_slice

print(res)
