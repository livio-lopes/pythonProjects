"""
QuantumBogoSort a quantum sorting algorithm which can sort any list in O(1), 
using the "many worlds" interpretation of quantum mechanics.
It works as follows:
1. Quantumly randomise the list, such that there is no way of knowing
 what order the list is in until it is observed. 
This will divide the universe into O(n!) universes; 
however, the division has no cost, as it happens cosntantly anyway.
2. If the list is not sorted, destroy the universe. (
This operation is left as an exercise to the reader.)
3. All remaining universes contain lists which are sorted.
"""






import random 

# Define numero elementos da lista

n = 20

# Cria uma lista de N elementos

lista = list(range(n))

# Embaralha a lista

random.shuffle(lista)

lista_universal = []
print(lista)
for i in range(len(lista)):
	random.shuffle(lista)
	lista_universal.append(lista)
	print(lista_universal[i])


print(lista_universal)

