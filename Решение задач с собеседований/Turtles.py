"""
Широко известна следующая задача для младших школьников. Три черепахи ползут по
дороге. Одна черепаха говорит: "Впереди меня две черепахи". Другая черепаха гово-
рит: "Позади меня две черепахи". Третья черепаха говорит: "Впереди меня две чере-
пахи и позади меня две черепахи". Как такое может быть? Ответ: третья черепаха
врёт!
По дороге одна за другой движутся N черепах. Каждая черепаха говорит фразу вида:
"Впереди меня ai черепах, а позади меня bi черепах". Ваша задача определить,
сколько самое большое количество черепах могут говорить правду.
Example:
    N = 3
    a = [0, 2, 2]
    b = [2, 0, 2]
Answer:
    nswr = 2
"""


def right_turtles(f, s):
    used_before = set()
    n = len(f)
    for i in range(n):
        a = f[i]
        b = s[i]
        if a + b == n - 1 and a >= 0 and b >= 0:
            used_before.add(a)
    return len(used_before)


# Raw Example
n = int(input())
used_before = set()
for i in range(n):
    a, b = map(int, input().split())
    if a + b == n - 1 and a >= 0 and b >= 0:
        used_before.add(a)
print(len(used_before))


# Function Example
a = [0, 2, 2]
b = [2, 0, 2]
print(right_turtles(a, b))
