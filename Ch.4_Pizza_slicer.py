print('CUT "PIZZA"')

word = 'pizza'

start = None


while start != '':
    start = (input('\nStart pos: '))
    if start:
        start = int(start)
        finish = int(input('End pos: '))
        print(word[start:finish])

input('\n\nPress Enter to Exit')
