#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
#Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
import time
start_time = time.time()

d2 = 0
for i in range(998001,10000,-1):
    if str(i) == str(i)[::-1]:#find the most bigger polidrom
        for d in range(999,100,-1):#check whether you can get this number by
            #multiplication of three-digit numbers
            if i / d >999:
                break
            if i % d == 0:
                d2 = int(i/d)
                break
    if d2 != 0:
        break
print(d,d2,i)

print("--- %s seconds ---" % (time.time() - start_time))