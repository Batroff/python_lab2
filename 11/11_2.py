# БСБО-05-19 Савранский Сергей

lines = [input("Line >> ").lstrip("%%") for i in range(int(input("N >> ")))]
lines = filter(lambda line: not line.startswith("####"), lines)

print(list(lines))
