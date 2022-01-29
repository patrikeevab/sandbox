"""
Напиши программу, которая ищет 10 самых часто встречающихся слов в тексте.
Программа принимает на вход строку и считает количество слов в этой строке,
затем выводит на печать 10 самых частых слов. Для слов, имеющих одинаковую частотность,
сортировка осуществляется по алфавиту.
Все знаки препинания должны быть проигнорированы, в том числе тире и многоточия.
Словом считается то, что отделено пробелом, символом табуляции или символом перевода строки.
Регистр игнорируется, слово Привет и привет считаются одним и тем же словом.
Слова короче трех символов — игнорируются,  чтобы убрать самые короткие и частые слова вроде «и», «а», «не» и подобные.
Участвуют только слова, состоящие из трёх и более символов.
"""

import sys
input_strings = sys.stdin.readlines()

all_words = {}

for string in input_strings:
    for s in string.lower().split():
        chars = ""
        for c in s:
            if c.isalpha():
                chars += c
        if len(chars) > 2:
            if all_words.get(chars):
                all_words[chars] = all_words[chars] + 1
            else:
                all_words[chars] = 1

num_words = list(set({all_words[key] for key in all_words}))
num_words.sort(reverse=True)

print('10 самых часто встречающихся слов в этом тексте:\n')
cnt = 1
for num in num_words:
    words_by_num = [(k, all_words[k]) for k in all_words if all_words[k] == num]
    words_by_num.sort(key=lambda x: x[0])
    for word in words_by_num:
        print(f'{word[0]}: {word[1]}')
        if cnt == 10:
            exit()
        cnt += 1
