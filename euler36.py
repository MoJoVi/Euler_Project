"""
Десятичное число 585 = 10010010012 (в двоичной системе), является
палиндромом по обоим основаниям.
Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по
основаниям 10 и 2. (Пожалуйста, обратите внимание на то, что палиндромы
не могут начинаться с нуля ни в одном из оснований).
"""
print(sum([num for num in range(10 ** 6) if str(num) == str(num)[::-1] and
           bin(num)[2:] == bin(num)[2:][::-1]]))
