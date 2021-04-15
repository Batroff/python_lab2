# БСБО-05-19 Савранский Сергей

is_allowed = [input('Allowed >> ') for a in range(int(input('N >> ')))]
to_check = [input('Check >> ') for c in range(int(input('K >> ')))]


def check(a, f):
    allow = [x.split('/')[1:] for x in a]
    file = f.split('/')[1:]

    for x in allow:
        if len(file) < len(x):
            continue
        else:
            if x == file[:len(x)]:
                return 'YES'

    return 'NO'


for f in to_check:
    print(check(is_allowed, f))
