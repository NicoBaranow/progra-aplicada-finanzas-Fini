#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:34:45 2024

@author: finiballester
"""

# M = 1000
# D = 500
# C = 100
# L = 50
# X = 10
# V = 5
# I = 1

# Se escriben de mayor a menor
# El valor del numero es la suma de los valores de todos sus numerales
# Si un valor menor precede a un valor mayor, el valor menor se resta del valor mayor al que precede inmediatamente, y esa diferencia se suma al valor del n ̇mero.
#Cree una funcion r2i que convierta de manera recursiva un numero romano entre 1 y 3999 en un numero entero



romano_a_numero = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}

def r2i (romano):            # "XXI"
    ROMANO = list(romano)    #["X", "X", "I"]
    numero = 0
    for posicion in range (0, len(ROMANO)-1):
        if romano_a_numero[ROMANO[posicion]] >= romano_a_numero[ROMANO[posicion+1]]:
            numero = numero + romano_a_numero[ROMANO[posicion]]
        else:
            numero = numero - romano_a_numero[ROMANO[posicion]]
    numero = numero + romano_a_numero[ROMANO[-1]]
    return numero

r2i("XXI") 
print (r2i("XXI"))

r2i("XIX") 
print (r2i("XIX"))

r2i("MDCLXVI") 
print (r2i("MDCLXVI"))

r2i("MMMXXIX") 
print (r2i("MMMXXIX"))