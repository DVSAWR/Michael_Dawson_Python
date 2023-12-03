# Бросок костей - Dice roller

import random


def dice_roll():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randrange(6) + 1
    print('При вашем броске выпало', dice_1, 'и', dice_2)


count = 0

while count > -1:
    count += 1
    print('Бросок №', count)
    dice_roll()
    input()
    continue
