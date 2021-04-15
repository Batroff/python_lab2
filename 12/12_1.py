# БСБО-05-19 Савранский Сергей

white = [input("White >> ") for i in range(int(input("N >> ")))]
queries = [input("Query >> ") for i in range(int(input("M >> ")))]

print('\n'.join(
    list(filter(lambda query: query in white, queries))
))
