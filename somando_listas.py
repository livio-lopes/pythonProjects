# Programinha para somar duas Listas
# Feito por Lívio Lopes


lista_1 = [1,2,3,4,5,6,7]
lista_2 = [1,2,3,4]

#Solução em Python
#Combinando as listas
soma = zip(lista_1,lista_2)
#Formando lista de somas dos valores desempacotados
total = [x + y for x,y in soma]
print(total)

#Solução genérica

lista_soma = []
if len(lista_1) >= len(lista_2):
	for index in range(len(lista_2)):
		lista_soma.append(lista_1[index] + lista_2[index])
	print(lista_soma)
else:
	pass