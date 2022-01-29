"""
Программа принимает на вход словарь в JSON формате, значения являются целыми числами.
Программа находит минимальное значение по словарю и печатает ключ этого значения.
{"key1": 123, "key2": 11, "key3": 110000, "key4": 50}
"""

import json

my_dict = json.loads(input())

m = min(my_dict.values())

for k in my_dict:
    if my_dict[k] == m:
        print(k)
        exit()

"""
Красивое решение

import json
my_dict = json.loads(input())
print(min(my_dict, key=my_dict.get))

"""