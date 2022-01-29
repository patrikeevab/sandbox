"""
Напиши программу, которая принимает на вход строку с JSON. Этот JSON надо разобрать и напечатать с помощью pprint.
Если на вход передан некорректный JSON, программа печатает: некорректный JSON.
Напоминаю, что программы на степике принимают на вход данные через input(), не через sys.argv.
Sample Input:
[{"phone": "01", "name": "John"}, "2", {"phone": "033", "name": "Vasya"}, "4", {"phone": "777", "name": "Daniel"}]
Sample Output:
[{'name': 'John', 'phone': '01'},
 '2',
 {'name': 'Vasya', 'phone': '033'},
 '4',
 {'name': 'Daniel', 'phone': '777'}]
"""

import json
from pprint import pprint

str = '[{"phone": "01", "name": "John"}, "2", {"phone": "033", "name": "Vasya"}, "4", {"phone": "777", "name": "Daniel"}]'

#my_dict = json.loads(input())
try:
    my_dict = json.loads(str)
    pprint(my_dict)
except:
    print('некорректный JSON')




