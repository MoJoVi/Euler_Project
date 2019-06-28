"""
Число 197 называется круговым простым числом, потому что все
перестановки его цифр с конца в начало являются простыми числами:
197, 719 и 971.
Существует тринадцать таких простых чисел меньше 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
Сколько существует круговых простых чисел меньше миллиона?
"""
ix, primes = 0, [3]
for num in range(5, 1000000, 2):
    if primes[ix] ** 2 == num:
        ix += 1
        continue
    for div in primes[:ix + 1]:
        if not num % div:
            break
    else:
        primes.append(num)

primes_dict = {str(num): True for num in primes}
res = 1
for num in primes:
    start = str(num)
    num = str(num)[1:] + str(num)[:1]
    while start != num:
        if not primes_dict.get(num, False):
            break
        num = str(num)[1:] + str(num)[:1]
    else:
        res += 1
print(res)
