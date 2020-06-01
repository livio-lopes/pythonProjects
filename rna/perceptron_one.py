#Perceptron de uma camada

entradas = [1,7,5]
pesos = [0.8, 0.1,0] #sinapses

#Função Soma
def somatorio(e,p):
	soma = 0
	for i in range(3):
		soma += e[i]*p[i]
	return soma

# Função ativação, degrau unitário
def stepFunction(somatorio):
	if somatorio >= 1: return 1
	return 0

soma = somatorio(entradas, pesos)
result = stepFunction(soma)
print(result)