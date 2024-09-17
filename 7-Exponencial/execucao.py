
import time

from metodo import fibonacci

# Função para medir o tempo de execução
def medir_tempo(**kwargs):
    inicio = time.time()
    fibonacci(**kwargs)
    fim = time.time()
    return fim - inicio

# Teste para tamanhos diferentes de entradas
for n in [10, 30, 50]:
    duracao = medir_tempo(n=n)
    print(f'Tempo para n={n}: {duracao:.6f} segundos')
