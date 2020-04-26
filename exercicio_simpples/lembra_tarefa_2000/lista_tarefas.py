"""
Programinha para criar uma lista de tarefas contendo no minimo 4 operações
add - adicionar tarefa
listar - listar tarefa
desf - desfazer a última tarefa
ref - refazer a última tarefa

Feito por Lívio Lopes
"""

import os
import functions

try:
	os.mkdir('guarda_tarefas')
except:
	pass # O diretório já existe

while True:
	print(
		'\nEsse é o Lembra Tarefa 2000\n'
		'Para adicionar uma tarefa, digite add\n'
		'Para listar as tarefas, digite listar\n'
		'Para desfazer a ultima alteração, digite desf\n'
		'Para refazer a última alteração, digite ref\n'
		'Para fechar o programa, digite sair\n'
		)
	entrada = input()
	if entrada == 'sair':
		break
	elif entrada == 'add':
		nova_tarefa = input('Insira a nova tarefa: ')
		functions.add(nova_tarefa)
	elif entrada == 'listar':
		functions.listar()
	elif entrada == 'desf':
		functions.desf()
	elif entrada == 'ref':
		functions.ref()
	else:
		print('Você digitou o comando errado, tente novamente')