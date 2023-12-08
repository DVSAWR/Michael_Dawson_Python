
scores = []

choice = None

while choice != '0':
    print('''
    SCORES:
    0 - Exit
    1 - Show scores
    2 - Add score
    3 - Delete score
    4 - Sort score list
    ''')

    choice = input('Your choice: ')

    if choice == '0':
        print('BB')

    elif choice == '1':
        print('SCORES: ')
        for i in scores:
            print(i)

    elif choice == '2':
        score = input('Add your score: ')
        if score.isdigit():
            score = int(score)
            scores.append(score)

    elif choice == '3':
        score = input('Delete score: ')
        if score.isdigit():
            score = int(score)
            if score in scores:
                scores.remove(score)
        else:
            print('ERROR')

    elif choice == '4':
        scores.sort(reverse=True)
