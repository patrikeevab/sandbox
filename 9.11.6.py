phone_string = input()

d = "".join([c for c in phone_string.strip() if c.isdigit()])

if len(d) != 11 or d[0] not in ('7', '8', '9'):
    print(d)
    exit()

if d[0] == '7':
    d = '8' + d[1:]
if d[0] == '9':
    d = '8' + d

print(f'{d[0]} ({d[1]}{d[2]}{d[3]}) {d[4]}{d[5]}{d[6]}-{d[7]}{d[8]}-{d[9]}{d[10]}')