"""n! означает n × (n − 1) × ... × 3 × 2 × 1
Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Найдите сумму цифр в числе 100!."""
from functools import reduce

ans = str(reduce(lambda x, y: x * y, list(range(1, 101))))
ans = reduce(lambda x, y: int(x) + int(y), ans)
print(ans)
