def busca_binaria(arr, valor):
    inicio, fim = 0, len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == valor:
            return meio
        elif arr[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1