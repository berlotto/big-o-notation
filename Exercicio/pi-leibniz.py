import math

def calculate_pi_leibniz(n):
  """Calcula uma aproximação de Pi utilizando a série de Leibniz.

  Args:
    n: Número de termos da série.

  Returns:
    Uma aproximação de Pi.
  """

  pi = 0
  for i in range(n):
    pi += (-1)**i / (2*i + 1)
  return 4 * pi

# Exemplo de uso:
n = 1000000
pi_approx = calculate_pi_leibniz(n)
print("Aproximação de Pi:", pi_approx)