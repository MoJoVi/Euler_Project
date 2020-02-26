"""
Число 10 можно записать в виде суммы простых чисел ровно
пятью различными способами:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

Какое наименьшее число можно записать в виде суммы простых
чисел по крайней мере пятью тысячами различных способов?
"""
from Euler_Project.euler027 import is_prime


def combs(num: int, terms: list, res=0):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        for i in range(len(terms)):
            res += combs(num=num - terms[i], terms=terms[i:])
    return res


if __name__ == '__main__':
    # primes = [2, 3]
    primes = [n for n in range(2, 10) if is_prime(n)]
    num = 10
    while combs(num=num, terms=[n for n in primes if n < num]) < 5000:
        num += 1
        primes += [num] if is_prime(num) else []
    print(num)


