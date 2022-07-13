"""
Требуется написать программу, которая позволяет выбрать минимальное число блоков,
которые, будучи установленными на указанных подрядчиками местах, образуют покрытие,
либо определить, что этого сделать невозможно. Высота, на которой образуется перек-
рытие, не имеет значения.
N <= 100_000
"""


n, w, l = map(int, input().split())
total_area = w * l
events = []
for i in range(1, n + 1):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    area = abs(x2 - x1) * abs(y2 - y1)
    events.append((z1, 1, area, i))
    events.append((z2, -1, area, i))
events.sort()
min_used = n + 1
now_used = 0
now_area = 0
for event in events:
    if event[1] == 1:
        now_used += 1
        now_area += event[2]
        if now_area == total_area and now_used < min_used:
            min_used = now_used
    else:
        now_used -= 1
        now_area -= event[2]
if min_used == n + 1:
    print('NO')
else:
    print('YES')
    print(min_used)
    used_blocks = set()
    for event in events:
        if event[1] == 1:
            now_used += 1
            used_blocks.add(event[3])
            now_area += event[2]
            if now_area == total_area and now_used == min_used:
                print(*used_blocks)
                break
        else:
            now_used += 1
            used_blocks.remove(event[3])
            now_area -= event[2]
