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

idade = input('Eu nascia a 2000 mil anos atrás, qual a sua idade?')

altura = input("Vamos calcular seu IMC, qual sua altura em métros? ")

massa = input("Qual o seu peso em Quilogramas?")

imc = float(massa)/(float(altura)**2)

ano_nasci = atual.year - int(idade)

if (imc < 18.5):
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está ABAIXO DO PESO")
elif (imc > 18.5 and imc < 24.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está com PESO NORMAL")
elif (imc > 25 and imc < 29.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está com SOBREPESO")
elif (imc > 30 and imc < 34.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está com OBESIDADE GRA 1")
elif (imc > 35 and imc < 39.9):
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está com OBESIDADE GRA 2")
else: 
	print(f"{nome} você nasceu em {ano_nasci}, correto? Seu indice é {imc:.2f} e você está com OBESIDADE GRA 3")