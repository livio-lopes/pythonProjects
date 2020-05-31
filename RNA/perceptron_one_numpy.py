#Perceptron de uma camada, com otimização de código

import numpy
#np.array() usando a definição da bib numpy
entradas = np.array([1,7,5])
pesos =np.array([0.8, 0.1,0]) #sinapses

#Função Soma
def somatorio(e,p):
	#Produto escalar
	return e.dot(p)

# Função ativação, degrau unitário
def stepFunction(somatorio):
	if somatorio >= 1: return 1
	return 0

soma = somatorio(entradas, pesos)
result = stepFunction(soma)
print(result)