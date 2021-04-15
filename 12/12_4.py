# БСБО-05-19 Савранский Сергей

message = input("Message >> ")

ctr = 0
last_ch = message[0]
for ch in message:
    if ch == last_ch:
        ctr += 1
    else:
        print(ctr, last_ch)
        ctr = 1
    last_ch = ch
print(ctr, last_ch)
