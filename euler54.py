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
cards = {}
with open('poker.txt') as poker:
    for i in range(1000):
        part = poker.readline()
        cards[i] = part.replace('\n', '').split(' ')


def how_cart(cardlist):
    for ix, card in enumerate(cardlist):
        card = [card[0], card[1]]

        if card[0] == 'T':
            card[0] = 10
        elif card[0] == 'J':
            card[0] = 11
        elif card[0] == 'Q':
            card[0] = 12
        elif card[0] == 'K':
            card[0] = 13
        elif card[0] == 'A':
            card[0] = 14
        else:
            card[0] = int(card[0])
        cardlist[ix] = card
    first_player, second_player = cardlist[:5], cardlist[5:]
    first_player = sort_cards(first_player)
    second_player = sort_cards(second_player)

    return first_player, second_player


def sort_cards(hand):
    value = []
    suit = set()
    for card in hand:
        suit.add(card.pop(-1))
        value.append(*card)

    value.sort()
    return value, suit


def how_comb(hand):
    if len(hand[1]) == 1 \
            and straight(hand[0]) \
            and hand[0][-1] == 14:  # Royal Flush
        return 10
    elif len(hand[1]) == 1 and straight(hand[0]):  # Straight Flush
        return 9, hand[0][-1]
    elif len(hand[1]) == 1:  # Flush
        return 6, hand[0][4], hand[0][3], \
               hand[0][2], hand[0][1], hand[0][0]
    elif straight(hand[0]):  # Straight
        return 5, hand[0][-1]
    return pairs(hand[0])


def straight(value):
    if value[4] - value[3] == 1 \
            and value[3] - value[2] == 1 \
            and value[2] - value[1] == 1 \
            and value[1] - value[0] == 1:
        return True
    else:
        return False


def pairs(value):
    if len(set(value)) == 5:
        return 1, value[4], value[3], value[2], value[1], value[0]
    v = 0
    n = 0
    comb = []
    for card in value:
        for other in value:
            if card == other:
                n += 1
                v = card
        if n > 1:
            comb.append((n, v))
            for i in range(n):
                value.remove(v)
        n = 0

    comb = list(set(comb))
    if len(comb) == 1:
        comb = comb[0]
        if comb[0] == 4:  # Four of a Kind
            return 8, comb[1], value[0]
        elif comb[0] == 3:  # Three of a Kind
            return 4, comb[1], value[1], value[0]
        elif comb[0] == 2:  # One Pair
            return 2, comb[1], value[2], value[1], value[0]

    else:
        if comb[0][0] == 3:  # Full House
            return 7, comb[0][1], comb[1][1]
        elif comb[1][0] == 3:
            return 7, comb[1][1], comb[0][1]
        else:  # Two Pairs
            return 3, max(comb[0][1], comb[1][1]), \
                   min(comb[0][1], comb[1][1]), value[0]


res = 0

for part in cards:
    first, second = how_cart(cards[part])
    first = how_comb(first)
    second = how_comb(second)

    for i in range(len(first)):
        print(i)
        if first[i] > second[i]:
            res += 1
            break
        elif first[i] < second[i]:
            break

print(res)
