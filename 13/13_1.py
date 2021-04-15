# БСБО-05-19 Савранский Сергей

thimbles = {i: input() for i in range(1, int(input("N >> ")) + 1)}

for i in range(int(input("K >> "))):
    tempThimbles = {}
    for j in range(1, int(input("Remained >> ")) + 1):
        tempThimbles[j] = thimbles[int(input())]
    thimbles = tempThimbles

for value in thimbles.values():
    print(value)
