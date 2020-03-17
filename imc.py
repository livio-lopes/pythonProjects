# Programinha para calcular IMC e ver resultado
# Feito por Lívio Lopes

"""
from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

"""

from datetime import datetime
atual = datetime.now() #Objeto que captura data e hora do computador
erro_entrada = False #Variavel para controle de tipos de dados

nome = input('Olá, sou a IMC 2000, a super calculadora de IMC, quem é você?')
#Entrada que pode gerar erro insignificante
idade = input('\nEu nascia a 2000 mil anos atrás, qual a sua idade?')
#Entradas que podem gerar erros significativos
altura = input("\nVamos calcular seu IMC, qual sua altura em métros? ")
massa = input("\nQual o seu peso em Quilogramas?")
#Tenta converter a entrada idade em int
try: 
	idade = int(idade)
	ano_nasci = atual.year - idade
except:
	ano_nasci = 'um lugar secreto'
#Tenta converter a entrada altura e massa em float
try:
	altura = float(altura)
	massa = float(massa)
	imc = massa/altura**2
except:
	erro_entrada = True
#Se houver erro nas entradas altura e massa
#o programa é interrompido, caso contrario continua
if erro_entrada == True:
	print('Erro na entrada, tente novamente!')
else:
	if (imc < 18.5):
		print(f"{nome} você nasceu em {ano_nasci}, correto?")
		if '20' in str(ano_nasci):
			print(' Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com ABAIXO DO PESO')
	elif (imc > 18.5 and imc < 24.9):
		print(f"{nome} você nasceu em {ano_nasci}, correto?")
		if '20' in str(ano_nasci):
			print(' Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com PESO NORMAL')
	elif (imc > 25 and imc < 29.9):
		print(f"{nome} você nasceu em {ano_nasci}, correto?")
		if '20' in str(ano_nasci):
			print(' Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com SOBREPESO')
	elif (imc > 30 and imc < 34.9):
		print(f"{nome} você nasceu em {ano_nasci}, correto?")
		if '20' in str(ano_nasci):
			print(' Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 2')
	elif (imc > 35 and imc < 39.9):
		print(f"{nome} você nasceu em {ano_nasci}, correto? ")
		if '20' in str(ano_nasci):
			print(' Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 2')
	else: 
		print(f"{nome} você nasceu em {ano_nasci}, correto? ")
		if '20' in str(ano_nasci):
			print('Você é tão antigo quanto eu!')
		print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 3')