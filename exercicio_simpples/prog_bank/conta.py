"""
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
 """


from abc import ABC, abstractmethod
#Conta é uma classe abstrata
class Conta(ABC):
	#Construtor
	def __init__(self, agencia,num,saldo = 0):
		self._agencia =agencia
		self._num = num
		self._saldo = saldo
	#Getters e Setters
	@property
	def agencia(self):
		return self._agencia
	@property
	def num(self):
		return self._num
	@property
	def saldo(self):
		return self._saldo
	@saldo.setter
	def  saldo(self, valor):
		self._saldo = valor
	#Métodos da Classe
	def depositar(self, valor):
		self._saldo += valor

	@abstractmethod
	def sacar(self, valor):
		pass

class ContaPoupanca(Conta):
	def __init__(self,agencia,num,saldo):
		super().__init__(agencia,num, saldo)
	def sacar(self,valor):
		if valor <= self._saldo:
			self.saldo -= valor
			return
		print('Saldo insuficiente')

class ContaCorrente(Conta):
	def __init__(self,agencia,num,saldo,limite =400):
		super().__init__(agencia,num,saldo)
		self._limite = limite

	@property
	def limite(self):
		return self._limite
	

	def sacar(self, valor):
		if valor <= (self._saldo + self._limite):
			self._saldo -= valor
			if self._saldo <= 0:
				self._limite += self._saldo
			return
		print('Saldo insuficiente')




"""c1 = ContaPoupanca(1111,1234,100)
c1.depositar(100)
print(c1.saldo)
c1.sacar(50)
print(c1.saldo)
c1.sacar(160)

c2 = ContaCorrente(2222,1234,100,100)
print(c2.limite)
c2.depositar(50)
print(c2.saldo)
c2.sacar(140)
print(c2.saldo)
c2.sacar(40)
print(c2.saldo)
c2.sacar(100)	
print(c2.saldo)
"""