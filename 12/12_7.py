# БСБО-05-19 Савранский Сергей

N = int(input("N >> "))
M = int(input("M >> "))

lines = [input() for i in range(N)]

for line in lines[::2]:
    for ch in line[::2]:
        print(ch, end='')
    print()
