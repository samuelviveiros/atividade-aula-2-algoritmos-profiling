import time
from random import randint
from typing import Optional, TextIO, Tuple

import psutil 


RANDOM_INTEGER = randint(1, 1_000_000)
print(f'Random integer generated: {RANDOM_INTEGER:,}'.replace(',', '.'))


def search_integer(target: int, file: TextIO) -> Tuple[bool, Optional[int]]:
    for line, integer in enumerate(file, start=1):
        if target == int(integer):
            return True, line
    return False, None


found = False
line = None

print('Searching integer in file `one_million_integers.txt`...')
with open('one_million_integers.txt', 'r') as integers:
    start_cpu = psutil.cpu_percent(interval=None)
    start_mem = psutil.virtual_memory().used
    start_time = time.time()

    found, line = search_integer(target=RANDOM_INTEGER, file=integers)

    end_time = time.time()
    end_cpu = psutil.cpu_percent(interval=None)
    end_mem = psutil.virtual_memory().used

if found:
    print(f'Integer FOUND on line {line} !!!')
else:
    print('Integer NOT FOUND !!!')

cpu_usage = end_cpu - start_cpu
mem_usage = (end_mem - start_mem) / (1024 * 1024)  # Convert to MB
execution_time = end_time - start_time

print('-' * 42)

print(f'CPU usage: {cpu_usage}%')
print(f'RAM usage: {mem_usage:.2f} MB')
print(f'Execution time: {execution_time:.2f} seconds')
