"""
145 является любопытным числом, поскольку
1! + 4! + 5! = 1 + 24 + 120 = 145.
Найдите сумму всех чисел, каждое из которых равно сумме
факториалов своих цифр. Примечание: поскольку 1! = 1 и 2! = 2
не являются суммами, учитывать их не следует.
"""
from functools import reduce

fact_list = {str(num): reduce(lambda x, y: x * y, range(1, num + 1))
             for num in range(1, 10)}
fact_list['0'] = 1

res = sum([num for num in range(145, 100000) if
           num == sum([fact_list[i] for i in str(num)])])

print(res)
