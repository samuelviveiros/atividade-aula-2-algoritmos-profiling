from random import randint

print('Generating `one_million.txt`...')
with open('one_million.txt', 'w') as numbers:
    count = 1_000_000
    i = 0
    while i < count:
        numbers.write(f'{str(randint(1, 1_000_000))}\n')
        i += 1

print('Generating `one_billion.txt`...')
with open('one_billion.txt', 'w') as numbers:
    count = 1_000_000_000
    i = 0
    while i < count:
        numbers.write(f'{str(randint(1, 1_000_000_000))}\n')
        i += 1
