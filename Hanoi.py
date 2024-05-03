#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:05:28 2024

@author: finiballester
"""

def hanoi(n,origen,final):
    lista_de_moves = []
    if (n,origen,final)==(1, 1, 3):
        lista = [1, 1, 3]
        lista_de_moves.append(lista)
    else:
        
        lista_anterior = hanoi(n-1, origen, final)
        lista1=[l.copy() for l in lista_anterior]
        lista2=[l.copy() for l in lista_anterior]
        for e in range(0,len(lista1)):
            if lista1[e][-1]==2:
                lista1[e][-1] = lista1[e][-1] + 1
            elif lista1[e][-1]==3:
                lista1[e][-1] = lista1[e][-1] - 1
            elif lista1[e][-2]==2:
                lista1[e][-2] = lista1[e][-2] + 1
            elif lista1[e][-2]==3:
                lista1[e][-2] = lista1[e][-2] - 1
            if lista2[e][-1]==2:
                lista2[e][-1]= lista2[e][-1] + 1
            elif lista2[e][-2]==1:
                lista2[e][-2] = lista2[e][-2] +1
            elif lista2[e][-2]==2:
                lista2[e][-2] = lista2[e][-2] -1 
                
        lista_de_moves=lista1 + [[n, origen, final]]+lista2
            
   
            
   
    return lista_de_moves
        
hanoi(3,1,3)            
print(hanoi(3,1,3))           
            
            
            
