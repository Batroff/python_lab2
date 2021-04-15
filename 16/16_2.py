# БСБО-05-19 Савранский Сергей

lines = [input('Line >> ').split(',') for i in range(int(input('N >> ')))]
pos = [input('Position >> ') for j in range(int(input('K >> ')))]

for p in pos:
    y, x = map(lambda i: int(i), p.split(','))
    print(lines[y][x])
