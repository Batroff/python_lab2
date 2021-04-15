# БСБО-05-19 Савранский Сергей

data = list(map(lambda x: int(x), input('Data >> ').split(' ')))
data_len = len(data)
graph_height = 2 + max(data)

for i in range(graph_height):
    if i == 0:
        print('*' * (data_len + 2))
    elif i == 1:
        print(f'*{" " * data_len}*')
    else:
        line = ''
        for j in data:
            line += '*' if j + i >= graph_height else ' '
        print(f'*{line}*')
