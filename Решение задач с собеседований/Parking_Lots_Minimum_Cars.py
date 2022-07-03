"""
На парковке в торговом центре N мест (занумерованных от 1 до N). За день в ТЦ при-
езжало M автомобилей, при этом некоторые из них длинные и занимали несколько подряд
идущих парковочных мест. Для каждого автомобиля известно время приезда и отъезда,а
также два числа - с какого по какое парковочное места он занимал. Если в какой-то
момент времени один автомобиль уехал с парковочного места, то место считается осво-
бодившимся и в тот же момент времени на его место может встать другой.
Необходимо определить, был ли момент, в который были заняты все парковочные места
и определить минимальное количество автомобилей, которое заняло все места. Если
такого момента не было - вернуть М + 1.
"""


def number_on_full_parking_lots(cars, n):
    events = []
    for car in cars:
        in_t, out_t, from_p, to_p = car
        events.append((in_t - 1, 1, to_p - from_p + 1))
        events.append((out_t, -1, to_p - from_p + 1))
    events.sort()
    occupied = 0
    min_cars = len(cars) - 1
    cur_cars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            cur_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            cur_cars += 1
        if occupied == n:
            min_cars = min(cur_cars, min_cars)
    return min_cars


cars_1 = [[5, 5, 1, 2],
          [1, 3, 1, 1],
          [2, 3, 2, 3],
          [3, 5, 4, 6]]
n_1 = 6
print(number_on_full_parking_lots(cars_1, n_1))
cars_2 = [[1, 2, 1, 2],
          [1, 1, 4, 4],
          [1, 3, 6, 6],
          [3, 3, 2, 5],
          [4, 5, 1, 2],
          [4, 4, 3, 3],
          [4, 5, 4, 6]]
n_2 = 6
print(number_on_full_parking_lots(cars_2, n_2))
cars_3 = [[1, 1, 1, 7]]
n_3 = 7
print(number_on_full_parking_lots(cars_3, n_3))
cars_4 = [[1, 1, 1, 1],
          [2, 2, 2, 2]]
n_4 = 2
print(number_on_full_parking_lots(cars_4, n_4))
