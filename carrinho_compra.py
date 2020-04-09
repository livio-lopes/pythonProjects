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
# O total será uma lista com os preços dos produtos
total = [item[1] for item in carrinho]

print(total, type(total),sum(total))