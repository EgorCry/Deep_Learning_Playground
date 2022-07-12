"""
На секретной военной базе работает N охранников. Сутки поделены на 10_000 равных
промежутков времени, и известно, когда каждый из охранников приходит на дежурство
и уходит с него. Например, если охранник приходит в 5, а уходит в 8, то значит, что
он был в 6, 7 и 8-о1 промежуток (а в 5-ый - нет).
Укажите, верно ли, что для данного набора охранников, объект охраняется в любой мо-
мент времени хотя бы одним охранником и удаление любого из них приводит к появлению
промежутка времени, когда объект не охраняется.
N <= 10_000, K <= 100
"""


def security(k):
    nswr = [''] * k
    for test in range(k):
        nums = list(map(int, input().split()))
        n = nums[0]
        events = [0] * (2 * n)
        for i in range(1, len(nums), 2):
            events[i - 1] = (nums[i], -1, i)
            events[i] = (nums[i + 1], 1, i)
        events.sort()
        good_seq = set()
        now_seq = set()
        good_flag = True
        prev_time = -1
        for event in events:
            if event[0] != 0 and len(now_seq) == 0:
                good_flag = False
                break
            if len(now_seq) == 1 and event[0] != prev_time:
                good_seq.update(now_seq)
            if event[1] == -1:
                now_seq.add(event[2])
            else:
                now_seq.remove(event[2])
            prev_time = event[0]
        if events[-1][0] != 10_000:
            good_flag = False
        if good_flag and len(good_seq) == n:
            nswr[test] = 'Accepted'
        else:
            nswr[test] = 'Wrong Answer'
    return '\n'.join(nswr)


k = 2
security(k)
