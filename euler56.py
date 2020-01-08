"""
Гугол (10^100) - гигантское число: один со ста нулями; 100^100 почти
невообразимо велико: один с двумястами нулями. Несмотря на их размер,
сумма цифр каждого числа равна всего лишь 1.

Рассматривая натуральные числа вида a^b, где a, b < 100, какая
встретится максимальная сумма цифр числа?
"""
res = 0
for a in range(1, 100):
    for b in range(1, 100):
        res = max(res, sum(int(x) for x in str(a ** b)))

print(res)