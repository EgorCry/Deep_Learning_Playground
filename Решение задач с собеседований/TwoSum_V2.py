'''
Найти 2 элемента массива, сумма которых равна заданному числу

Example: a = [1 4 7 8 10 20], target = 11
Answer: i_1 = 0, i_2 = 4
'''


def two_sum_in_array(arr, t):
    i_1 = 0
    i_2 = len(arr) - 1
    ans = -1
    while True:
        current_sum = arr[i_1] + arr[i_2]
        if current_sum == t:
            ans = current_sum
            return i_1, i_2
        if current_sum > t:
            i_2 -= 1
        else:
            i_2 += 1


assert(two_sum_in_array([1, 4, 7, 8, 10, 20], 11) == (0, 4))
assert(two_sum_in_array([1, 2], 3) == (0, 1))
assert(two_sum_in_array([1, 2, 3, 4, 5, 6], 7) == (0, 5))
assert(two_sum_in_array([10, 20, 30, 40, 123], 133) == (0, 4))
