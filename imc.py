# Programinha para calcular IMC e ver resultado
# Feito por Lívio Lopes


altura = input("Vamos calcular seu IMC, qual sua altura em métros? ")

massa = input("Qual o seu peso em Quilogramas?")

imc = float(altura)/float(massa)**2

if (imc < 18,5)
	print("Seu indice é ", imc," e você está ABAIXO DO PESO")
elif (imc > 18,5 && imc < 24,9)
	print("Seu indice é ", imc," e você está com PESO NORMAL")
elif (imc > 25 && imc < 29,9)
	print("Seu indice é ", imc," e você está com SOBREPESO")
elif (imc > 30 && imc < 34,9)
	print("Seu indice é ", imc," e você está com OBESIDADE GRA 1")
elif (imc > 35 && imc < 39,9)
	print("Seu indice é ", imc," e você está com OBESIDADE GRA 2")
elif (imc < 40 )
	print("Seu indice é ", imc," e você está com OBESIDADE GRA 3")