
import time

from metodo import bubble_sort

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    bubble_sort(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [10, 1000, 10000]:
    entrada = list(range(n))
    duracao = medir_tempo(arr=entrada)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
