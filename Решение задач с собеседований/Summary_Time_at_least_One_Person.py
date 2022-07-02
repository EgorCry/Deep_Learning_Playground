"""
Сайт посетило N человек. Для каждого известно время входа на сайт In и время выхо-
да с сайта Out. Считается, что человек был на сайте с момента In по Out, включи-
тельно.
Определите, какое суммарное время на сайте был хотя бы один человек.
"""


def summary_time_visitors(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()
    print(events)
    online = 0
    sum_time = 0
    for i in range(len(events)):
        if online > 0:
            sum_time += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return sum_time


in_0 = [2, 2, 2, 3, 3]
out_0 = [5, 3, 4, 6, 4]
print(summary_time_visitors(5, in_0, out_0))
in_0 = [1, 2, 1]
out_0 = [2, 3, 3]
print(summary_time_visitors(3, in_0, out_0))
