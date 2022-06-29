"""
Игрок в футбол обладает одной числовой характеристикой - профессионализмом. Ко-
манда называется сполчённой, если профессионализм любого игрока не превосходит
суммарный профессионализм любых двух игроков из команды. Команда может состоять
из любого количества игроков. Дана отсортированная последовательность чисел дли-
ной N - профессионализм игроков. Необходимо найти максимальный суммарный профес-
сионализм сплочённой команды.
Example: rqst = [1, 1, 3, 3, 4, 6, 11]
Answer: 17
"""


def best_team_sum(arr):
    best_sum = 0
    last = 0
    current_sum = 0
    for first in range(len(arr)):
        while last < len(arr) and (last == first or
                                   arr[first] + arr[first + 1] >= arr[last]):
            current_sum += arr[last]
            last += 1
        best_sum = max(best_sum, current_sum)
        current_sum -= arr[first]
    return best_sum


print(best_team_sum([1, 1, 3, 3, 4, 6, 11]))
print(best_team_sum([9]))
