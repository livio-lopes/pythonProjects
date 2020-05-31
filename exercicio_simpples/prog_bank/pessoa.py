"""
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Só será possível sacar se passar na autenticação do banco
"""


from abc import ABC, abstractmethod

class Pessoa:
	#Construtor, variaveis de instância
	def __init__(self, nome, idade):
		# Usando o escopo protected ._
		self._nome = nome
		self._idade = idade
		
	#Getter de Nome
	@property
	def nome(self):
		return self._nome

	#Getter de Idade
	@property
	def idade(self):
		return self._idade
	
class Cliente(Pessoa):
	def __init__(self, nome, idade):
		super().__init__(nome,idade)
		self._tipo_conta = None

	def inserir_conta (self,conta):
		print('conta pessoa')
		self._tipo_conta = conta