def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return array

print("Lista desordenada: [1, 36, 12, 14, 59, 2]")
print(f"Lista ordenada: {merge_sort([1, 36, 12, 14, 59, 2])}")

# Vantagens: 
# É eficiente para organizar listas com grande volume de dados. 
# É um algoritmo estável que preserva a ordem relativa de elementos iguais. 
# Indicado para aplicações que possuem restrições de tempo. 

# Desvantagens: 
# Utiliza memória auxiliar pois durante o processo de merge o Merge Sort cria listas auxiliares para armazenar as sublistas ordenadas, isso pode consumir uma quantidade significativa de memória auxiliar.
