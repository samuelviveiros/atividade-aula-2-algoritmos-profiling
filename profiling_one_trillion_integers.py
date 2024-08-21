import time
from random import randint

import psutil 


RANDOM_INTEGER = randint(1, 1_000_000_000_000)
print(f'Random integer generated: {RANDOM_INTEGER:,}'.replace(',', '.'))

start_cpu = psutil.cpu_percent(interval=None)
start_mem = psutil.virtual_memory().used
start_time = time.time()

# 
# Uma lista contendo 100 milhões de números consumirá cerca de 5.3 GB de RAM.
# Dependendo da quantidade de memória disponível no seu sistema, aumente ou
# diminua este número conforme necessário.
#
# Observe que o produto de factor_1 por factor_2 deverá ser sempre igual a 1 trilhão.
#
factor_1 = 10_000
factor_2 = 100_000_000  # 5.3 GB de RAM
#factor_1 = 20_000
#factor_2 = 50_000_000  # 2.7 GB de RAM

def search_integer(target: int):
    # Simula busca em arquivo de texto com 1 trilhão de linhas
    for count in range(1, factor_1 + 1):

        # Preenche a memória com inteiros
        memory = []
        for k in range(1, factor_2 + 1):
            memory.append(randint(1, 1_000_000_000_000))

        # Procura o inteiro na memória
        for integer in memory:
            if target == integer:
                return True

        print(f'Searched {(count * factor_2):,} lines of 1.000.000.000.000'.replace(',', '.'))

    return False  # Inteiro não encontrado

if search_integer(target=RANDOM_INTEGER):
    print(f'Integer FOUND !!!')
else:
    print('Integer NOT FOUND !!!')

end_time = time.time()
end_cpu = psutil.cpu_percent(interval=None)
end_mem = psutil.virtual_memory().used

cpu_usage = end_cpu - start_cpu
mem_usage = (end_mem - start_mem) / (1024 * 1024)  # Convert to MB
execution_time = end_time - start_time

print('-' * 42)

print(f'CPU usage: {cpu_usage}%')
print(f'RAM usage: {mem_usage:.2f} MB')
print(f'Execution time: {execution_time:.2f} seconds')
