"""
Instruções:

Conforme combinamos, seguem as instruções do Trabalho.

1. Podem fazer em dupla ou individual.

2. Desta forma, esta dupla já deve ser montada (preferencialmente) para desenvolvimento das atividades da disciplina até o final do curso. Mas não e mandatório, podem trocar se for preciso.

3. Lembrem-se que irão apresentar no próximo encontro. Se for em dupla, ambos falam.

4. Ao enviar o trabalho, em arquivo compactado, é obrigatório que coloquem os códigos comentados. Coloquem os autores no código e no nome do arquivo.



Trabalho



1. A dupla deve implementar um programa computacional, em linguagem de programação a sua escolha, que trabalhe os seguintes itens ao receber um grafo como entrada.



a. Verificar a existência de uma determinada aresta. 

b. Informar o grau de um dado vértice.

c. Informar a lista de adjacência de um dado vértice.

d. Verificar se o grafo é cíclico.

e. Verificar se o grafo é conexo.

f. Informar quantos e quais são os componentes fortemente conexos do grafo.

g. Verificar se o grafo é Euleriano.

h. Plotar o (s) Grafo (s) gerado (s).

i. O algoritmo deve admitir grafo orientado e nao-orientado.


Bom trabalho!"""

#AUTOR: ANTONIO LÍVIO B. LOPES - 201506840013

from function_grafo import *

grafo= { "A" : ["B"],
          "B" : ["C", "D"],
          "C" : ["B", "E"],
          "D" : ["A"],
          "E" : ["B"]        }
loop = True

while loop:
	print('ESCOLHA UMA DAS OPÇÕES ABAIXO')
	print('\na. Verificar a existência de uma determinada aresta. ',
		'\nb. Informar o grau de um dado vértice e sua lista de adjacência',
		'\nc. Informar quantos e quais são os componentes fortemente conexos do grafo.',
		'\nd. Verificar se o grafo é conexo.',
		'\nFechar'
		)
	option = input()

	if option == 'a':
		aresta = input("Qual a aresta você deseja Verificar? ")
		existeAresta(aresta,grafo)
	if option == 'b':
		vertice = input("De qual vertice você deseja as informações? ")
		infoVertice(vertice,grafo)
	if option == 'c':
		print("\nOs vertices que estão fortemente conexos são das seguintes aresta: ")
		fortementeConexo()
	if option == 'd':
		grafoCONEXO(grafo)
	if option == 'Fechar':
		loop = False