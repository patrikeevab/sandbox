days_in_month=[31,29,31,30,31,30,31,31,30,31,30,31]
zodiaс=[('Козерог', 22, 12, 19, 1),
    ('Водолей', 20, 1, 18, 2),
    ('Рыбы', 19, 2, 20, 3),
    ('Овен', 21, 3, 19, 4),
    ('Телец', 20, 3, 20, 5),
    ('Близнецы', 21, 5, 20, 6),
    ('Рак', 21, 6, 22, 7),
    ('Лев', 23, 7, 22, 8),
    ('Дева', 23, 8, 22, 9),
    ('Весы', 23, 9, 22, 10),
    ('Скорпион', 23, 10, 21, 11),
    ('Стрелец', 22, 11, 21, 12)]

month, day = input().split()

if (not month.isnumeric()) or (not day.isnumeric()):
    print('некорректная дата')
    exit()

month = int(month)
day = int(day)

if month < 1 or month > 12:
    print('некорректная дата')
    exit()

if days_in_month[month-1] < day or day < 1:
    print('некорректная дата')
    exit()

for i in range(12):
    if month == zodiaс[i][2] and day >= zodiaс[i][1] or month == zodiaс[i][4] and day <= zodiaс[i][3]:
        print(zodiaс[i][0])
        exit()

