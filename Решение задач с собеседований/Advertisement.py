"""
Фирма NNN решила транслировать свой рекламный ролик в супермаркете ХХХ. Однако, де-
нег, запланированных на рекламную кампанию, хватило лишь на две трансляции ролика в
течение одного рабочего дня.
Фирма NNN собрала информацию о времени прихода и времени ухода каждого покупателя в
некоторый день. Менеджер по рекламе предположил, что и на следующий день покупатели
будут приходить и уходить ровно в те же моменты времени.
Помогите ему определить моменты времени, когда нужно включить трансляцию рекламных
роликов, чтобы как можно большее количество покупателей прослушало ролик целиком
от начала до конца хотя бы один раз. Ролик длится ровно 5 единиц времени. Трансля-
ции роликов не должны пересекаться, то есть начало второй трансляции должно быть
хотя бы на 5 единиц времени позже, чем начало первой.
1 <= N <= 2_000
"""


def ad(n):
    events = []
    for i in range(n):
        now_in, now_out = map(int, input().split())
        if now_out - now_in >= 5:
            events.append((now_in, -1, i))
            events.append((now_out - 5, 1, i))
    events.sort()
    if len(events) == 0:
        return (0, 10, 20)
    elif len(events) == 2:
        return (1, events[0][0], events[0][0] + 10)
    best_ans = 0
    first_best, second_best = 0, 0
    first_ad = set()
    for i in range(len(events)):
        event1 = events[i]
        if event1[1] == -1:
            first_ad.add(event1[2])
            if len(first_ad) > best_ans:
                best_ans = len(first_ad)
                first_best = event1[0]
                second_best = event1[0] + 5
        second_cnt = 0
        for j in range(i + 1, len(events)):
            event2 = events[j]
            if event2[1] == -1 and event2[2] not in first_ad:
                second_cnt += 1
            if event2[0] - 5 >= event1[0] and len(first_ad) + second_cnt > best_ans:
                best_ans = len(first_ad) + second_cnt
                first_best = event1[0]
                second_best = event2[0]
            if event2[1] == 1 and event2[2] not in first_ad:
                second_cnt -= 1
        if event1[1] == 1:
            first_ad.remove(event1[2])
    return (best_ans, first_best, second_best)
