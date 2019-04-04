#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом?
import time
start_time = time.time()

n = 600851475143
for i in range(2,n):
    if n // i == 1:
        break
    elif n % i == 0:
        n //= i
print(n)

print("--- %s seconds ---" % (time.time() - start_time))