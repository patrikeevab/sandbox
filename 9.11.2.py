"""
Напиши код, который принимает на вход строку, в этой строке чётное количество слов, разделённых пробелами
(2, 4, 6, 8 или больше слов). Сформируй словарь таким образом, чтобы нечётные слова были ключами словаря,
а чётные — значениями по этим ключам. Выведи этот словарь на печать таким образом
(словарь в примере хранится в переменной my_dict):

import json
print(json.dumps(my_dict, ensure_ascii=False))

Здесь импортируется модуль json и вызывается функция dumps, определённая в нём. Функция json.dumps
выполняет преобразование переданного в неё словаря в формат данных JSON.

Например, программа вызывается так:

echo "name Пётр phone 02 sex male balance 50000" | python3.9 gen_dict.py
и она печатает:

{"name": "Пётр", "phone": "02", "sex": "male", "balance": "50000", }
Если количество слов нечётное — программа игнорирует последнее слово.
"""
import json

w = input().split(' ')
d = dict(zip([w[i] for i in range(len(w)) if not i % 2],
             [w[i] for i in range(len(w)) if i % 2]))
d["special_key"] = 12
print(json.dumps(d, ensure_ascii=False))

"""
Красивые решения

import json
word_list = input().split()
print(json.dumps(dict(zip(word_list[::2], word_list[1::2])), ensure_ascii=False))

import json
data = input().split()
output = {data[i]: data[i+1] for i in range(0, len(data) - 1, 2)}
print(json.dumps(output, ensure_ascii=False))

"""
