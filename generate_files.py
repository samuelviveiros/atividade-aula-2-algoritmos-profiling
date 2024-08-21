from random import randint


print('Generating `one_million_integers.txt`...')
with open('one_million_integers.txt', 'w') as integers:
    for i in range(1_000_000 + 1):
        integers.write(str(randint(1, 1_000_000)) + '\n')

print('Generating `one_billion_integers.txt`...')
with open('one_billion_integers.txt', 'w') as integers:
    for i in range(1_000_000_000 + 1):
        integers.write(str(randint(1, 1_000_000_000)) + '\n')
