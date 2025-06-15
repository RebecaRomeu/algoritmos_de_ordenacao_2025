def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

print("Lista desordenada: [52, 106, 33, 1, 9, 14, 78]")
print(f"Lista ordenada: {heap_sort([52, 106, 33, 1, 9, 14, 78])}")

# Vantagens 
# Complexidade de tempo estável, tendo um desempenho consistente e não depende da ordem inicial dos elementos. Complexidade de tempo O(n*log(n)), independentemente da distribuição dos dados. 
# Utiliza quantidade constante de memória, sendo mais adequado para ordenar grandes conjuntos de dados, quando a memória disponível é limitada. 

# Desvantagens 
# Não é estável, não mantém a ordem relativa dos elementos iguais. 
# Não é eficiente devido às altas constantes na complexidade de tempo. 
# Sua implementação é mais complexa em comparação a algoritmos mais simples como o Insertion Sort e Selection Sort.
