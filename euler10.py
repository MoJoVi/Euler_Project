#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

#Найдите сумму всех простых чисел меньше двух миллионов.
import time
start_time = time.time()
n=0
primes = [3]
for i in range(5, 2000000, 2):
    if int(primes[n]) ** 2 == i:
        n += 1
        continue
    for k in primes[:n+1]:#divider
        if i % k == 0:
            break
        elif k == primes[n]:
            primes.append(i)
            break
print(sum(primes)+2)
print("--- %s seconds ---" % (time.time() - start_time))

#[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#0.2211003303527832 seconds