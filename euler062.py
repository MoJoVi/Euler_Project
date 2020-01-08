"""
Можно найти перестановки куба 41063625 (3453), чтобы получить еще два куба:
56623104 (3843) и 66430125 (4053). К слову, 41063625 является наименьшим кубом,
для которого ровно три перестановки также являются кубами

Найдите наименьший куб, для которого ровно пять перестановок также
являются кубами.
"""
from collections import defaultdict

cub_dict = defaultdict(list)
for num in range(345, 10000):
    cub_num = ''.join(sorted(str(num ** 3)))
    cub_dict[cub_num].append(num)

    if len(cub_dict[cub_num]) == 5:
        print(min(cub_dict[cub_num]) ** 3)
        break

