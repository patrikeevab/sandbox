"""
Напиши код, который уберёт дубли строк из переданных на вход данных, и выведет строки в алфавитном порядке.
Во входных данных строки разделяются символом |. В выходных данных строки разделяются символом перевода каретки \n.
"""
print("\n".join(sorted(set(input().split('|')))))

