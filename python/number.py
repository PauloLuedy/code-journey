numeros = [1, 20, 1, 1, 1]

numeros[0] = 99          # muda o valor do índice 0
numeros.append(6)        # adiciona no final
numeros.insert(2, 100)   # insere na posição 2
numeros.remove(20)        # remove o valor 4
del numeros[0]  
print(numeros)

print(len(numeros))   # tamanho da lista
print(sum(numeros))   # soma dos valores
print(max(numeros))   # maior valor
print(min(numeros))   # menor valor