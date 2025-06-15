def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array

# Exemplo de uso
lista_desordenada = [10, 7, 8, 9, 1, 5]
n = len(lista_desordenada)
print("Lista desordenada: ",  lista_desordenada)
print("Lista ordenada: ", quick_sort(lista_desordenada, 0, n - 1))

# Vantagens: 
# Melhor opção para usar com grande volume de dados. 
# Maior rapidez devido a simplicidade do seu laço interno. 
# Memória auxiliar usada para recursão é pequena. 

# Desvantagens: 
# Não é estável. 
# No seu pior caso possui o mesmo desempenho que o Bubble Sort por exemplo. 
