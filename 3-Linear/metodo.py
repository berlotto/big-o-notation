def encontrar_elemento(arr, valor):
    for i in range(len(arr)):
        if arr[i] == valor:
            return i
    return -1