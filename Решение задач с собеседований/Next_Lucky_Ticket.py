"""
Однажды Адлет ехал домой на автобусе и обратил внимание,
что номер на его билете не был счастливым. На каждом
автобусном билете — шестизначное число. Счастливый
билет — тот, в котором сумма первых трех цифр этого
числа равна сумме трех последних. Например, число
201111 — счастливое, так как суммы первых
(2 + 0 + 1 = 3) и последних (1 + 1 + 1 = 3) трех цифр
одинаковы. Поскольку номер на билете не был счастливым,
Адлет захотел найти следующее ближайшее счастливое
число. Например, если номер билета —165901, то
счастливым (в последовательности возрастания) будет
билет 165903. Учитывая текущий номер билета Адлета,
найдите и выведите ближайший (из следующих за ним)
счастливый номер.
Формат ввода
Первая строка содержит целое число number
(100000 ≤ number ≤ 999999) - шестизначный номер билета.
Формат вывода
Для числа во входных данных найдите и выведите следующее
счастливое число. Гарантируется что такое число существует.
ПРИМЕР А:
Ввод: 165901 Вывод: 165903
ПРИМЕР В:
Ввод: 100000 Вывод: 100001
"""


def lucky_ticket(ticket):
    while True:
        f, s = ticket // 1000, ticket % 1000
        if sum(map(int, list(str(f)))) == sum(map(int, list(str(s)))):
            return ticket
        if sum(map(int, list(str(f)))) < list(map(int, list(str(f))))[2]:
            f += 1
            s = 1
            ticket = f * 1_000 + s
        else:
            ticket += 1

        
print(lucky_ticket(101002))
print(lucky_ticket(165901))
print(lucky_ticket(100000))
print(lucky_ticket(100900))
print(lucky_ticket(113600))
print(lucky_ticket(831108))
print()


# Test Time Section (Run in Terminal for showing the Bar)
# import time
# from progress.bar import IncrementalBar
#
# bar = IncrementalBar('Countdown', max=999_999 - 100_000)
# for i in range(100_000, 200_000):
#     start_time = time.time()
#     lucky_ticket(i)
#     end_time = time.time() - start_time
#     if end_time >= 1.0:
#         print(end_time)
#     bar.next()
