"""
На парковке в торговом центре N мест (занумерованных от 1 до N). За день в ТЦ при-
езжало M автомобилей, при этом некоторые из них длинные и занимали несколько подряд
идущих парковочных мест. Для каждого автомобиля известно время приезда и отъезда,а
также два числа - с какого по какое парковочное места он занимал. Если в какой-то
момент времени один автомобиль уехал с парковочного места, то место считается осво-
бодившимся и в тот же момент времени на его место может встать другой.
Необходимо определить, был ли момент, в который были заняты все парковочные места
и определить минимальное количество автомобилей, которое заняло все места, а также
номера этих автомобилей (в том порядке, как они перечисляются в списке). Если пар-
ковка никогда не была занята полностью, то вернуть пустой список.
"""


def min_cars_numbers(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append((time_in - 1, 1, place_to - place_from + 1, i))
        events.append((time_in, -1, place_to - place_from + 1, i))
    events.sort()
    occupied = 0
    cur_cars = 0
    min_cars = len(cars) + 1
    car_nums = set()
    best_car_nums = set()
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            cur_cars -= 1
            if events[i][3] in car_nums:
                car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            cur_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and cur_cars < min_cars:
            best_car_nums = car_nums.copy()
            min_cars = cur_cars
    return best_car_nums


def min_cars_numbers_effective(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append((time_in - 1, 1, place_to - place_from + 1, i))
        events.append((time_out, -1, place_to - place_from + 1, i))
    events.sort()
    occupied = 0
    cur_cars = 0
    min_cars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            cur_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            cur_cars += 1
        if occupied == n and cur_cars < min_cars:
            min_cars = cur_cars
    car_nums = set()
    cur_cars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            cur_cars -= 1
            if events[i][3] in car_nums:
                car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            cur_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and cur_cars == min_cars:
            return car_nums
    return set()


cars_2 = [[1, 2, 1, 2],
          [1, 1, 4, 4],
          [1, 3, 6, 6],
          [3, 3, 2, 5],
          [4, 5, 1, 2],
          [4, 4, 3, 3],
          [4, 5, 4, 6]]
n_2 = 6
print(min_cars_numbers(cars_2, n_2))
cars_1 = [[5, 5, 1, 2],
          [1, 3, 1, 1],
          [2, 3, 2, 3],
          [3, 5, 4, 6]]
n_1 = 6
print(min_cars_numbers_effective(cars_1, n_1))
