def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print("Lista desordenada: [5, 4, 8, 1, 6]")
print(f"Lista ordenada: {bubble_sort([5, 4, 8, 1, 6])}")



# Vantagens: 
# Algoritmo é simples de ser implementado, possui apenas uma tarefa a ser executada, que é a comparação entre dois valores e a troca se houver necessidade. 
# É um algoritmo de classificação estável que mantém a ordem relativa dos elementos de valores iguais, assim se dois elementos tiverem o mesmo valor, sua ordem mantida mesmo após a classificação. 
# Não requer memória adicional para executar a operação de classificação. Ele ordena os elementos dentro da própria matriz fornecida, tornando-a eficiente em termos de memória.  

# Desvantagens: 
# O algoritmo é ineficiente para grandes conjuntos de dados. À medida que o número de elementos aumenta, o número de comparações e trocas cresce exponencialmente, levando a tempos de execução cada vez mais longos. 
