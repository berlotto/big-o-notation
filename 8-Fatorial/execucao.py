
import time

from metodo import permutacoes

# Função para medir o tempo de execução
def medir_tempo(n):
    inicio = time.time()
    permutacoes(n)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [5, 8, 10]:
    entrada = list(range(n))
    duracao = medir_tempo(n=entrada)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
