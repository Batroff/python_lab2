# БСБО-05-19 Савранский Сергей

N = int(input('N >> '))
s = [[]]

for i in range(N - 1):
    s.append([int(j) for j in input('Values >> ').split()])

path = input('Path >> ').split()

a, a1 = int(path[0]), int(path[1])

path_len = s[max(a, a1)][min(a, a1)]
b = -1

for i in range(N):
    if i != a and i != a1:
        if path_len > s[max(a, i)][min(a, i)] + s[max(i, a1)][min(i, a1)]:
            path_len = s[max(i, a1)][min(i, a1)] + s[max(i, a1)][min(i, a1)]
            b = i

if b != -1:
    print(b)
else:
    print(a)
