
import time
import random
from metodo import knapsack

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    knapsack(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [5, 100, 150]:
    valores = list(range(n))
    pesos = [random.randint(0,n) for x in range(n)]
    capacidade = random.randint(0,n)

    duracao = medir_tempo(capacidade=capacidade, pesos=pesos, valores=valores, n=n)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
