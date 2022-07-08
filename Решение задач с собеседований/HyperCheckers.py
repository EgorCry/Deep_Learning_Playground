"""
В каждой игре в гипершашки участвует три игрока. По ходу игры каждый из игроков на-
бирает некоторое положительное целое число баллов. Если после окончания гры первый
игрок набрал а баллов, второй - b, а третий c, то говорят, что игра закончилась со
счётом a:b:c.
Андрей знает, что правила игры гипершашек устроены таким образом, что в результате
игры баллы любых двух игроков различаются не более чем в k раз.
После матча Андрей показывает его результат, размещая три карточки с очками игроков
на специальное табло. Для этого у него есть набор из n карточек, на которых написа-
ны числа x1, x2, ..., xn. Чтобы выяснить, насколько он готов к чемпионату, Андрей
хочет понять, сколько различных вариантов счёта он сможет показать на табло, ис-
пользуя имеющиеся карточки.
3 <= n <= 1_000_000, 1 <= k <= 10^9, 1 <= xi <= 10^9
Example:
n, k = 5 2
x = 1 2 1 3 3
"""


def hyper_checkers(n, k, x):
    n = n
    k = k
    x = x
    cnt_nums = {}
    for i in x:
        if i not in cnt_nums:
            cnt_nums[i] = 0
        cnt_nums[i] += 1
    uniq_nums = list(cnt_nums.keys())
    uniq_nums.sort()
    r = 0
    nswr = 0
    duplicates = 0
    for l in range(len(uniq_nums)):
        while r < len(uniq_nums) and uniq_nums[l] * k >= uniq_nums[r]:
            if cnt_nums[uniq_nums[r]] >= 2:
                duplicates += 1
            r += 1
        range_len = r - l
        if cnt_nums[uniq_nums[l]] >= 2:
            nswr += (range_len - 1) * 3
        if cnt_nums[uniq_nums[l]] >= 3:
            nswr += 1
        nswr += (range_len - 1) * (range_len - 2) * 3
        if cnt_nums[uniq_nums[l]] >= 2:
            duplicates -= 1
        nswr += duplicates * 3
    return nswr


n, k = map(int, input().split())
x = list(map(int, input().split()))
print(hyper_checkers(n, k, x))
