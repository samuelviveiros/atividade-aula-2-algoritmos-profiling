# Atividade - Aula 2 - Profilling - Estruturas e Complexidade de Algoritmos

Configurando o ambiente:

```bash
C:\>python -m venv env-3.11
C:\>env-3.11\Scripts\activate
(env-3.11) C:\>python -m pip install --upgrade pip
(env-3.11) C:\>pip install -r requirements.txt
```

Gerando os arquivos:

```bash
(env-3.11) C:\>python generate_files.py
Generating `one_million.txt`...
Generating `one_billion.txt`...
```

Carregando 1 milhão de números inteiros na memória:

```bash
(env-3.11) C:\>python profilling_one_million_numbers.py
Loading `one_million.txt` into memory...
CPU usage: 9.0%
RAM usage: 56.39 MB
Execution time: 0.14 seconds
```

Carregando 1 bilhão de números inteiros na memória:

```bash
(env-3.11) C:\>python profilling_one_billion_numbers.py
Loading `one_billion.txt` into memory...
CPU usage: 17.2%
RAM usage: 17612.58 MB        
Execution time: 163.47 seconds
```
