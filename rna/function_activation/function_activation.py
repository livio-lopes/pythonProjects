#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 01:51:04 2021

@author: marunga
"""
import numpy as np

# Função degrau unitário
def stepFunction(valor):
    if valor >=1:
        return 1
    return 0

# Função Sigmoid
def sigmoid(valor):
    return 1/(1+ np.exp(-valor))

# Função Hiperbólica
def tanh(valor):
    return (np.exp(valor)-np.exp(-valor))/(np.exp(valor)+np.exp(-valor))



print(sigmoid(0))
print(tanh(0))