#найти сумму всех чисел не превышающих 1000, которые делятся на 3 или 5
import time
start_time = time.time()

x = (x for x in range(3,1000) if x %3 == 0 or x % 5 == 0)
print(sum(x))

print("--- %s seconds ---" % (time.time() - start_time))