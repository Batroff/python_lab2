# БСБО-05-19 Савранский Сергей

import statistics


data = [list(map(lambda x: int(x), input('Line >> ').split(' '))) for line in range(int(input('N >> ')))]

med1 = [statistics.median(series) for series in data]
mod1 = [statistics.mode(series) for series in data]
med2 = statistics.median(med1)
mod2 = statistics.mode(mod1)
all_data = sum(data, [])

print(*(i for i in med1))
print(*(i for i in mod1))
print(med2)
print(mod2)
print(statistics.median(all_data))
print(statistics.mode(all_data))
