# БСБО-05-19 Савранский Сергей

names = {}
for i in range(int(input("N >> "))):
    name = input("Name >> ")
    names[name] = 1 if name not in names.keys() else names[name] + 1

print(sum(
    filter(lambda ctr: ctr > 1, names.values())
))
