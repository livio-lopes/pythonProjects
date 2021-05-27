#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:38:31 2021

@author: marunga
"""

import numpy as np

"""
OPERADOR AND
#Entradas
x = np.array([[0,0],[0,1],[1,0],[1,1]])
#Saídas
y = np.array([0,0,0,1])
"""

""" 

OPERADOR OR
#Entradas
x = np.array([[0,0],[0,1],[1,0],[1,1]])
#Saídas
y = np.array([0,1,1,1])

"""
#Pesos
w = np.array([0.0,0.0])
#Taxa de aprendizagem
learning = 0.1

#Função de ativação
def functionActivation (summation):
    if (summation >=1):
        return 1
    return 0

#Função Somatório
def calculateOutput(register):
    #Realiza o produto escalar do par ordedado de entradas com o peso
    result = register.dot(w)
    return functionActivation(result)

#Treinamento, encontra o melhor conjunto de pesos
def training ():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(y)):
            #Calcula a saída 
            calculatedOutput = calculateOutput(np.array(x[i]))
            #Calcula a diferença entre a saida esperada e saida calculada
            erro = abs(y[i]- calculatedOutput)
            erroTotal += erro
            #Atualizando Pesos
            for j in range(len(w)):
                #Proximo peso = Peso atual + Taxa de Aprendizado * Entrada Atual * Erro
                w[j] = w[j]+ (learning*x[i][j]*erro)
                print('Peso atualizado: ' + str(w[j]))
        print('Total de Erros: ' +str(erroTotal))
        
training()
print('Rede Treinada!')
#Com a rede treinada, testa se as respostas sairão sem erros
print(calculateOutput((x[0])))
print(calculateOutput((x[1])))
print(calculateOutput((x[2])))
print(calculateOutput((x[3])))