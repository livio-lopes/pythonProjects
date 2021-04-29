"""
FONTES:
https://pt.wikipedia.org/wiki/Bogosort

AUTOR:
ANTONIO LIVIO BARBOSA LOPES - 201506840013
"""

import random, time
 
# Enquanto não for x<=y em toda a sequencia, embaralha
def bogosort(seq, contador = 0):
    while not all(x <= y for x, y in zip(seq, seq[1:])):
        random.shuffle(seq)
        contador +=1
    return seq, contador


def busca_linear(lista, elemento,contador=0):
	for i in range(len(lista)):
		contador+=1
		if elemento == lista[i]:
			return elemento, contador
		

#define quantidade de elementos da lista
n = 10
#cria uma lista com n elementos, de 0 a n-1
lista = list(range(n))
#lista = [1,1,13,5,2,5,66,2,5]
#lista = [-1,0.2, 33,3213]
lista = lista
print(f' A lista gerada {lista}')
#embaralha a lista
random.shuffle(lista)
print(f'A lista embaralha {lista}')
# Retorna o tempo antes de executar a função
inicio = time.time()
# ordenação com o bogo sorte 
lista,contador= bogosort(lista)
# Retorna o tempo depois da execução
fim = time.time()

execucao = fim - inicio
print(f'A lista ordenada {lista}',
		 f'\niterações realizadas: {contador}',
		 f'\ntempo de execução: {execucao} em seg')



# Sorteia uma elento de 0 a 2xtamanho da lista
# para ter 50% de chance sortear um elemento não listado
elemento = random.randint(0, 2*len(lista))
# tenta fazer achar o elemento
try:
	# Retorna o tempo antes de executar a função
	inicio = time.time()
	acha_ai, contador = busca_linear(lista,elemento)
	# Retorna o tempo depois da execução
	fim = time.time()
	execucao = fim - inicio
	print(f'O elemento sorteado foi {elemento}',
			f'\n E {acha_ai} existe na lista {lista}',
			f'\n Tempo de execução: {execucao} em seg',
			f'\n Interações realizadas: {contador}')
except:
	print(f'O elemento {elemento} não existe na lista {lista}')


