def counting_sort(array):
    max_val = max(array)
    m = max_val + 1
    count = [0] * m

    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

print("Lista desordenada: [2, 9, 11, 5, 3, 19]")
print(f"Lista ordenada: {counting_sort([2, 9, 11, 5, 3, 19])}")


# Vantagens: 
# Muito eficiente quando o intervalo de números é pequeno. 
# Não usa comparações. 

# Desvantagens: 
# Não funciona bem com intervalos muito grandes. 
# Só funciona com inteiros. 
