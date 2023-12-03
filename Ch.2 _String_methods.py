print('\n~ Исходная цитата:')
patter='Ехал Грека через реку, видит Грека — в реке рак'
print(patter)

print('\n~ .upper в верхнем регистре:')
print(patter.upper())

print('\n~ .lower в нижнем регистре:')
print(patter.lower())

print('\n~ .swapcase меняет местами регистр:')
print(patter.swapcase())

print('\n~ .capitalize первая прописная, остальные строчные:')
print(patter.capitalize())

print('\n~ .title Как заголовок, каждая первая бука прописная:')
print(patter.title())

print('\n~ .strip убраны все интервалы:')
print(patter.strip())

print('\n~ .replace с заменой:')
print(patter.replace('Грека', 'Даня'))


input('\n\nНажмите Enter, чтобы выйти.')