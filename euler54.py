"""В карточной игре покер ставка состоит из пяти карт и оценивается
от самой младшей до самой старшей в следующем порядке:

Старшая карта: Карта наибольшего достоинства.
Одна пара: Две карты одного достоинства.
Две пары: Две различные пары карт
Тройка: Три карты одного достоинства.
Стрейт: Все пять карт по порядку, любые масти.
Флаш: Все пять карт одной масти.
Фул-хаус: Три карты одного достоинства и одна пара карт.
Каре: Четыре карты одного достоинства.
Стрейт-флаш: Любые пять карт одной масти по порядку.
Роял-флаш: Десятка, валет, дама, король и туз одной масти.
Достоинство карт оценивается по порядку:
2, 3, 4, 5, 6, 7, 8, 9, 10, валет, дама, король, туз.

Если у двух игроков получились ставки одного порядка, то выигрывает
тот, у кого карты старше: к примеру, две восьмерки выигрывают две пятерки.
Если же достоинства карт у игроков одинаковы, к примеру, у обоих игроков
пара дам, то сравнивают карту наивысшего достоинства (см. пример 4 ниже);
если же и эти карты одинаковы, сравнивают следующие две и т.д.

Файл poker.txt содержит одну тысячу различных ставок для игры двух игроков.
В каждой строке файла приведены десять карт (отделенные одним пробелом):
первые пять - карты 1-го игрока, оставшиеся пять - карты 2-го игрока. Можете
считать, что все ставки верны (нет неверных символов или повторов карт),
ставки каждого игрока не следуют в определенном порядке, и что при каждой
ставке есть безусловный победитель.

Сколько ставок выиграл 1-й игрок?

Примечание: карты в текстовом файле обозначены в соответствии с английскими
наименованиями достоинств и мастей: T - десятка, J - валет, Q - дама,
K - король, A - туз; S - пики, C - трефы, H - червы, D - бубны."""


def how_cards(cardlist):
    sorting = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    for ix, card in enumerate(cardlist):
        card = list(card)
        card[0] = sorting[card[0]] if not card[0].isdigit() else int(card[0])
        cardlist[ix] = card
    first_player, second_player = sort_cards(cardlist[:5]), sort_cards(cardlist[5:])
    return first_player, second_player


def sort_cards(hand):
    value, suit = list(), set()
    for card in hand:
        suit.add(card.pop())
        value.append(card.pop())
    value.sort(reverse=True)
    return value, suit


def how_comb(hand):
    if flush(hand[1]):
        if straight(hand[0]):
            if hand[0][0] == 14:
                res = 10
            res = 9
        res = 6
    elif straight(hand[0]):
        res = 5
    elif len(set(hand[0])) == 5:
        res = 1
    else:
        return pairs(hand[0])
    return res, hand[0]


def flush(suit):
    return len(suit) == 1


def straight(value):
    for ix, num in enumerate(range(value[0], value[0] - 5, -1)):
        if value[ix] != num:
            return False
    else:
        return True


def pairs(value):
    comb = {(value.count(card), card) for card in value if value.count(card) > 1}
    comb = sorted(list(comb), reverse=True)
    res = {  # other combinations
        (1, 4): 8,
        (1, 3): 4,
        (1, 2): 2,
        (2, 3): 7,
        (2, 2): 3
    }
    return res[(len(comb), comb[0][0])], comb[0][1]


if __name__ == '__main__':
    with open('poker.txt') as poker:
        res = 0
        for part in poker.readlines():
            part = part.rstrip().split(' ')
            first, second = how_cards(part)
            first, second = how_comb(first), how_comb(second)
            for fir, sec in zip(first, second):
                if fir > sec:
                    res += 1
                    break
                elif fir < sec:
                    break
        print(res)
