import random

count = 0
h_count = 0
t_count = 0

while count < 1000:
    x = random.randint(1, 2)
    if x == 1:
        h_count += 1
        count += 1
    if x == 2:
        t_count += 1
        count += 1


print(f'\nCOUNT: {count}\n'
      f'HEADS: {h_count}\n'
      f'TAILS: {t_count}\n')
