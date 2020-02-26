"""
Пусть p(n) представляет собой число различных способов, которыми можно разделить
монеты на несколько столбиков. К примеру, пять монет можно разделить на несколько
столбиков ровно семью различными способами, таким образом p(5) = 7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Найдите наименьшее значение n для которого p(n) делится на один миллион без остатка.
"""
import time
from math import ceil

start = time.time()


def gen_next_p():
    p_nums, num = dict(), 0
    while True:
        res = p_nums.get(num - 1, 0) + p_nums.get(num - 2, 0)
        res += 1 if not res else 0
        k = -1
        for q in range(2, ceil(num ** 0.5)):
            f1 = p_nums.get(num - ((3 * (q ** 2) - q) / 2), 0)
            f2 = p_nums.get(num - ((3 * (q ** 2) + q) / 2), 0)
            if f1 or f2:
                res += k * (f1 + f2)
                k *= -1
            else:
                break
        p_nums[num] = res
        yield num, res
        num += 1


if __name__ == '__main__':
    next_p = iter(gen_next_p())
    num, p = next(next_p)
    while p % 1000000:
        num, p = next(next_p)
    print('num:', num)
    print(f'time: {time.time() - start} sec.')
