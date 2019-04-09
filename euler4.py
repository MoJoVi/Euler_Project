# Число-палиндром с обеих сторон (справа налево и слева направо)
# читается одинаково.
# Самое большое число-палиндром, полученное умножением
# двух двузначных чисел – 9009 = 91 × 99.

# Найдите самый большой палиндром, полученный умножением
# двух трехзначных чисел.
d = 0
i = 998000  # the largest number that can be obtained by
# multiplying three-digit numbers
while d == 0:
    i -= 1
    if str(i) == str(i)[::-1]:  # find the most bigger palindrome
        for d2 in range(999, 100, -1):
            # check whether you can get this number by
            # multiplication of three-digit numbers
            if i / d2 > 999:
                break
            if i % d2 == 0:
                d = int(i / d2)
                break
print(d, d2, i)
