#AUTOR: ANTONIO LÍVIO B. LOPES - 201506840013

grafo= { "A" : ["B"],
          "B" : ["C", "D"],
          "C" : ["B", "E"],
          "D" : ["A"],
          "E" : ["B"],
        }

# Verifica se existe aresta
def existeAresta(aresta, grafo):

	aresta = list(aresta)
	vertice_A = aresta[0]
	vertice_B = aresta[1]

	# Verifica se o vertice_A é válido
	if vertice_A in grafo:
		# Verifica se o svertice_B é válido
		if vertice_B in grafo:
			#Verifica se o vertice_A conecta com vertice_B
			if vertice_B in grafo[vertice_A]:
				print("Exite",aresta)
			else:
				print(f'\n{vertice_A} e {vertice_B} são vertices validos porém não formam aresta')
	else:
		print("\nnão exite")

# Informa lista de adjacência e grau do vertice
def infoVertice(vertice, grafo):
	# Verificar vertice é válido
	if vertice in grafo:
		print(f'\nA sua lista de conexões do vertice {vertice} é {grafo[vertice]}, o seu grau é {len(grafo[vertice])}')
	else:
		print("\nEsse vertice não é válido")
 

# Cria uma lista com as arestas do grafo
def dictTOLIST(grafo):
	lista_aresta = []

	for chave in grafo:
		for lista in grafo[chave]:
			# Tenta contatenar strings
			try:
				text = chave+lista
			except:
				text = chave
			lista_aresta.append(text)
	
	return lista_aresta

# Inverte o par ordenado da lista
def inverte(aresta):
	l = list(aresta)
	l.reverse()
	return ''.join(l)

# Verifica qual par ordenado "possui o seu invertido"
def fortementeCONEXO():

	lista_aresta = dictTOLIST(grafo)

	for x in range(len(lista_aresta)):

		if inverte(lista_aresta[x]) in lista_aresta:

			print(lista_aresta[x])

# Verifica na lista de arestas quem não possui par ordenado
def grafoCONEXO(grafo):

	lista_aresta = dictTOLIST(grafo)

	for par in lista_aresta:
		grau = len(par)
	if len(par) == 1:
		print("\ngrafo é DESCONEXO")
	else:
		print("\ngrafo é CONEXO")	



def grafoCICLICO(grafo):

	lista_aresta = dictTOLIST(grafo)
	lista_caminho = []
	for aresta in lista_aresta:
		vertice_2 = aresta[-1]
		for x in range(len(lista_aresta)):
			#print(aresta, lista_aresta[x])
			vertice_1 = lista_aresta[x]
			vertice_1 = vertice_1[0]
			if vertice_2 == vertice_1:
				lista_caminho.append(aresta+lista_aresta[x])
	#print(lista_caminho)
	for caminho in lista_caminho:
		#print(caminho)
		#primeiro vertice do caminho
		p_vertice = caminho[0]
		if  p_vertice in caminho:
			print(p_vertice,caminho)

grafoCICLICO(grafo)

