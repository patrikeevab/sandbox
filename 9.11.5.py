"""
Программа принимает на вход словарь в JSON формате. Если в словаре есть ключ special_key,
удали его и выведи на печать получившийся словарь, если нет — просто выведи исходный словарь.
Для форматирования словаря при печати используй json.dumps.
"""
import json

my_dict = json.loads(input())
my_dict.pop("special_key", 1)
print(json.dumps(my_dict, ensure_ascii=False))
