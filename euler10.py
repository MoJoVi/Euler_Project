"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов."""

ix, primes = 0, [3]
for num in range(5, 2000000, 2):
    if primes[ix] ** 2 == num:
        ix += 1
        continue
    for div in primes[:ix + 1]:
        if not num % div:
            break
    else:
        primes.append(num)

print(sum(primes) + 2)
