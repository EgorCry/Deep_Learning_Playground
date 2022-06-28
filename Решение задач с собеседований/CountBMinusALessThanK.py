'''
Дан отсортированный список. Нужно найти количество пар элементов, сумма которых будет меньше заданного числа К.
Пример: rqst = [1, 3, 7, 8, 9] k = 3
Answer: 6
'''


def cnt_b_minus_a_less_k(arr, k):
    last = 0
    cnt = 0
    for i in range(len(arr)):
        while last < len(arr) and arr[last] - arr[i] <= k:
            last += 1
        cnt += len(arr) - last
    return cnt


print(cnt_b_minus_a_less_k([1, 3, 7, 8, 9], 3))
assert(cnt_b_minus_a_less_k([1, 3], 1) == 1)
print(cnt_b_minus_a_less_k([2, 3], 1))
assert(cnt_b_minus_a_less_k([1, 2], 1) == 0)
