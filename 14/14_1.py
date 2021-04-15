# БСБО-05-19 Савранский Сергей

order = [input("Line >> ") for i in range(int(input("N >> ")))]
print(", ".join(list(line for line in order if line.find("лук") == -1)))
