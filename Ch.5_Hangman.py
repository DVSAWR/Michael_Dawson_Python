import random

HANGMAN = (
    '''
    7 HP
    ''',
    '''
    6 HP
    ''',
    '''
    5 HP
    ''',
    '''
    4 HP
    ''',
    '''
    3 HP
    ''',
    '''
    2 HP
    ''',
    '''
    1 HP
    ''',
    '''
    0 HP
    '''
)

MAX_WRONG = len(HANGMAN) - 1

WORDS = ('OVERUSED', 'CALM', 'GUAM', 'TAFFETA', 'PYTHON')

word = random.choice(WORDS)

so_far = '*' * len(word)

wrong = 0

used = []

while wrong < MAX_WRONG and so_far != word:
    print(f'TR: {HANGMAN[wrong]}')
    print(f'USED LETTERS: {used}')
    print(f'WORD: {so_far}')

    guess = input('\nENTER LETTER: ')
    guess = guess.upper()
    if len(guess) > 1:
        print('\nJUST ONE LETTER\n')
        continue

    while guess in used:
        print(f'YOU ALREADY TRY THIS LETTER <{guess}>')
        guess = input('\nENTER LETTER: ')
        guess = guess.upper()
    used.append(guess)



    if guess in word:
        print(f'\nYES, <{guess}> IN WORD')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print(f'\nNO, <{guess}> NOT IN WORD')
        wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print('YOU LOSE')
    if word == so_far:
        print('\n\nYOU WIN')
        print(f'WORD: {word}')

input('\n\nPress Enter to Exit')

