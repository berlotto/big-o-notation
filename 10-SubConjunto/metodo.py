def knapsack(capacidade, pesos, valores, n):
    if n == 0 or capacidade == 0:
        return 0
    if pesos[n-1] > capacidade:
        return knapsack(capacidade, pesos, valores, n-1)
    else:
        return max(valores[n-1] + knapsack(capacidade-pesos[n-1], pesos, valores, n-1),
                   knapsack(capacidade, pesos, valores, n-1))