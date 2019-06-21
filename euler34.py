"""
145 является любопытным числом, поскольку
1! + 4! + 5! = 1 + 24 + 120 = 145.
Найдите сумму всех чисел, каждое из которых равно сумме
факториалов своих цифр. Примечание: поскольку 1! = 1 и 2! = 2
не являются суммами, учитывать их не следует.
"""
from functools import reduce
import time
start_time = time.time()

res = []

fact_list = {str(num): reduce(lambda x, y: x * y, range(1, num + 1))
             for num in range(1, 10)}

for num in range(145, 2180000):
    fact_num = list()
    for i in str(num):
        if i != '0':
            fact_num.append(fact_list[i])
    if num == sum(fact_num):
        res.append(num)
print(sum(res), time.time() - start_time, 'sec')
