#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:29:16 2021

@author: marunga
"""

import numpy as np

#Função de Ativação
def sigmoid(valor):
    return 1/(1+ np.exp(-valor))

# Entradas para o operador lógico XOR
x = np.array([[0,0],
             [0,1],
             [1,0],
             [1,1]])
# Saidas para o operador lógico XOR
y = np.array([[0],[1],[1],[0]])
# Pesos da camada de entrada
w1 = np.array([[-0.424,-0.740,-0.961],
               [0.358, -0.577, -0.469]])
# Pesos da camada intermediária
w2 = np.array([[-0.017],[-0.893],[0.148]])
# Épocas/ Quantidade de treinos
time_training = 100

for i in range(time_training):
    input_layer = x
    # Produto escalar entre camada entrada e os seus respectivos pesos
    input_synapse = np.dot(input_layer, w1)
    hiden_layer = sigmoid(input_synapse)
    # Produto escalar entre camada intermediaria e os seus respectivos pesos
    hiden_synapse = np.dot(hiden_layer,w2)
    output_layer = sigmoid(hiden_synapse)
    # Calculando erros da camada de saída
    erro_output_layer = y - output_layer
    # Se usa np.abs() para obter o módulo dos erros da camada de saída
    erro_mean = np.mean(np.abs(erro_output_layer))
