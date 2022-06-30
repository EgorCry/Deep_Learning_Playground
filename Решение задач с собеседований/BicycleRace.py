"""
Велосипедисты, участвующие в шоссейной гонке, в некоторый момент времени, который
называется начальным, оказались в точках, удалённых от места старта на x1, x2 ...
xn метров (n - общее количество велосипедистов, не превосходящих 100_000). Каждый
велосипедист двигается со своей сокоростью v1, v2 ... vn метров в секунду. Все ве-
лосипедисты двигаются в одну и ту же сторону. Репортёр, освещающий ход соревнова-
ний, хочет определить момент времени, в который расстояние между лидирующим в гон-
ке велосипедистом и замыкающим гонку велосипедистом станет минимальным, чтобы с
вертолёта сфотографировать сразу всех участников велогонки.
Необходимо найти момент времени, когда расстояние станет минимальным.
(!)Дополнительно: вывести расстояние между велосипедистами в нужный момент времени.
"""


def position(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0] * t
    for i in range(1, len(x)):
        pos = x[i] + v[i] * t
        minpos = min(pos, minpos)
        maxpos = max(pos, maxpos)
    return maxpos - minpos


def check_dist(t, params):
    x, v = params
    minpos = maxpos = x[0] + v[0] * t
    for i in range(1, len(x)):
        pos = x[i] + v[i] * t
        minpos = min(pos, minpos)
        maxpos = max(pos, maxpos)
    return maxpos - minpos


def check_difference(t, eps, check, params):
    return check(t + eps, params) >= check(t, params)


def float_binary_search(l, r, eps, dif_check, dist_check, params):
    while l + eps < r:
        t = (l + r) / 2
        if dif_check(t, eps, dist_check, params):
            r = t
        else:
            l = t
    return l, position(l, params)


x = [90, 100, 100, 110, 120]
v = [100, 70, 70, 60, 35]
print(float_binary_search(0, 100, 0.000001, check_difference, check_dist, (x, v)))

x_1 = [0, 30, 40]
v_1 = [40, 10, 30]
print(float_binary_search(0, 150, 0.000001, check_difference, check_dist, (x_1, v_1)))
