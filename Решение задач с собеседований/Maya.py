"""
Одна из проблем расшифровки письменности Майя заключается в определении этого по-
рядка. Рисуя значки некоторого слова, писатели Майя иногда выбирали позиции для
значков, исходя, скорее, из эстетических взглядов, а не определённых правил. Это
привело к тому, что, хотя звуки для многих значков известны, археологи не всегда
уверены, как должно произноситься записанное слово.
Археологи ищут некоторое слово W. Они знают значки для него, но не знают все воз-
можные способы их расположения. Вам дадут g значков, составляющих слово W, и пос-
ледовательность S всех значков в надписи, которую они изучают, в порядке их появ-
ления. Помогите им, подсчитав количество возможных появлений слова W.
Задание.
Напишите программу, которая по значкам слова W и по последовательности S значков
надписи подсчитывает количество всех возможных вхождений слова W в S, то есть
количество всех различных позиций идущих подряд g значков в последовательности
S, которые являются какой-либо перестановкой значков слова W.
Example:
4 9
abca
bcaabmbca
Answer:
2
"""


def to_dict(word):
    nswr = {}
    for i in word:
        if i not in nswr:
            nswr[i] = 0
        nswr[i] += 1
    return nswr


def dict_comparison(d_1, d_2):
    match = 0
    for i in d_1:
        if i in d_2 and d_1[i] == d_2[i]:
            match += 1
    return match


def dict_modification(s_d, w_d, symbol, count_mod):
    nswr = 0
    if symbol not in s_d:
        s_d[symbol] = 0
    if symbol in w_d and s_d[symbol] == w_d[symbol]:
        nswr -= 1
    s_d[symbol] += count_mod
    if symbol in w_d and s_d[symbol] == w_d[symbol]:
        nswr = 1
    return nswr


lenW, lenS = map(int, input().split())
w, s = input(), input()
w_dict = to_dict(w)
s_dict = to_dict(s[:len(w)])
matching_counter = dict_comparison(w_dict, s_dict)
occurrences = 0
if matching_counter == len(w_dict):
    occurrences += 1
for i in range(lenW, lenS):
    matching_counter += dict_modification(s_dict, w_dict, s[i - lenW], -1)
    matching_counter += dict_modification(s_dict, w_dict, s[i], +1)
    if matching_counter == len(w_dict):
        occurrences += 1
print(occurrences)
