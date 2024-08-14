import psutil
import time


start_cpu = psutil.cpu_percent(interval=None)
start_mem = psutil.virtual_memory().used

start_time = time.time()

print('Loading `one_billion.txt` into memory...')
memory = []
with open('one_billion.txt', 'r') as numbers:
    for number in numbers:
        memory.append(number.strip())

end_time = time.time()

end_cpu = psutil.cpu_percent(interval=None)
end_mem = psutil.virtual_memory().used

cpu_usage = end_cpu - start_cpu
mem_usage = (end_mem - start_mem) / (1024 * 1024)  # Convert to MB
execution_time = end_time - start_time

print(f'CPU usage: {cpu_usage}%')
print(f'RAM usage: {mem_usage:.2f} MB')
print(f'Execution time: {execution_time:.2f} seconds')
