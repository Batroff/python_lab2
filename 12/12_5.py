# БСБО-05-19 Савранский Сергей

num = int(input("Num >> "))

remainders = []
period = ""
remainder = 1

while not (remainder in remainders):
    remainders.append(remainder)
    period += str(remainder // num)
    remainder = (remainder % num) * 10

period = period[remainders.index(remainder):]

print(period)
