"""
Programinha para validar e gerar CNPJ válido

Feito por Lívio Lopes
"""

import gera, valida

while True:
	entrada = input('Digite 1 para Validar CNPJ \n'
					'Digite 2 para Gerar CNPJ\n'
					'Digite 3 para Sair\n')
	# Validando CNPJ
	if entrada == '1':
		cnpj = input('Digite o CNPJ que deseja validar: ')
		#cnpj = valida.teste
		valido = valida.process_cnpj(cnpj)
		print(f'O CNPJ {cnpj} é Valido'
		if valido else f'O CNPJ {cnpj} é Inválido')
	# Gerando CNPJ Válido
	elif entrada == '2':
		pass
	# Saindo do programa
	elif entrada == '3':
		break
	else:
		print('Você digitou algo errado, tente novamente')