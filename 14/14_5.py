# БСБО-05-19 Савранский Сергей

queries = input("URL >> ").split('/')[-1].split('?')[-1].split('&')
to_find = input('Query >> ')
print([q for q in queries if to_find in q][0].split('=')[-1])
