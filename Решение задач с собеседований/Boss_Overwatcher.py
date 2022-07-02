"""
Сайт посетило N человек, для каждого известно время входа на сайт In, и время выхо-
да с сайта Out. Считается, что человек был на сайте с момента In по Out включитель-
но. Начальник заходил на сайт M раз в моменты времени Boss и смотрел, сколько людей
сейчас онлайн. Посещения сайта начальником упорядочены по возрастанию времени.
Определите, какие показания счётчика людей онлайн увидел начальник.
"""


def how_many_online_while_boss(n, tin, tout, m, boss):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    for i in range(m):
        events.append((boss[i], 0))
    online = 0
    boss_see = []
    events.sort()
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == 1:
            online -= 1
        elif events[i][1] == 0:
            boss_see.append(online)
    return boss_see


n = 5
in_1 = [2, 2, 2, 3, 3]
out_1 = [5, 3, 4, 6, 4]
m = 2
boss_1 = [3, 5]
print(how_many_online_while_boss(n, in_1, out_1, m, boss_1))
