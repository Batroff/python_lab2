# БСБО-05-19 Савранский Сергей

series = []

for i in range(int(input("N >> "))):
    ctr = 0

    for index in range(len(series)):
        if list(reversed(series))[index] == series[index]:
            ctr += 1

    series.append(ctr)

for num in series:
    print(num)
