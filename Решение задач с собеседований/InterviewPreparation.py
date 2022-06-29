"""
Вася готовится к собеседеованию. Он выбрал на сайте leetcode N задач. В первый день
Вася решил K задач, а в каждый следующий день Вася решал на одну задачу больше, чем
в предыдущий.
Определите, сколько дней уйдёт у Васи на подготовку к собеседованию.
"""


def check_params(days, params):
    n, k = params
    return (k + (k + days - 1)) * days // 2 >= n


def binary_search(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    return l


print(binary_search(0, 20, check_params, [20, 1]))
print(binary_search(0, 100, check_params, [100, 3]))
