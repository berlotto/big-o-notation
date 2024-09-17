import math
import decimal

def calculate_pi_gauss_legendre(iterations):
    decimal.getcontext().prec = 100  # Ajustar a precisão conforme necessário
    a = decimal.Decimal(1)
    b = decimal.Decimal(1/math.sqrt(2))
    t = decimal.Decimal(1/4)
    p = decimal.Decimal(1)

    for _ in range(iterations):
        a_next = (a + b) / 2
        b_next = decimal.Decimal(a * b).sqrt()
        t_next = t - p * (a - a_next)**2
        p = 2 * p
        a = a_next
        b = b_next
        t = t_next

    pi = (a + b)**2 / (4 * t)
    return pi

# Exemplo de uso:
n = 1000000
pi_approx = calculate_pi_gauss_legendre(n)
print("Aproximação de Pi:", pi_approx)