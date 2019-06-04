# #*ЗАДАЧИ НА ДЕКОРАТОРЫ
#
# #Написать декоратор, который отменяет выполнение любой декорированной
# #функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!
#
# def is_closing(function):
#     def inner(*arg):
#         try:
#             raise SyntaxError
#         except:
#             print(function.__name__,'is closing!')
#     return inner
#
# @is_closing
# def funk(arg):
#     print('Function is work!', arg)
#
# @is_closing
# def func(*args):
#     return print(sum(args))
#
# funk('hipe')
# func(6,78,9,6)
#
# #Реализовать декоратор, который измеряет скорость выполнения функций.
# import time
# start_time = time.time()
#
# def timer(func):
#     def inner(*args):
#         x = func(*args)
#         print('{} seconds'.format(time.time()- start_time))
#         return x
#     return inner
#
# @timer
# def funk(arg):
#     print('Function is work!', arg)
#
# @timer
# def summ(*args):
#     return sum(args)
#
# print(summ(5,6,453545,345,34,56,456,45,64,56,456,45))
# funk('NINI')
#
# #Реализовать декоратор, который будет считать, сколько раз выполнялась функция
#
# def counter(func):
#     n = 0
#     def inner(*args):
#         nonlocal n
#         n += 1
#         print('Function {} wos running {} times'.format(func.__name__,n))
#         return func(*args)
#     return inner
#
# @counter
# def funk(arg):
#     print('Function is work!', arg)
#
# @counter
# def summ(*args):
#     return sum(args)
#
# print(summ(16,35,664,4,6,4658,4))
# funk('mom')
# funk('mom')
# print(summ(165,65,51,6,432,16,4))
# print(summ(165,65,51,6,432,16,4))
# funk('mom')
# funk('mom')
# print(summ(165,65,51,6,432,16,4))
# print(summ(165,65,51,6,432,16,4))
# funk('mom')
# print(summ(165,65,51,6,432,16,4))
# print(summ(165,65,51,6,432,16,4))
#
# #Реализовать декоторатор, который будет логгировать процесс выполнения функции:
# #создан декоратор, начато выполнение функции, закончено выполнение функции
#
# def decorator(function):
#     def inner(*arg):
#         print('Running Decorator...\n Snacks Function {}'.format(function.__name__))
#         x = function(*arg)
#         print('The Function {} is completed...\n Closing Decorator'.format(function.__name__))
#         return x
#     return inner
#
# @decorator
# def funk(arg):
#     print('Function is work!', arg)
#
# @decorator
# def summ(*args):
#     return sum(args)
#
# print(summ(16,35,664,4,6,4658,4))
# funk('mom')
#
# #Реализовать декоратор, который будет перехватывать все исключения в функции.
# #Если они случились, нужно просто писать в консоль сообщение об ошибке
# def errors_hunter(function):
#     def inner(*arg):
#         try:
#             x = function(*arg)
#         except IndexError as e:
#             print(e)
#         except SyntaxError as e:
#             print(e)
#         except TypeError as e:
#             print(e)
#         except NameError as e:
#             print(e)
#         else:
#             return x
#     return inner
#
# @errors_hunter
# def funk(arg):
#     print('Function is work!', arg)
#
# @errors_hunter
# def summ(*args):
#     return sum(args)
#
# print(summ(16,35,664,4,6,print(),4))
# print(summ(16,35,664,4,6,'rrr',4))
# print(summ(None))
# funk('mom', None)
#
# #ЗАДАЧИ НА MAP/FILTER/REDUCE (И LAMBDA, ЕСЛИ НУЖНО)
#
# #При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
#
# x = list(map(lambda y: y % 5, [1, 4, 5, 30, 99]))
# print(x)
#
# #При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
#
# x = list(map(str, [3, 4, 90, -2]))
# print(x)
#
# #При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки
#
# x = list(filter(lambda y: type(y) != str, ['some', 1, 'v', 40, '3a', str]))
# print(x)
#
# import math
#
# import time
# start_time = time.time()
#
#
#
# end_time=time.time()-start_time
# print(end_time)
#
# #написать генератор, который, при его вызове,
# #будет возвращать случайное значение
#
# import random
# def rand_numb():
#     while True:
#         yield random.randint(1,10)
# x = rand_numb()
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# #написать генератор который будет работать как range()
# def gen_range(arg):
#     n = 0
#     if type(arg) == str:
#         while True:
#             yield arg[n]
#             n += 1
#     elif type(arg) == int:
#         while n < arg:
#             yield n
#             n += 1
#     else:
#         while True:
#             yield arg[n]
#             n += 1
# x = gen_range('abc')
# y = gen_range(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
#
# #Написать генератор, который работает как map
#
# def gen_map(func, *args):
#     n = 0
#     while True:
#         yield func(args[n])
#         n += 1
#
# x = gen_map(str, 1,2,3,4,5,6)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
#
# #написать генератор который работает как 'enumerate()'
#
# def gen_enum(arg):
#     n = 0
#     if type(arg) == str:
#         while True:
#             yield arg[n], n
#             n += 1
#     else:
#         while True:
#             yield arg[n], n
#             n += 1
# x = gen_enum('qwe')
# y = gen_enum([1,2,3])
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(y))
# print(next(y))
# print(next(y))
#
# #написать генератор который работает как 'zip()'
#
# def gen_zip(list1, list2):
#     n = 0
#     while True:
#         yield (list1[n], list2[n])
#         n += 1
# x = gen_zip([1,2,3], (4,5,6))
# print(next(x))
# print(next(x))
# print(next(x))

def dec(func):
    # func.counter = 0

    def fake(value):
        # func.counter += 1
        fake.counter += 1
        # print('Runs: ', func.counter)
        print('Runs:', fake.counter)
        return 'fake: ' + func(value)

    fake.counter = 0
    print('Decorated')
    return fake

@dec
def my_func(value):
    return str(value)

# a = dec(my_func)
print(my_func(123))
print(my_func([]))
print(my_func({}))

