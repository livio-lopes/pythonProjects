# Programa para validar cpf e gerar
# Feito por Lívio Lopes 

# O CPF pode entrar de duas formas: 
# 54646584115 
# 546.465.841-15
# 


entrada = input('Digite um CPF que deseja validar: ')
lista_digito = []

# Salva string de entrada em uma lista, pode virar uma função
def string_intList(string = entrada):
	for digito in string:
		try:
			lista_digito.append(int(digito))
		except:
			print('\nVocê digitou algo errado no CPF')

def valida_cpf():	
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
		print(f'\nO CPF {entrada} é válido!')

def trata_string():
	lista_digito = entrada.split('-')
	lista_digito = lista_digito[0].split('.')
	temp =''
	for index in range(3):
		temp += lista_digito[index]
	temp+=entrada[-2] + entrada[-1]
	lista_digito.clear()
	return temp


#PRINCIPAL
if len(entrada) == 11:
	# 1 Tenta converter a string em um alista de inteiros
	string_intList()
	# 2 Valida CPF
	valida_cpf()

elif len(entrada) == 14:
	# 1 Verificar se existem 2 pontos e 1 ifen
	# 2 Verificar se eles estão na posição 3, 7 e 11 respectivamente
	if entrada[3] == '.' and entrada[7] == '.'and entrada[11] == '-':
	# 3 Faz tratamento da String
		temp2 = trata_string()
	# 4 Tenta converter a string em uma lista de inteiros
		string_intList(temp2)
	# 5 Valida o CPF
		valida_cpf()
	else:
		print('\nVocê digitou algo errado no CPF, tente novamente.')
else:
	print('\nVocê digitou algo errado no CPF, tente novamente.')

