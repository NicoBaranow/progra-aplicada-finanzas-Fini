# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:17:39 2024

@author: gbasa
"""

def ordenar(lista):
    if len(lista) == 2:
        if lista[0]<lista[1]:
            salida = lista
        else:
            salida =[lista[1],lista[0]]
    else:
       l0 = lista[0]
       aux = ordenar(lista[1:len(lista)])
       
       if l0 <= aux[0]:
           salida = [l0]+aux
       elif l0>= aux[len(aux)-1]:
           salida  = aux + [l0]
       else:
           salida = [aux[0]]+ordenar([lista[0]]+aux[1:len(aux)])
       print(salida)
    return salida


lista = [(0,1),(1,2),(0,2),(0,3),(1,1),(1,0),(1,1)]

salida = ordenar(lista)