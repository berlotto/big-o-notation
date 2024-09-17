
import time
import random
from metodo import busca_binaria

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    busca_binaria(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [10, 5000, 100000]:
    entrada = list(range(n))
    duracao = medir_tempo(arr=entrada, valor=random.randint(1, n))
    print(f'Tempo para n={n}: {duracao:.8f} segundos')
