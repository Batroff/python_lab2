# БСБО-05-19 Савранский Сергей

M = int(input("M >> "))
N = int(input("N >> "))

home = [input("Home book >> ") for i in range(M)]
read = [input("Book >> ") for i in range(N)]

result = [any(book == to_read for book in home) for to_read in read]
print('\n'.join(list(map(lambda res: "YES" if res == True else "NO", result))))
