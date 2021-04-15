# БСБО-05-19 Савранский Сергей

line = input("Line >> ")

while len(line) > 2:
    print(line)
    line = line[1:-1:]
print(line)