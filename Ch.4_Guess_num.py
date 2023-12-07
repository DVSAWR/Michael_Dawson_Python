import random

num = random.randint(1, 100)
print(f'HIDDEN NUM: {num}\n')

count = 1
print('GUESS THE HIDDEN NUM (1 - 100) IN 10 TURNS\n')
print(f'TURN COUNT {count}')

def your_guess():
    while True:
        guess = input('YOUR GUESS?: ')
        if guess.isdigit():
            guess = int(guess)
            return guess
        else:
            print('ENTER NUMBER')
            continue

guess = your_guess()

while True:
    if guess > num:
        print('LESS')

    if guess < num:
        print('MORE')

    if guess == num:
        print(f'RIGHT! NUM WAS: {num}')
        break

    count += 1
    print(f'\nTURN COUNT: {count}')

    guess = your_guess()

    if count >= 10:
        print(f'\nGAME OVER\nTURN COUNT MORE THAN 10')
        break

    if guess == num:
        print(f'RIGHT! HIDDEN NUM WAS: {num}')
        break


print('\n----------------------------\n')

print('COMPLUCTER TURN')

count = 1
comp_min = 0
comp_max = 100

while True:
    num = input('ENTER HIDDEN NUM (1 - 100): ')

    if num.isdigit():
        num = int(num)
        break

    else:
        print('ENTER NUMBER')
        continue

while True:
    print(f"\nCOMP'S TURN COUNT: {count}")

    comp_guess = int((comp_min + comp_max) / 2)

    if comp_guess < num:
        comp_min = comp_guess
        count += 1
        print(comp_guess)

    if comp_guess > num:
        comp_max = comp_guess
        count += 1
        print(comp_guess)

    if comp_guess == num:
        print(comp_guess)
        print(f'\nRIGHT! HIDDEN NUM WAS: {num}')
        print(f"COMPLUCTER FIND NUM IN {count} TURNS\n")
        break

    if count > 10:
        print(f'GAME OVER\nTURN COUNT MORE THAN 10')
        break
