"""
В Англии валютой являются фунты стерлингов £ и пенсы p, и в
обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
Сколькими разными способами можно составить £2, используя любое
количество монет?
"""
coins = (1, 2, 5, 10, 20, 50, 100, 200)


def sum_combs(sum_coins, coins, combs=0):
    if sum_coins == 200:
        return 1
    elif sum_coins > 200:
        return 0
    else:
        for i in range(len(coins)):
            combs += sum_combs(sum_coins + coins[i], coins[i:])
    return combs


if __name__ == '__main__':
    print(sum_combs(0, coins))
