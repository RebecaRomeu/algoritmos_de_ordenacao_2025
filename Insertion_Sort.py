def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print("Lista desordenada: [102, 59, 33, 1, 70, 8]")
print(f"Lista ordenada: {insertion_sort([102, 59, 33, 1, 70, 8])}")

# Vantagens: 
# O algoritmo é estável, preservando a ordem de elementos com valores iguais. 
# Ele não utiliza memória auxiliar. 
# Mesmo ainda realizando muitas trocas ele se mostra mais eficiente que o Selection Sort e o Bubble Sort. 

# Desvantagens: 
# É um algoritmo com baixa performance para grande quantidade de itens a serem ordenados. 
