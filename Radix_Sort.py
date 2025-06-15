def counting_sort_for_radix(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = array[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]

def radix_sort(array):
    max_val = max(array)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(array, exp)
        exp *= 10

    return array

print("Lista desordenada: [2, 54, 89, 32, 64, 159, 99, 2, 89]")
print(f"Lista ordenada: {radix_sort([2, 54, 89, 32, 64, 159, 99, 2, 89])}")

# Vantagens: 
# Muito rápido para números inteiros de tamanho fixo. 
# É um algoritmo de classificação estável. 
# Eficiente para grandes conjuntos de dados com valores dentro de um intervalo razoável. 

# Desvantagens: 
# Requer sub-rotina de ordenação estável (ex.: Counting Sort). 
# Não serve bem para números com casas decimais ou negativos sem adaptações. 
# Pode requerer memória adicional dependendo da implementação
