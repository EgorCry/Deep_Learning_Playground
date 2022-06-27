'''
Найти подстроку в строке S с максимальной длиной уникальных символов.
'''


def longest_unic_symbols(text):
    letters = dict()
    max_len = 0

    for i in range(len(text)):
        if text[i] not in letters:
            letters[text[i]] = 1
        elif text[i] in letters or i == len(text) - 1:
            letters = dict({text[i]: 1})

        current_len = len(letters)
        if current_len > max_len:
            max_len = current_len

    return max_len


assert(longest_unic_symbols('') == 0)
# print(longest_unic_symbols('ab'))
assert(longest_unic_symbols('abcdee') == 5)
assert(longest_unic_symbols('aabcabcbbddee') == 3)
