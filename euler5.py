#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

#Какое самое маленькое число делится нацело на все числа от 1 до 20?
k = 0
n = 2520
for i in range(1,21):
    if n % i != 0:
        n *= i
while n != k:
    k = n
    n //= 2
    for i in range(2,21):
        if n % i != 0:
            n *= 2
            break
        elif i == 20:
            break
print(n)











#n = 0
#for i in range(2520, 1000000000, 20):
#    for n in range(2, 21):
#        if i % n != 0:
#            n = 0
#            break
#        elif n == 20:
#            break
#    if n == 20:
#        break
#print(i)