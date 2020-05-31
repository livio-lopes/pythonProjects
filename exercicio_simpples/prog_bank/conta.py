"""
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
 """


from abc import ABC, abstractmethod


class Conta(ABC):

	#Construtor, variaveis de instância
	def __init__(self,agencia,num_conta,saldo = 0.0):
		self._agencia = agencia
		self._num_conta = num_conta
		self._saldo = saldo

	# Getters
	@property
	def agencia(self):
		return self._agencia
	@property
	def num_conta(self):
		return self._num_conta
	@property
	def saldo(self):
		return self._saldo
	
	# Setter
	@saldo.setter
	def saldo(self, valor):
		# Faz um breve tratamento da entrada
		if not isinstance(valor, (int, float)):
			print("Você não digitou um valor válido")
		else:
			self._saldo = valor

	def deposito(self, valor):
		self._saldo += valorPessoa
		self.exibir()

	def exibir(self):
		print(f'Agencia: {self._agencia}'
			f'Conta: {self._num_conta}'
			f'Saldo: {self._saldo}')

	# Cada conta terá o seu método para saque
	@abstractmethod
	def saque(self, valor):	pass

# Conta Corrente
class CC(Conta):
	
	def __init__(self,agencia,num_conta,saldo = 0, cheque_especial=400.0):
		super().__init__(agencia, num_conta, saldo)
		self._cheque_especial = cheque_especial

	def saque(self, valor):
		if valor <= self._saldo:
			self._saldo -= valor
		elif valor <= (self._saldo + self._cheque_especial):
			aux = self._saldo - valor
			self._cheque_especial += aux
			self._saldo -= valor
		else:
			print(f'Seu saldo de {self._saldo} + {self._cheque_especial} o saldo de seu Cheque Especial são inferiores ao valor de {valor} desejado para saque')

# Conta Poupança
class CP(Conta):
	
	def saque(self, valor):
		if valor <= self._saldo:
			self._saldo -= valor
			self.exibir()
		else:
			print('Vocẽ não possui saldo na conta para efetuar esse saque')