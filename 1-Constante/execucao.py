
import time

from metodo import acessar_elemento

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    acessar_elemento(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [10, 100, 1000]:
    entrada = list(range(n))
    duracao = medir_tempo(arr=entrada, index=3)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
