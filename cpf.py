# Programa para validar cpf e gerar
# Feito por Lívio Lopes 

# O CPF pode entrar de duas formas: 
# 54646584115 
# 546.465.841-15

# Importando Bibliotecas
from random import randint
# Instanciando Variaveis Globais
lista_digito = []
loop = True
# Salva string de entrada em uma lista, pode virar uma função
def string_intList(string):
	for digito in string:
		try:
			lista_digito.append(int(digito))
		except:
			print('\nVocê digitou algo errado no CPF')

def verifica_cpf(string ):	
# Identifica qual seria o décimo digito do CPF, pode virar uma função
	acumulador = 0
	for index in range(9):
		acumulador += lista_digito[index]*(10-index)
	ten_dgt = 11 - (acumulador % 11)
	if ten_dgt > 9:
		ten_dgt = 0
# Identifica qual seria o décimo primeiro digito do CPF, pode virar uma função
	acumulador = 0
	for index in range(10):
		acumulador += lista_digito[index]*(11-index)
	elv_dgt = 11 - (acumulador % 11)
# Valida final CPF 
	if ten_dgt == lista_digito[9] and elv_dgt == lista_digito[10]:
		return True
	else:
		return False

def trata_string(string):
	lista_digito = string.split('-')
	lista_digito = lista_digito[0].split('.')
	temp =''
	for index in range(3):
		temp += lista_digito[index]
	temp+=string[-2] + string[-1]
	lista_digito.clear()
	return temp


def valida_cpf(string ):
	if len(string) == 11:
# 1 Tenta converter a string em um alista de inteiros
		string_intList(string)
# 2 Verifica CPF
		valido = verifica_cpf(string)
		if valido == True:
			print(f'O CPF {string} é VÁLIDO\n')
		else:
			print(f'O CPF {string} é INVÁLIDO\n')

	elif len(string) == 14:
# 1 Verificar caracteres especiais nas posições 3,7 e 11 da string
		if string[3] == '.' and string[7] == '.'and string[11] == '-':
# 2 Faz tratamento da String
			temp2 = trata_string(string)
# 3 Tenta converter a string em uma lista de inteiros
			string_intList(temp2)
# 4 Verifica o CPF
			valido = verifica_cpf(temp2)
			if valido == True:
				print(f'O CPF {string} é VÁLIDO\n')
			else:
				print(f'O CPF {string} é INVÁLIDO\n')	
		else:
			print('\nVocê digitou algo errado no CPF, tente novamente.')
	else:
		print('\nVocê digitou algo errado no CPF, tente novamente.')

def gera_cpf():
	loop = True
	while loop:
		lista_digito.clear()
		for index in range(0,11):
			lista_digito.append(randint(0,9))
		string = ''
		for index in range(0,11):
			string += str(lista_digito[index])
		valido = verifica_cpf(string)
		if valido == True:
			loop = False
	return string

# PRINCIPAL
while loop:
	escolhe=input('Olá, Bem-Vindo ao famegerado ValiGeraCPF!\nDigite 1 - Gerar CPF VÁLIDO\n Digite 2 - Validar UM CPF\n Para sair digite Fechar\n')
	if escolhe == '1':
		cpf = gera_cpf()
		print(f'{cpf} é um CPF VÁLIDO\n')
	elif escolhe == '2':
		cpf = input('Qual o CPF que você deseja validar? ')
		valida_cpf(cpf)
	elif escolhe == 'Fechar':
		loop = False
