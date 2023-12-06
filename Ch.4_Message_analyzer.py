print('Анализ текста')

message = input('Введите текст: ')

print(f'\nДлина текста: {len(message)}')

letter = input('Введите букву: ')

if letter in message:
    print(f'{letter} встречается в тексте')
else:
    print(f'{letter} не встречается в тексте')
    