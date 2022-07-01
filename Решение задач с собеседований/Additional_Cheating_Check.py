"""
В первой строке вводится число n - количество ключевых слов в языке (0 <= n <= 50)
и два слова C и D, каждое из которых равно либо "yes", либо "no". Слово C равно
"yes" , если идентификаторы и ключевые слова в языке чувствительны к регистру сим-
волов, и "no", если нет. Слово D равно "yes", если идентификаторы в языке могут на-
чинаться с цифры, и "no", если нет.
Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита
и символов подчёркивания - ключевые слова. Все ключевые слова непусты, различны,
при этом, если язык не чувствителен к регистру, то различны и без учёта регистра.
Длина каждого слова не превышает 50 символов.
Далее до конца входных данных идёт текст программы. Он содержит только символы с
ASCII-кодами от 32 до 126 и переводы строки.
Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один
идентификатор.
Выведите идентификатор, встречающийся в программе максимальное число раз. Если та-
ких идентификаторов несколько, следует вывести тот, который встречается в первый
раз раньше. Если язык во входных данных не чувствителен к регистру, то можно выво-
дить идентификатор в любом регистре.
"""


def only_letters_digits_and_underscore(line):
    ans = []
    for c in line:
        if c.isalpha() or c.isdigit() or c == ' ':
            ans.append(c)
        else:
            ans.append(' ')
    return ''.join(ans)


def is_correct(word,st_digit):
    if word.isdigit():
        return False
    if not word[0].isdigit() or st_digit:
        return True
    return False


fin = open('input_a_c_c.txt', 'r')
keywords = set()
n, case_sens, st_digit = fin.readline().strip().split()
n = int(n)
case_sens = case_sens == 'yes'
st_digit = st_digit == 'yes'
for _ in range(n):
    keyword = fin.readline().strip()
    if not case_sens:
        keyword = keyword.lower()
    keywords.add(keyword)
cnt_pos_ids = {}
word_number = 0
for line in fin.readlines():
    line = only_letters_digits_and_underscore(line.strip())
    words = line.split()
    for word in words:
        if not case_sens:
            word = word.lower()
        if word in keywords:
            continue
        if is_correct(word, st_digit):
            word_number += 1
            if word not in cnt_pos_ids:
                cnt_pos_ids[word] = [0, word_number]
            cnt_pos_ids[word][0] += 1
best_word = ''
max_cnt_pos = [0, 0]
for word in cnt_pos_ids:
    if cnt_pos_ids[word][0] > max_cnt_pos[0]:
        max_cnt_pos = cnt_pos_ids[word]
        best_word = word
    if cnt_pos_ids[word][0] == max_cnt_pos[0] and cnt_pos_ids[word][1] < max_cnt_pos[1]:
        max_cnt_pos = cnt_pos_ids[word]
        best_word = word
print(best_word)
