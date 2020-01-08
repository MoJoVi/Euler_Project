"""Выписав первые шесть простых чисел, получим
2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?"""


def is_prime(num):
    for div in range(3, int(num ** 0.5) + 1, 2):
        if num % div == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    count = 1
    primes = iter(num for num in range(3, 200000, 2) if is_prime(num))
    while count < 10001:
        count += 1
        res = next(primes)
        print(res)
    print(res)
