"""
Первые два последовательные числа, каждое из которых имеет два
отличных друг от друга простых множителя:

14 = 2 × 7
15 = 3 × 5

Первые три последовательные числа, каждое из которых имеет три
отличных друг от друга простых множителя:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Найдите первые четыре последовательных числа, каждое из которых
имеет четыре отличных друг от друга простых множителя.
Каким будет первое число?
"""
from Euler_Project.euler027 import is_prime

primes = [n for n in range(2, 1000) if is_prime(n)]


def prime_factorization(num):
    count = 0
    for div in [n for n in primes if n < num]:
        count += 1 if not num % div else 0
        while not num % div:
            num //= div
        if num == 1:
            break
    return count == 4


if __name__ == '__main__':
    nums, num = list(), 646
    while len(nums) < 4:
        if prime_factorization(num):
            nums.append(num)
        else:
            nums = list()
        num += 1
    print(nums)
