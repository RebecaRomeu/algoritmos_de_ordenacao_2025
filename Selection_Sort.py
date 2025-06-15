def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


print("Lista desordenada: [15, 25, 22, 10, 9]")
print(f"Lista ordenada: {selection_sort([15, 25, 22, 10, 9])}")




# Vantagens: 
# A sua simplicidade de implementação o torna uma boa opção para situações em que a simplicidade é mais importante do que o desempenho. 
# Requer menos trocas do que outros algoritmos de ordenação, como o Bubble Sort por exemplo. 

# Desvantagens: 
# Não é eficiente para lidar com grandes conjuntos de dados pois seu tempo de execução aumenta muito conforme o aumento do tamanho da lista. 
# Não preserva a ordem relativa de elementos iguais, dessa forma se houverem dois elementos com o mesmo valor eles podem ser trocados de posição durante o processo de ordenação. 
