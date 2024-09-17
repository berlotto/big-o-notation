
import time

from metodo import encontrar_elemento

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    encontrar_elemento(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [10, 1000, 100000]:
    entrada = list(range(n))
    duracao = medir_tempo(arr=entrada, valor=n-1)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
