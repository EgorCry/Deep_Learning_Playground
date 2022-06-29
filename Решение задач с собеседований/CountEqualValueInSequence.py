"""
Задана отсортированная по неубыванию последовательность из N чисел и число X.
Необходимо определить сколько раз число X входит в последовательность.
"""


def check_equal_or_bigger(index, params):
    seq, x = params
    return seq[index] >= x


def check_bigger(index, params):
    seq, x = params
    return seq[index] > x


def binary_search(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    return l


def find_first(seq, x, check):
    ans = binary_search(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans


def answer_func(seq, x):
    left_index = find_first(seq, x, check_equal_or_bigger)
    right_index = find_first(seq, x, check_bigger)
    return right_index - left_index


print(answer_func([1, 2, 2, 2, 3, 4], 2))
print(answer_func([1, 2, 3, 4], 2))
