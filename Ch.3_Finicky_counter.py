
count = 0
drop = 5

while True:
    count += 1
    if count > 10:
        break
    if count == drop:
        continue
    print(count)

input('\n\nНажмите Enter, чтобы выйти.')