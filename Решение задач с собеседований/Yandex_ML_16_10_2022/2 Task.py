def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs


with open('input.txt') as f:
    bottles = [i for i in f.readline()]

s = set()
for i in range(len(bottles)):
    a = combs(bottles)[1:]
    for i in a:
        s.add(''.join([str(j) for j in i]))
    bottles = [bottles[-1]] + bottles[:-1]
print(len(s), s)