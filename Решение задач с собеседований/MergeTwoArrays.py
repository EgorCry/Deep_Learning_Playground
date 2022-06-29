"""
Даны две отсортированные последовательности чисел (длиной n и m соответственно).
Необходимо слить их в одну отсортированную последовательность.
Example: f = [1, 1, 3, 5, 5, 5, 7] s = [2, 4, 6, 7, 8, 8, 8, 8]
Answer: [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8]
"""


def merge_arrays(arr_1, arr_2):
    first, second = 0, 0
    nswr = []
    for k in range(len(arr_1) + len(arr_1)):
        if first != len(arr_1) and (second == len(arr_2) or
                                    arr_1[first] < arr_2[second]):
            nswr.append(arr_1[first])
            first += 1
        else:
            nswr.append(arr_2[second])
            second += 1
    return nswr


print(merge_arrays([1, 1, 3, 5, 5, 5, 7], [2, 4, 6, 7, 8, 8, 8, 8]))
