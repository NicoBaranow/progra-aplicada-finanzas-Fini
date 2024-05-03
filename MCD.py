#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:20:16 2024

@author: finiballester
"""

#%%
#La descomposición en factores primos es el proceso de expresar un número como el producto de números primos. 
# c es el producto de los factores comunes(encontrados) elevados a su menor exponente(el mas chico de los dos).


def buscador_numeros_primos(num):
    divisor = 2
    numeros_primos=[]
    
    while num > 1:
        if num % divisor != 0:
            divisor = divisor + 1
        
        else:
            numeros_primos.append(divisor)
            num = num/divisor
            
    return numeros_primos
    print (numeros_primos)



def mcd1(a,b):
    primos_a = buscador_numeros_primos(a)
    primos_b = buscador_numeros_primos(b)
    factores_comunes = []
    exponentes = {}
    numeros_elevados=[]
    for e in primos_a:
        if e in primos_b:
            factores_comunes.append(e)
    
    for i in factores_comunes:
       contador_a = primos_a.count(i)
       contador_b = primos_b.count(i)
       menor_exponente = min(contador_a, contador_b)
       exponentes[i] = menor_exponente
    
    for n in factores_comunes:
        numero = n ** exponentes[n]
        numeros_elevados.append(numero)
        
    producto = 1 
    for n in numeros_elevados:
        producto *= n
        
        return producto
        
#mcd1(96,8)
#print (mcd1(96,8))
#%%

def mcd2(a,b):
    if a == 0:
        mcd = b
    elif b == 0:
        mcd = a
    elif a == b:
        mcd = a
        
    elif a > b:
        c = a%b
        if c == int:
            mcd = c
        else:
            
            mcd = mcd2(b,c)
    else: 
        c = b%a
        if c== int:
            mcd = c
        else:
            mcd = mcd2(a,c)
            
    return mcd
    
#mcd2(24,18)
#print(mcd2(24,18))


#%%
import time
start=time.perf_counter_ns()
print(mcd1(148832,448))
end=time.perf_counter_ns()
print("tardo" ,end - start,"ns en calcularlo con la funcion mcd1.")

st=time.perf_counter_ns()
print (mcd2(148832,448))
fin=time.perf_counter_ns()
print("tardo" ,fin - st,"ns en calcularlo con la funcion de Euclides.")




#%%
def mcd2(a,b):
    if b == 0:
        mcd = a
    elif a == 0:
        mcd = b
    elif a == b:
        mcd = a
    
    elif a > b:
        c = a % b
        if c == int:
            mcd = c
                
        else:
            mcd2= b%c
            mcd = mcd2
        
    else:
        c = b % a
        if c == int:
            mcd = c
                    
        else:
            mcd3 = a%c
            mcd = mcd3
    
    return mcd
            


mcd2(96,42)




    
        












