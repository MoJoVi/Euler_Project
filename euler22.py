"""Используйте names.txt, текстовый файл размером 46 КБ, содержащий
более пяти тысяч имен. Начните с сортировки в алфавитном порядке. Затем
подсчитайте алфавитные значения каждого имени и умножьте это значение
на порядковый номер имени в отсортированном списке для получения количества
очков имени. Например, если список отсортирован по алфавиту, имя COLIN
(алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым
в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
Какова сумма очков имен в файле?"""
from string import ascii_uppercase as alph

numsdict = {letter: alph.index(letter) + 1 for letter in alph}

with open('names.txt') as names:
    for namelist in names:
        namelist = sorted(namelist.replace('"', '').split(','))

res = 0

for name in namelist:
    name_res = 0
    for letter in name:
        name_res += numsdict[letter]
    name_res *= (namelist.index(name) + 1)
    res += name_res

print(res)
