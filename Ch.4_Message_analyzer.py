print('Text analyze')

message = input('Enter text: ')

print(f'\nText len: {len(message)}')

letter = input('Enter letter: ')

if letter in message:
    print(f'{letter} in text')
else:
    print(f'{letter} not in text')
