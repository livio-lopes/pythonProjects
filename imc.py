# Programinha para calcular IMC e ver resultado
# Feito por Lívio Lopes


altura = input("Vamos calcular seu IMC, qual sua altura em métros? ")

massa = input("Qual o seu peso em Quilogramas?")

imc = float(massa)/(float(altura)**2)

if (imc < 18.5):
	print(f"Seu indice é  {imc:.2f} e você está ABAIXO DO PESO")
elif (imc > 18.5 and imc < 24.9):
	print(f"Seu indice é {imc:.2f} e você está com PESO NORMAL")
elif (imc > 25 and imc < 29.9):
	print(f"Seu indice é {imc:.2f} e você está com SOBREPESO")
elif (imc > 30 and imc < 34.9):
	print(f"Seu indice é {imc:.2f} e você está com OBESIDADE GRA 1")
elif (imc > 35 and imc < 39.9):
	print(f"Seu indice é {imc:.2f} e você está com OBESIDADE GRA 2")
else: 
	print(f"Seu indice é {imc:.2f} e você está com OBESIDADE GRA 3")