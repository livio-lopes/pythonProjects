#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:31:36 2021

@author: marunga
"""

import numpy as np

#Função Somatóŕio
def summation(entrada, peso):
    #Retorna o produto escalar entre o vetor entrada e peso
    return entrada.dot(peso)

#Função de Ativação: Degrau unitário
def functionActivation(soma):
    if soma >=0:
        return 1
    return 0


#Entrada x
x = np.array([7,2,-1])
#Pesos w
w = np.array([0.5,0.35,-0.25])
     
s = summation(x, w)
f = functionActivation(s)