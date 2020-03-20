# Programa para validar cpf e gerar
# Feito por Lívio Lopes 

# O CPF pode entrar de duas formas, 
# apenas numeros com tamanho 11, 
# ou numero, pontos e traços tamanho 14
entrada = '16899535009'
lista_digito = []
acumulador = 0
# Salva string de entrada em uma lista
for digito in entrada:
	try:
		lista_digito.append(int(digito))
	except:
		print('\nVocê digitou algo errado no CPF')
for index in range(9):
	acumulador += lista_digito[index]*(10-index)
ten_dgt = 11 - (acumulador % 11)
acumulador = 0
if ten_dgt > 9:
	ten_dgt = 0
for index in range(10):
	acumulador += lista_digito[index]*(11-index)
elv_dgt = 11 - (acumulador % 11)

if ten_dgt == lista_digito[9] and elv_dgt == lista_digito[10]:
	print(f'\nO CPF {entrada} é válido!')
