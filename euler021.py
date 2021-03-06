"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
а каждое из чисел a и b - дружественным числом.
Например, делителями числа 220 являются:
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284.
Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.
Подсчитайте сумму всех дружественных чисел меньше 10000.
"""


def sum_divs(num):
    res_num = 1
    for div in range(2, int(num ** 2)):
        if not num % div:
            res_num += div + (num // div)
    return int(res_num)


if __name__ == '__main__':
    res = set()
    for num in range(10000):
        if num in res:
            continue
        sec = sum_divs(num)
        if num != sec and num == sum_divs(sec):
            res.update({num, sec})

    print(sum(res))
