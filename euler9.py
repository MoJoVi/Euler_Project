#Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

#a2 + b2 = c2
#Например, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.
import time
start_time = time.time()

for i in range(1,30):
    for n in range(1, 300):
        m = n+i
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        if a + b + c == 1000:
            break
        if a + b + c > 1000:
            print('FUCK!')
            break
    if a + b + c == 1000 and a**2 + b**2 == c**2:
        print(a * b * c, a, b, c)
        break

print("--- %s seconds ---" % (time.time() - start_time))