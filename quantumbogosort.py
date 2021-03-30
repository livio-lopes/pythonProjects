"""QuantumBogoSort a quantum sorting algorithm which can sort any list in O(1), using the "many worlds" interpretation of quantum mechanics.
It works as follows:
1. Quantumly randomise the list, such that there is no way of knowing what order the list is in until it is observed. This will divide the universe into O(n!) universes; however, the division has no cost, as it happens constantly anyway.
2. If the list is not sorted, destroy the universe. (This operation is left as an exercise to the reader.)
3. All remaining universes contain lists which are sorted."""






import random 


def bogosort(seq):
    while not all(x <= y for x, y in zip(seq, seq[1:])):
        random.shuffle(seq)
    return seq

def factor(n):
  if ( n == 0):
    return None
  elif(n==1):
      return 1
  else:    
      theFactors = []
      for i in range(2,n+1):          
          while n % i == 0:
              n = n/i
              theFactors.append(i)
      return theFactors

def chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]

# Cria uma lista com 20 elementos, de 0 a 19

lista = list(range(20))

random.shuffle(lista)

tamanho = len(lista)

fator_comum=factor(tamanho)

lista = list(chunks(lista,5))


listona = []
for listinha in  lista:
	print(listinha)
	if not all(x <= y for x,y in zip(listinha,listinha[1:])):
		random.shuffle(listinha)
	for item in listinha:
		listona.append(item)	



print(listona)
random.shuffle(listona)
print(listona)