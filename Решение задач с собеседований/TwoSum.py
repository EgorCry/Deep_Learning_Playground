from math import log2


def binary_search(lst, a, low, high):
    """:returns index if a is in list"""
    if low > high:
        return -1
    mid = int((low + high) / 2)
    if a == lst[mid]:
        return mid
    if a > lst[mid]:
        return binary_search(lst, a, mid + 1, high)
    return binary_search(lst, a, low, mid-1)


def two_sum(lst, req):
    """:returns indexes of for requested value"""
    ind_1, ind_2 = -1, -1
    for i in range(len(lst)):
        if int((req - lst[i]) / 2) == 0:
            return ind_1, ind_2
        temp = binary_search(lst, req - lst[i], 0, len(lst)-1)
        if lst[temp] > 0 and req - lst[i] - lst[temp] == 0:
            ind_1, ind_2 = i, temp
            return ind_1, ind_2


list_1 = [2, 7, 13, 15]
print(two_sum(list_1, 28))
print([list_1[i] for i in two_sum(list_1, 28)])
