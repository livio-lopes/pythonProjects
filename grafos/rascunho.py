lista_aresta = dictTOLIST(grafo)
tamanho = len(lista_aresta)
ciclo = []

for x in range(tamanho):
	vertice_2 = lista_aresta[x]
	vertice_2 = vertice_2[1]

	for y in range(tamanho):
		vertice_1 = lista_aresta[y]
		vertice_1 = vertice_1[0]

		if vertice_2 == vertice_1:
			ciclo.append(lista_aresta[x]+lista_aresta[y])
			

tamanho = len(ciclo)
ciclo_2 =[]
for x in range(tamanho):
	print(ciclo[x])
	aresta_1 = ciclo[x]
	for y in range(tamanho):
		aresta_2 = ciclo[y]
		if aresta_1[-1] == aresta_2[0]:
			ciclo_2.append(aresta_1+aresta_2)

print(ciclo_2)

for caminho in ciclo_2:
	if caminho[-2]==caminho[0] and caminho[-1]==caminho[1]:
		print(caminho)
	else:
		print("Não é ciclico")