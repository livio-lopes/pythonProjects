# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

entradas = [7,2,-1]
pesos = [0.5,0.35,-0.25]


#Função Soma
def summation(e, p):
    for i in range (len(entradas)):
        s= e[i]*p[i]
    return s

#Função de Ativação: Degrau unitário
def functionActivation(soma):
    if soma >=0:
        return 1
    return 0
        
s = soma(entradas, pesos)
f = functionActivation(s)