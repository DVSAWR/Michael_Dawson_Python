import random

x = input('ENTER SMTH: ')
res = ''

for i in range(len(x)):
    pos = random.randrange(-len(x), len(x))
    print('SMTH:', x, '\tPOS: ', pos, '\t\tCHAR:', x[pos])
    res += x[pos]

print(f'\nRES: {res}')
