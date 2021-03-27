# БСБО-05-19 Савранский Сергей

LOWER_CASE_START = 1040
LOWER_CASE_END = 1071
UPPER_CASE_START = 1072
UPPER_CASE_END = 11103

shift = int(input("Shift >> "))
msg = input("Message >> ")

res = ''
for ch in msg:
    code = ord(ch)
    if LOWER_CASE_START <= code <= LOWER_CASE_END:
        res += chr((code + shift - LOWER_CASE_START) % 31 + LOWER_CASE_START)
    elif UPPER_CASE_START <= code <= UPPER_CASE_END:
        res += chr((code + shift - UPPER_CASE_START) % 31 + UPPER_CASE_START)
    else:
        res += ch

print(res)
