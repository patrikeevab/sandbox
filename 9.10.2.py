"""
Программа принимает на вход строку. Напиши код, который убирает все повторяющиеся символы из этой строки и
выводит на печать получившуюся строку. Порядок символов должен сохраниться.
"""
string = input()
char_set = []
for char in string:
    if char not in char_set:
        char_set.append(char)
print(''.join(char_set))

"""
красивое решение
ls = input()
print("".join(sorted(set(ls), key=ls.index)))
"""
