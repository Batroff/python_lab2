# БСБО-05-19 Савранский Сергей

alph = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
        'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
        'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
        'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'y',
        'э': 'e', 'ю': 'iu', 'я': 'ia'}

text = ''
for i in input('Text >> '):
    text += alph.get(i.lower(), i.lower()).upper() if i.isupper() else alph.get(i, i)

print(text)
