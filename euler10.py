"""Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов."""
n = 0
primes = [3]
for i in range(5, 200000000, 2):
    if primes[n] ** 2 == i:
        n += 1
        continue
    for k in primes[:n + 1]:
        if i % k == 0:
            break
        elif k == primes[n]:
            primes.append(i)
            break
print(sum(primes) + 2, len(primes) / len(list(range(2000000))))
