"""
Задана отсортированная по неубыванию последовательность из N чисел и число X.
Необходимо определить индекс первого числа в последовательнсои, которое больше
либо равно X. Если такого числа нет, то вернуть число N.
"""


def check_value(index, params):
    seq, x = params
    return seq[index] >= x


def binary_search(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    return l


def find_first(seq, x):
    ans = binary_search(0, len(seq) - 1, check_value, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


print(find_first([1, 2, 2, 3, 4, 5], 2))
