"""
Учительница задала ПЕТЕ домашнее задание - в заданном тексте расставить ударения в
словах, после чего поручила ВАСЕ проверить это домашнее задание. ВАСЯ очень плохо
знаком с данной темой, поэтому он нашёл словарь, в котором указано, как ставятся
ударения в словах. К сожалению, в этом словаре присутствуют не все слова. ВАСЯ ре-
шил, что в словах, которых нет в словаре, он будет считать, что ПЕТЯ поставил уда-
рение правильно, если в этом слове ПЕТЕЙ поставлено ровно одно ударение. Оказалось,
что в некоторых словах ударение может быть поставлено больше, чем одним способом.
ВАСЯ решил, что в этом случае если то, как ПЕТЯ поставил ударение, соответствует
одному из приведённых в словаре вариантов, он будет засчитывать это как правиль-
ную расстановку ударения, а если не соответствует, то как ошибку. Вам дан словарь,
которым пользовался ВАСЯ и домашнее задание, сданное ПЕТЕЙ. Ваша задача - опреде-
лить количество ошибок, которое в этом задании насчитает ВАСЯ.
EXAMPLE:
4
cAnnot
cannOt
fOund
pAge
thE pAge cAnnot be found.
ANSWER:
2
"""


def to_dict(words):
    nswr = {}
    for i in range(len(words)):
        if words[i].lower() not in nswr:
            nswr[words[i].lower()] = set()
        nswr[words[i].lower()].add(words[i])
    return nswr


def check_stress(word):
    nswr = 0
    for i in word:
        if i != i.lower():
            nswr += 1
    if nswr != 1:
        return True
    return False


def main_function(words, rqst):
    dict_words = to_dict(words)
    errors = 0
    for word in rqst.split():
        if word.lower() in dict_words:
            if word not in dict_words[word.lower()]:
                errors += 1
        else:
            if check_stress(word):
                errors += 1
    return errors


# Example
n = 4
words = ['cAnnot', 'cannOt', 'fOund', 'pAge']
rqst = 'thE pAge cAnnot be found.'
print(main_function(words, rqst))
