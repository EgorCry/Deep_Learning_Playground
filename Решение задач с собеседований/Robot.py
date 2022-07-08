"""
В процессе сборки двигателя могут встречаться операции 26 типов, которые обознача-
ются строчными буквами латинского алфавита. Процесс сборки состоит из N операций.
Предполагается использовать робота один раз для выполнения части подряд идущих опе-
раций из процесса сборки.
Память робота состоит из К ячеек, каждая из которых содержит одну операцию. Опера-
ции выполняются последовательно, начиная с первой, в том порядке, в котором они
расположены в памяти. Выполнив последнюю из них, робот продолжает работу с первой.
Робота можно остановить после любой операции. Использование робота экономически
целесообразно, если он выполнит хотя бы К+1 операцию.
Требуется написать программу, которая по заданному процессу сборки определит коли-
чество экономически целесообразных способов использования робота.
N <= 2_000_000
"""


def robot(memory, string):
    nswr = 0
    temp_len = 0
    for i in range(memory, len(string)):
        if string[i] == string[i - k]:
            temp_len += 1
            nswr += temp_len
        else:
            temp_len = 0
    return nswr


s = 'abcabcac'
k = 3
print(robot(k, s))
