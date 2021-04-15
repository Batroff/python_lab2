# БСБО-05-19 Савранский Сергей

mark = False
slash = False

char = 0
result = []

for i in range(int(input('N >> '))):
    line = input('Line >> ')
    while line[char] == " ":
        result.append(" ")
        char += 1
    for j in range(char, len(line)):
        if not slash:
            if line[j] == "'":
                result.append(line[j])
                mark = not mark
            elif line[j] == "\\":
                result.append(line[j])
                slash = True
            elif line[j] == "#":
                if mark:
                    result.append(line[j])
                else:
                    break
            elif line[j] == " ":
                if mark:
                    result.append(line[j])
                else:
                    if j + 1 != len(line):
                        if line[j + 1] == " ":
                            result.append("")
                        else:
                            result.append(line[j])
            else:
                result.append(line[j])
        else:
            slash = False
            result.append(line[j])
    print("".join(result))
    result = []
    mark = False
    slash = False
    char = 0
