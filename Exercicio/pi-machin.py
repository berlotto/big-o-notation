import math

def calculate_pi_machin(n):
  """Calcula uma aproximação de Pi utilizando a fórmula de Machin.

  Args:
    n: Número de termos da série usada para calcular o arcotangente.

  Returns:
    Uma aproximação de Pi.
  """

  def arctan(x, n):
    """Calcula o arcotangente de x usando uma série de Taylor truncada em n termos."""
    t = 0
    for i in range(n):
      t += (-1)**i * x**(2*i+1) / (2*i+1)
    return t

  return 16*arctan(1/5, n) - 4*arctan(1/239, n)

# Exemplo de uso:
n = 1000
pi_approx = calculate_pi_machin(n)
print("Aproximação de Pi:", pi_approx)