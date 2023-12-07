import random

def dice_roll():
	dice1 = random.randrange(1, 6)
	dice2 = random.randint(1, 6)
	if dice1 == 1 and dice2 == 1:
		print(f'SNAKE EYES')
	return dice1, dice2

while True:
	input('\nPRESS ENTER TO ROLL')
	x, y = dice_roll()
	print(f'YOUR ROLL: {x} AND {y}')
