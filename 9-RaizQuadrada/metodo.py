import math

def jump_search(arr, valor):
    n = len(arr)
    passo = int(math.sqrt(n))
    prev = 0

    while arr[min(passo, n)-1] < valor:
        prev = passo
        passo += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(passo, n)):
        if arr[i] == valor:
            return i
    return -1