# БСБО-05-19 Савранский Сергей

N = int(input("N >> "))
half = (N + 1) // 2
teams = {input("Team >> "): int(input("Score >> ")) for i in range(N)}
teams = [(k, v) for k, v in sorted(teams.items(), key=lambda item: item[1], reverse=True)]

print(*(t[0] for t in sorted(teams[:half:])), sep='\n')
print(*(t[0] for t in sorted(teams[half::])), sep='\n')
