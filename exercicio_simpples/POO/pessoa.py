"""
Uma  pessoa tem nome e idade.

Enquanto uma pessao fala, ela não come. Vice versa.

Se está realizando uma ação, tem que de interromper 
a ação corrente para executar outra.
"""



class Pessoa:

	def __init__(self, nome, idade, comendo=False, falando=False):
		self.nome = nome
		self.idade = idade
		self.comendo = comendo
		self.falando = falando

	def comer(self, alimento):

		if self.comendo:
			print(f"{self.nome} já está comendo")
			return

		if self.falando:
			print(f'{self.nome} está falando, não pode comer')
			return

		print(f"{self.nome} está comendo {alimento}")
		self.comendo = True

	def parar_de_comer(self):
		if not self.comendo:
			print(f"{self.nome} não está comendo")
			return

		print(f"{self.nome} parou de comer")
		self.comendo = False

	def falar(self,assunto):
		
		if self.falando:
			print(f'{self.nome} já está falando')
			return

		if self.comendo:
			print(f'{self.nome} está comendo, não pode falar')
			return

		print(f'{self.nome} está falando sobre {assunto}')
		self.falando = True

	def parar_de_falar(self):
		if not self.falando:
			print(f'{self.nome} não está falando')
			return

		print(f'{self.nome} parou de falar')
		self.falando = False
