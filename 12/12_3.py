# БСБО-05-19 Савранский Сергей

goods = [[input("Name >> "), input("Quantity >> ")] for i in range(int(input("N >> ")))]

for elem in goods[::-1]:
    print(elem[0], elem[1])
