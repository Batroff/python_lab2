# БСБО-05-19 Савранский Сергей

message = input("Message >> ")
index = int(input("Index >> ")) - 1
favourite = input("Fav char >> ")

print(index, len(message))
if len(favourite) != 1 or index >= len(message):
    print("ОШИБКА")
else:
    print("ДА" if message[index] == favourite else "НЕТ")
