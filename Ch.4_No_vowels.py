message = input('Enter text: ')

new_message = ''

VOWELS = 'aeiouy'

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print(f'New message {new_message}')

print(f'\nResult: {new_message}')

input('\n\nPress Enter to Exit')
