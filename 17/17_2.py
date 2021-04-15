# БСБО-05-19 Савранский Сергей

book = {}
for _ in range(int(input('N >> '))):
    name, number = input('Data >> ').split()
    if number in book:
        book[number].append(name)
    else:
        book[number] = [name]


for _ in range(int(input('K >> '))):
    print(*book.get(input('Name >> '), ['Нет в телефонной книге']))
