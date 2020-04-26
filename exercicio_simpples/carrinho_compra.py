# Programinhas para somar produtos de um carrinho
# Feito por Lívio Lopes

carrinho= [
	('Chilano Branco', 10),
	('Chilano Tinto', 20),
	('Chilano Rosé', 30),
	('Condado Real Tempranillo', 40),
	('Calvet Pinot Noir', 60),
	('Calvet Prestiged Bordeaux', 70),
	('Lambrusco Tinto', 80),
	('Lambrusco Branco', 90)	
]
#Posição na tupla
produto = 0
valor = 1 
# O total será uma lista com os preços dos produtos
total = sum([item[valor] for item in carrinho])

print(f'O valor total dessa compra é {total} R$')