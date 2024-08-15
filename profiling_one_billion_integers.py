import time
from random import randint

import psutil


start_cpu = psutil.cpu_percent(interval=None)
start_mem = psutil.virtual_memory().used

search = int(input('Para iniciarmos a busca, informe um número inteiro entre 1 e 1000000000 (um bilhão): '))

start_time = time.time()

total_of_files = 4
memory = []  # Inicializa memória
found = False
for i in range(1, total_of_files + 1):
    print(f'Gerando arquivo {i} de {total_of_files} com números inteiros aleatórios...')
    # Gerando arquivo de 250 milhões de linhas, um pouco mais de
    # 2.6 GB de tamanho em disco (cabe na RAM com certo conforto)
    with open('250_millions_of_random_integers.txt', 'w') as integers:
        for j in range(1, 250_000_000 + 1):
            integers.write(f'{randint(1, 1_000_000_000)}\n')

    print(f'Carregando arquivo {i} de {total_of_files} na memória...')
    with open('250_millions_of_random_integers.txt', 'r') as integers:
        for integer in integers:
            memory.append(int(integer.strip()))

    print('Buscando número inteiro na memória...')
    for integer in memory:
        if search == integer:
            print(f'>>> Número {i} encontrado! <<<')
            found = True
            break

    if found:
        memory = []  # Libera memória utilizada
        break

    memory = []  # Libera memória utilizada

end_time = time.time()

end_cpu = psutil.cpu_percent(interval=None)
end_mem = psutil.virtual_memory().used

cpu_usage = end_cpu - start_cpu
mem_usage = (end_mem - start_mem) / (1024 * 1024)  # Convert to MB
execution_time = end_time - start_time

print(f'CPU: {cpu_usage}%')
print(f'RAM: {mem_usage:.2f} MB')
print(f'Tempo de execução: {execution_time:.2f} segundos')





# 1_000_000 ocupa 8 MB em disco
        
