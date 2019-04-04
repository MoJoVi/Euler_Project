#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

#Какое число является 10001-ым простым числом?
import time
start_time = time.time()

n = 1# Prime number counter
i = 1
while n < 10001:
    i += 2
    for k in [3,5,7]:#dividers
        if i % k == 0:
            break
        elif k == 7:
            n += 1
            if n == 10001:
                break
            break
    if n == 10001:
        break
print(i,n)

print("--- %s seconds ---" % (time.time() - start_time))