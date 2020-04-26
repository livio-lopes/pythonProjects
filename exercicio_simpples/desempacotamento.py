#Programinha para extrair Olá
#Feito e Comentado por Lívio Lopes

"""
Talvez essa solução não seja a mais bonita
mas, se você entender está ótimo pra mim
"""

dicionario_1 = {'k1':[1,2,3,{'café':['banana','mulher', 'colher',{'alvo':[1,2,3,'olá']}]}]}
"""
Primeiro, analizando as camadas de fora pra dentro:

dicionario_1{lista_1[dicionario_2{lista_2[dicionario_3{lista_3[]}]}]}

Dentro da terceira lista, que está contida no ultimo dicionário,
está contida a string Olá a qual queremos extrair
"""

# Criamos uma variavel do tipo dicionário para iterar nos valores de dict
tipo_dicionario = dict()
# Variavel Global vazia para extrair a string Olá
extrai = ''
# Salvamos uma 'lista' de valores do dicionario 1
valores_dicionario_1 = dicionario_1.values()
"""
Se você tirar a # no print vai poder observar
que é uma variavel do tipo dict_values, logo 
NÃO É UMA LISTA AINDA.
"""
#print(type(valores_dicionario_1))
# Vamos verifica todos os valores contidos na 'lista 1' de valores
for lista_1 in valores_dicionario_1:
	"""
	Se você tirar a # no print vai perceber que saída é todo
	o valor da chave k1 do primeiro dicionario, e agora sim,
	É UMA LISTA.
	"""
	#print(lista_1, type(lista_1))

	#Verificando indice a indice da lista 1
	for index in lista_1:
		#Se o indice conter um dicionário, salvar os valores do mesmo
		if type(tipo_dicionario) == type(index):
			valores_dicionario_2 = index.values()
			# Verificando todos o valores do dicionario 2
			for lista_2 in valores_dicionario_2:
				#print(lista_2)
				# Novamente, verifica cada indice da lista 2
				for index in lista_2:
					#print(index)
					# Novamente, identifica se o indice da lista contem um dicionario
					if type(tipo_dicionario) == type(index):
						valores_dicionario_3 = index.values()
						#Mais uma vez, verifica todos os valores do dicionario 3
						for lista_3 in valores_dicionario_3:
							#Mais uma vez, verifica indice a indice da lista 3
							for index in lista_3:
								#print(index)
								# Se o indice conter Olá, salva na varia global
								if index == 'olá':
									extrai = index
# Extração feita com sucesso, eu acho
print(extrai)
