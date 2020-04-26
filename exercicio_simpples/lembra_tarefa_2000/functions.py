"""
add - adicionar tarefa
listar - listar tarefa
desf - desfazer a última tarefa
ref - refazer a última tarefa

Feito por Lívio Lopes

"""


#lista_de_entradas = []

backup = ''

local_arquivo = "guarda_tarefas/lista_de_tarefas.txt"

# Adiciona uma tarefa por linha em lista_de_tarefas.txt
def add(string):
	with open(local_arquivo, 'a+') as file:
		file.write(f'\n{string}')
# Lista as tarefas contidas em lista_de_tarefas.txt
def listar():
	with open(local_arquivo, 'r') as file:
		print(f'\n{file.read()}')
def ref():
	# Acessar backup e escreve-lo no arquivo
	add(backup)
def desf():
	global backup
	# Abre o arquivo para leitura
	with open(local_arquivo, 'r+') as file:
		# Seta o curso no inicio do arquivo
		file.seek(0)
		# Transforma em lista todas as linhas do arquivo
		lista_de_entradas = file.readlines()
	backup = lista_de_entradas[-1]
	lista_de_entradas.pop()
	with open(local_arquivo, 'w+') as file:
			for tarefa in lista_de_entradas:
				file.write(f'{tarefa}')
