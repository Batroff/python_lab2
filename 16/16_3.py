# БСБО-05-19 Савранский Сергей

def arr_minus(a, i, j, val):
    a[i][j] = a[i][j] - val if a[i][j] > val else 0


N = int(input('N >> '))
arr = [[int(input('Val >> ')) for i in range(N)] for j in range(N)]

anti = [[int(input(f'Pos {i} >> ')) for i in range(2)] for k in range(int(input('K >> ')))]

for (y, x) in anti:

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):

            if 0 <= i < len(arr) and 0 <= j < len(arr[i]):
                if i == x and j == y:
                    arr_minus(arr, i, j, 8)
                else:
                    arr_minus(arr, i, j, 4)

for line in arr:
    print(*(i for i in line), sep=' ', end='\n')
