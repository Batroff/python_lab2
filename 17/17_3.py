# БСБО-05-19 Савранский Сергей

bd = {}
for i in range(int(input('N >> '))):
    name = input('Name >> ').split()
    if name[2] in bd:
        bd[name[2]].append([name[0], name[1]])
    else:
        bd[name[2]] = [[name[0], name[1]]]

arr = [input() for _ in range(int(input('K >> ')))]

for word in arr:
    if word in bd:
        arr = sorted(bd[word], key=lambda x: (int(x[1]), x[0]))
        res = ''
        for x in arr:
            res += ' '.join(x) + ' '
        print(res.rstrip())
    if word not in bd:
        print()
