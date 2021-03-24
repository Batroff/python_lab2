# БСБО-05-19 Савранский Сергей

msg = input("Message >> ")
index = int(input("Index >> "))

print(msg[index - 1] if index - 1 < len(msg) and index > 0 else "ОШИБКА")
