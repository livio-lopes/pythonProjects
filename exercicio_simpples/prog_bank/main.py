"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from pessoa import Cliente
from conta import CC, CP
from bank import Banco

banco = Banco() 

clt1 = Cliente(nome = 'Daniela', idade = 28)
clt2 = Cliente(nome = 'Ane Carolinda', idade = 24)
clt3 = Cliente(nome = 'Kalyne', idade = 22)

cont1 = CC(agencia = '1111', num_conta = '22345-3', saldo=535.2)
cont2 = CP(agencia = '2222', num_conta = '2256345-3', saldo=1200)
cont3 = CC(agencia = '3124', num_conta = '2256345-3', saldo=0)

clt1.inserir_conta(cont1)
clt2.inserir_conta(cont2)
clt3.inserir_conta(cont3)

