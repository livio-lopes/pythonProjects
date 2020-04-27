"""
Funções para gerar CNPJ

Feito por Lívio lopes
"""

"""
Ao se fazer uma combinação, o cnpj que será validado sempre será
o primeiro que aparecer na lista de combinações
não parece ser a melhor opção

from itertools import combinations_with_replacement
lista = ['0','1','2','3','4','5','6','7','8','9']
comp = combinations_with_replacement(lista,14)
for combina in list(comp):
	string = ''
	for num in combina:
		string +=num
	print(string)

"""


import valida, random


"""
O Sorteio parece ser a melhro solução, só é preciso corrigir
com 0 (zero) a esquerda para formar uma string de tamanho 14

1 - Sortear um número
2 - Transforma em string
	1 - Se for tamanho menor que 14, completar com 0 a esquerda
3 - Validação
"""
def genex(cont = 1):
	
	inicio = 0
	fim =    99999999999999
	valido = False

	while valido == False:
		cnjp = str(random.randint(inicio,fim))

		if len(cnjp) <14:
			# Completar com 0 a esquerda
			pass

		valido = valida.process_cnpj(cnjp)
	return cnjp

def completa_zero():
	pass

def trata_saida():
	pass


