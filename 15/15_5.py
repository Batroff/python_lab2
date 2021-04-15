# БСБО-05-19 Савранский Сергей

import re

commands = [input('Line >> ') for i in range(int(input('N >> ')))]
people = []

for command in commands:
    if re.match('.* встал(а)? в очередь.', command):
        people.append(command.split(' ')[0])
    elif re.match('Привет, .*! .* будет за тобой.', command):
        people.insert(
            people.index(command.split("! ")[0].split(" ")[-1]) + 1,
            command.split("! ")[-1].split(" ")[0]
        )
    elif re.match('.*, хватит тут стоять, пошли отсюда.', command):
        people.remove(command.split(', ')[0])

print(*(p for p in people), sep='\n')
