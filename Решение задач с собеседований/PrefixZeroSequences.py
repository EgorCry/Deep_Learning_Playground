"""
Дана последовательность чисел длиной N. Надо найти количество отрезков с нулевой суммой.
Пример: rqst = [1, -1, 1, 0, 1]
Answer: 4
"""


def prefix_sum_count(arr):
    cnt_dict = {0: 1}
    cur_sum = 0
    for i in arr:
        cur_sum += i
        if cur_sum not in cnt_dict:
            cnt_dict[cur_sum] = 0
        cnt_dict[cur_sum] += 1
    return cnt_dict


def ranges_count(cnt_dict):
    cnt_ranges = 0
    for k in cnt_dict:
        temp = cnt_dict[k]
        cnt_ranges += temp * (temp - 1) // 2
    return cnt_ranges


print(ranges_count(prefix_sum_count([1, -1, 1, 0, 1])))
assert(ranges_count(prefix_sum_count([1, 0])) == 1)
assert(ranges_count(prefix_sum_count([1, 0, -1])) == 2)
