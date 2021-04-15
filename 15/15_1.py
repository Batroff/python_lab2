# БСБО-05-19 Савранский Сергей

letter = input("Letter >> ")
phrase = input("Phrase >> ")

print(*(word for word in phrase.split(' ') if letter in word.lower()), sep='\n')
