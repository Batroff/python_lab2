# БСБО-05-19 Савранский Сергей

from re import split

goods_quantity, summary = list(map(
    lambda num: int(num), split("\s+", input("N, SUM >> "))
))

goods_sum = 0
errors = []
for i in range(goods_quantity):
    cost, quantity, theory_multiply = list(map(
        lambda num: int(num), split("\s+[*=]", input("Cost, quantity, summary >> "))
    ))
    multiply = cost * quantity

    goods_sum += multiply
    if multiply != theory_multiply:
        errors.append(str(i + 1))

print(summary - goods_sum)
print(" ".join(errors))
