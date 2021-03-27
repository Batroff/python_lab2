# БСБО-05-19 Савранский Сергей

products = [input("Product >> ") for i in range(int(input("M >> ")))]

result = []
for i in range(int(input("N >> "))):
    food = input("Food >> ")
    needs = [input("Ingredient >> ") for j in range(int(input("Ingredient quantity >> ")))]
    if all(need in products for need in needs):
        result.append(food)

print('\n'.join(result))
