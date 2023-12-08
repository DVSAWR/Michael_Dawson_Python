import re


dict_1 = {'python': 'питон',
          'quesadilla': 'кесадилья'
          }


print(dict_1['quesadilla'])

target = 'кесадилья'

print('\nlist')
key = [key for key in dict_1 if dict_1[key] == target]
print(key)

print('\nlist.index()')
keys = list(dict_1.keys())
inx = list(dict_1.values()).index(target)
key = keys[inx]
print(key)

print('\ndict.items()')
key = [key for key, value in dict_1.items() if value == target]
print(key)

print('\nlambda filter()')
key = list(filter(lambda  key: dict_1[key] == target, dict_1))
print(key)


print('\nre')
pattern = re.compile(r'\b' + re.escape(target) + r'\b')

key = next((k for k, v in dict_1.items() if pattern.search(v)), None)

if key:
    print(target, key)
else:
    print(target, 'ERROR')

