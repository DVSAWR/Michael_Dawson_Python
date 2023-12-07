import random

print('\nTRY GUESS THE HIDDEN WORD\n')

words = ('food', 'pizza')

word = random.choice(words)

x = len(word)

count = 1

lst = ['•' for i in range(x)]

indx_find = 0

def find_all_indx(txt, char):
    lst = []
    l = len(txt)
    index = 0
    while index < l:
        i = txt.find(char, index)
        if i == -1:
            return lst
        lst.append(i)
        index = i + 1
    return lst


while True:
    for i in lst:
        print(f' {i} ', end=' ')

    if ''.join(lst) in word.upper():
        print(f'\nRIGHT! THE HIDDEN WORD WAS: {word.upper()}')
        break

    print(f'\n\nTURN COUNT: {count}')
    guess = input('ENTER YOUR GUESS: ')


    indx = word.find(guess)

    if len(guess) > 1:
        if guess.lower() == word:
            print(f'RIGHT! THE HIDDEN WORD WAS: {word.upper()}')
            break
        else:
            print('RIGHT!')
    if len(guess) == 1:
        if guess in word:
            for i in find_all_indx(word, guess):
                lst[i] = word[i].upper()
            print('RIGHT!\n')
        else:
            print('WRONG!\n')
    count += 1


