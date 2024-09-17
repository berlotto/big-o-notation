
import time

import random 
from metodo import multiplicar_matrizes

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    multiplicar_matrizes(**kwargs)
    fim = time.time()
    return fim - inicio

def gerar_matriz_aleatoria(tamanho):
  """Gera uma matriz quadrada aleatória com o tamanho especificado."""
  return [[random.randint(1, 100) for _ in range(tamanho)] for _ in range(tamanho)]

# Teste para tamanhos diferentes de entradas
for n in [10, 50, 90]:
    A = gerar_matriz_aleatoria(n)
    B = gerar_matriz_aleatoria(n)
    duracao = medir_tempo(A=A, B=B)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
