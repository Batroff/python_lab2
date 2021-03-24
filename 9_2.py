# БСБО-05-19 Савранский Сергей

names = {}
lessons = int(input("Pages >> "))

for page in range(lessons):
    for line in range(int(input("Lines >> "))):
        student = input("Student >> ")

        if student in names.keys():
            names[student] += 1
        else:
            names[student] = 1

print('\n'.join(
    filter(lambda name: names[name] == lessons, names.keys())
))
