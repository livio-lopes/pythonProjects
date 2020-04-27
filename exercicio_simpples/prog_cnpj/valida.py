"""
Funções para Validação de CNPJ

Feito por Lívio Lopes
"""

lista_digitos = []
new_string = ''

# Processa o CNPJ da entrada
def process_cnpj(string):
	formatacao = formato(string)
	if formatacao:
		valido = verifica_digito(string)
		return True if valido else False
	else:
		return False


# Formatos de entrada do CNPJ 33.608.075/0001-09 ou 33608075000109
def formato(string):
	tamanho = len(string)
	if tamanho == 14:
		tamanho_correto = tamanho_14(string)
		return True if tamanho_correto else False
	elif tamanho == 18:
		#Fazer tratamento da string, 'converter' em tamanho 14
		new_string = trata_string(string)
		tamanho_correto = tamanho_14(new_string)
		return True if tamanho_correto else False	
	else:
		return False

# Verifica se há erro de digitação
def tamanho_14(string):
	try:
		lista_digitos = [int(index) for index in string]
		return True
	except ErroDigito:
		print('Houve um erro de digitação\n')
		return False

# Retorna uma string correta com tamanho 14 ou 'erro'
def trata_string(string):
	for index in string:
		try:
			if isinstance(int(index),int):
		  		new_string += index
		except:
			#Não faz nada
			pass

	return new_string if len(new_string) == 14 else 'erro'

# Deve receber uma string com tamanho 14 para verificação
def verifica_digito(string):
	#Toda string que for recebida será tratada para tamanho 14
	new_string = trata_string(string)
	acumulador = 0
	try:
		for num in range(-3,-15,-1):
			aux = -num-1
			if aux >9:
				aux -=8
			print(new_string[num], aux)
			acumulador += (int(new_string[num])*aux)
	except:
		#Não faz nada
		pass
	resultado = 11 - (acumulador%11)
	digito_1 = 0 if resultado >9 else resultado

	if digito_1 == int(new_string[-2]):
		digito_1 = True
		print(digito_1)
	else:
		digito_1 = False
		print(digito_1)

	acumulador = 0
	try:
		for num in range(-2,-15,-1):
			aux = -num
			if aux >9:
				aux -=8
			print(new_string[num], aux)
			acumulador += (int(new_string[num])*aux)
	except:
		#Não faz nada
		pass
		
	resultado = 11 - (acumulador%11)
	digito_2 = 0 if resultado >9 else resultado

	if digito_2 == int(new_string[-1]):
		digito_2 = True
		print(digito_2)
	else:
		digito_2 = False
		print(digito_2)
	"""
	Retorna Verdadeiro se o Penultimo digito
	e o Ultimo digito estiverem certoas.
	"""
	return True if digito_1 == digito_2 else False
