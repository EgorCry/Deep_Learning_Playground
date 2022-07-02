"""
Сайт посетило N человек. Для каждого известно время входа на сайт In и время выхо-
да с сайта Out. Считается, что человек был на сайте с момента In по Out, включи-
тельно.
Определите, какое максимальное количество человек было на сайте одновременно.
"""


def maximum_at_the_same_time(n, in_1, out_1):
    check_d = {}
    for i in range(n):
        for j in range(in_1[i], out_1[i]+1):
            if j not in check_d:
                check_d[j] = 0
            check_d[j] += 1
    # max_t = next(iter(check_d))
    # max_p = check_d[max_t]
    max_p = 0
    for k, v in check_d.items():
        if v > max_p:
            # max_t = k
            max_p = v
    return max_p


def maximum_at_the_same_time_1(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online


in_0 = [1, 2, 1]
out_0 = [2, 3, 3]
print(maximum_at_the_same_time(3, in_0, out_0))
in_0 = [2, 2, 2, 3, 3]
out_0 = [5, 3, 4, 6, 4]
print(maximum_at_the_same_time(5, in_0, out_0))
print(maximum_at_the_same_time_1(5, in_0, out_0))
