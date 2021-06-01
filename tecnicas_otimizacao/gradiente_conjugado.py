"""

@author: Livio Lopes
"""
import numpy as np
import matplotlib.pyplot as plt


# Função objetivo minF(x1,x2)=(x1-2)⁴+(x1-2*x2)²
def func(a,b):
	return ((a-2)**4 + (a-2*b)**2)


# Plotando grafico em 3D de uma função com duas variaveis
def plotting_function(a,b,function):
    a,b = np.meshgrid(a,b)
    c = function(a, b)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(a,b,c)
    fig.savefig("plotting_function.png")
    plt.show()
    
    
"""
A procura irá identificar o intervalor onde está
o minimo local, e ponto minimo local
""" 
def dichotomous_search(function,variable ='',ak=-1.0,bk=1.0,E= 1.0,l =2.0):
    loop = True
    while loop:
        # Verifica se o limiar foi alcançado
        if (bk-ak)< l:
            loop = False
            return (ak,bk), (ak+bk)/2
        #Calcula ponto médio e o desloca para a esquerda
        y = (ak+bk)/2 - E
        #Calula ponto médio e o desloca para a direita
        u = (ak+bk)/2 + E
        # Se estivermos avaliando uma função do tipo x, f(x)
        if variable == '':
            fy = function(y)
            fu = function(u)
            #print(fy,fu)
        # Se estivermos avaliando uma função do tipo x1,x2,f(x1,x2)   
        if variable == 'x1':
            fy = function(y,0)
            fu = function(u,0)
            #print(fy,fu)                        
        if variable == 'x2':
            fy = function(0,y)
            fu = function(0,u)  
            #print(fy,fu)
        # Se o ponto de mínimo não está entre [ak,y], então ak = y
        if fy>fu:
            ak = y
        # Se o ponto de mínimo não está entre [u,bk], então bk = u
        if fy<fu:
            bk = u

# Inicio da sequencia
start = -100.0
# Fim da sequencia
end = 100.0
# Quantidade de amostras da sequência
variation = 1
# Criando vetor x1
x1 = np.arange(start,end,variation)
# Criando vetor x2
x2 = np.arange(start,end,variation)
z = func(x1,x2)

plotting_function(x1, x2, func)

#Encontrando o intervalo e o ponto em relação ao variavel em questão
interspace_x1, point_x1 = dichotomous_search(func,variable='x1',ak=-50.0,bk=60.0,E=0.25,l=1.0)
interspace_x2, point_x2 = dichotomous_search(func,variable='x2',ak=-50.0,bk=60.0,E=0.25,l=1.0)

print(point_x1,point_x2,func(point_x1, point_x2))



