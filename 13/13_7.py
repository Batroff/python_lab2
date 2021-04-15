# БСБО-05-19 Савранский Сергей

soldiers = [input("Name >> ") for i in range(int(input("N >> ")))]
K = int(input("K >> "))

while len(soldiers) != 0:
    print(*(s for s in soldiers if soldiers.index(s) % K == 0), sep='\n')
    soldiers = [s for s in soldiers if soldiers.index(s) % K != 0]
