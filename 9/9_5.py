# БСБО-05-19 Савранский Сергей

food = [input("Food >> ") for i in range(int(input("M >> ")))]

was = []
for i in range(int(input("N >> "))):
    was += [input("Food >> ") for j in range(int(input("K >> ")))]

print('\n'.join(list(filter(lambda f: f not in was, food))))
