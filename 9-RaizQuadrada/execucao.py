
import time

from metodo import jump_search

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    jump_search(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [5, 1000, 10000]:
    entrada = list(range(n))
    duracao = medir_tempo(arr=entrada, valor=abs(n/2)+abs(n/4))
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
