"""
На парковке в торговом центре N мест (занумерованных от 1 до N). За день в ТЦ при-
езжало M автомобилей, при этом некоторые из них длинные и занимали несколько подряд
идущих парковочных мест. Для каждого автомобиля известно время приезда и отъезда, а
также два числа - с какого по какое парковочные места он занимал. Если в какой-то
момет времени один автомобиль уехал с парковочного места, то место считается осво-
бодившимся и в тот же момент времени на его место может встать другой.
Необходимо определить, был ли момент, в который были заняты все парковочные места.
"""


def is_parking_lots_full(cars, n):
    events = []
    for car in cars:
        time_in, time_out, place_from, place_to = car
        events.append((time_in - 1, 1, place_to - place_from + 1))
        events.append((time_out, -1, place_to - place_from + 1))
    events.sort()
    occupied = 0
    for i in range(len(events)):
        if occupied == n:
            return True
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
    return False


cars_1 = [[5, 5, 1, 2],
          [1, 3, 1, 1],
          [2, 3, 2, 3],
          [3, 5, 4, 6]]
n_1 = 6
print(is_parking_lots_full(cars_1, n_1))
cars_2 = [[1, 2, 1, 2],
          [1, 1, 4, 4],
          [1, 3, 6, 6],
          [3, 3, 2, 5],
          [4, 5, 1, 2],
          [4, 4, 3, 3],
          [4, 5, 4, 6]]
n_2 = 6
print(is_parking_lots_full(cars_2, n_2))
cars_3 = [[1, 1, 1, 7]]
n_3 = 7
print(is_parking_lots_full(cars_3, n_3))
cars_4 = [[1, 1, 1, 1],
          [2, 2, 2, 2]]
n_4 = 2
print(is_parking_lots_full(cars_4, n_4))
