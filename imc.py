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

atual = datetime.now()

nome = input('Olá, sou a IMC 2000, a super calculadora de IMC, quem é você?')

idade = input('\nEu nascia a 2000 mil anos atrás, qual a sua idade?')

altura = input("\nVamos calcular seu IMC, qual sua altura em métros? ")

massa = input("\nQual o seu peso em Quilogramas?")

imc = float(massa)/(float(altura)**2)

ano_nasci = atual.year - int(idade)

if (imc < 18.5):
	print(f"{nome} você nasceu em {ano_nasci}, correto?")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com ABAIXO DO PESO')
elif (imc > 18.5 and imc < 24.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto?")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com PESO NORMAL')
elif (imc > 25 and imc < 29.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto?")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com SOBREPESO')
elif (imc > 30 and imc < 34.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto?")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 2')
elif (imc > 35 and imc < 39.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto? ")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 2')
else: 
	print(f"{nome} você nasceu em {ano_nasci}, correto? ")
	if '20' in ano_nasci):
		print(' Você é tão antigo quanto eu!')
	print(f'\nSeu indice é {imc:.2f} e você está com OBESIDADE GRA 3')