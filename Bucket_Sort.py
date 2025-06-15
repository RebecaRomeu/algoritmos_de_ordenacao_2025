def bucket_sort(array):
    if len(array) == 0:
        return array

    min_val = min(array)
    max_val = max(array)
    bucket_range = (max_val - min_val) / len(array)

    buckets = [[] for _ in range(len(array))]

    for num in array:
        index = int((num - min_val) / bucket_range)
        if index == len(array):  # Tratar o caso do valor máximo
            index -= 1
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

print("Lista desordenada: [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]")
print(f"Lista ordenada: {bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434])}")

# Vantagens 
# Muito rápido com dados bem distribuídos. 
# Estável (se o algoritmo usado nos baldes for estável). 
# Pode ser adaptado para trabalhar com números de ponto flutuante. 

# Desvantagens 
# Escolha dos baldes pode ser difícil (número e intervalo ideais). 
# Pode perder eficiência se houver muitos elementos concentrados em poucos baldes. 
# Precisa de memória extra para armazenar os baldes. 
