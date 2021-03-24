# БСБО-05-19 Савранский Сергей

commands = input()
SYMBOL = commands[0]
SPACE = ' '

space_ctr = 0
line = SYMBOL
for ch in commands[1::]:
    if ch == '>':
        space_ctr += 1
        line += SYMBOL
    elif ch == 'V':
        print(line)
        line = SPACE * space_ctr + SYMBOL
    elif ch == '<':
        space_ctr -= 1
        line = SPACE * space_ctr + SYMBOL * (line.count(SYMBOL) + 1)
print(line)
