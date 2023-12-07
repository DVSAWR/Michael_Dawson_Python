import random

words = ('puppy', 'crusader', 'book')

word = list(random.choice(words))
random.shuffle(word)
anagram = ''.join(word)

print('\n', anagram)


word = random.choice(words)
anagram2 = ''

while word:
    pos = random.randrange(len(word))
    anagram2 += word[pos]
    word = word[:pos] + word[(pos + 1):]

print('\n', anagram2)

