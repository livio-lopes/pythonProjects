"""
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

class Banco:
	def __init__(self):

		self._agencias = ['1111','2222','3333']
		self._clientes = []
		self._contas = []

	def inserir_client(self, cliente):
		self._clientes.append(cliente)

	def inserir_conta(self,conta):
		self._contas.append(conta)

	def autenticar(self, cliente):
		if cliente not in self._clientes: return False
		if cliente.conta not in self._contas: return False
		if cliente.conta.agencia not in self._agencias: return False
		return True
