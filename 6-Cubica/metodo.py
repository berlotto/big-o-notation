def multiplicar_matrizes(A, B):
    # Tamanho das matrizes
    n = len(A)
    # Matriz resultante
    C = [[0 for _ in range(n)] for _ in range(n)]

    # Três laços aninhados - Complexidade cúbica O(n³)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C