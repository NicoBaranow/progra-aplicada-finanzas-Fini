# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
#a
def fib1(n):
    if n<=0:
        return 0
    elif n==1:
        return 1 
    else:
        return fib1(n-1)+fib1(n-2)

fib1(10)
#%%
#b
lista=[]
def fib2(n):
    for e in range(n):
        a=fib1(e)
        lista.append(a)
        print(lista)
    

#Primer paso: Probar/validar para un cierto n0 inicial que f(n0)=g(n0)

import sympy as sp
import math
n=sp.symbols("n")
s=math.sqrt(5)
equation= (1/s)*((((1+s)/2)**n)-(((1-s)/2)**n))
resultado=equation.subs(n,20)
print(resultado)

#Cumple, da lo mismo que usando fib1 y fib2. 
#esta parte ni idea como hacer con el n+1
#%%

#c
import time
start=time.perf_counter_ns()
print(fib2(40))
end=time.perf_counter_ns()
print("tardo" ,end - start,"ns en calcularlo con la funcion.")

st=time.perf_counter_ns()
for e in range(40):
    eq= (1/s)*((((1+s)/2)**n)-(((1-s)/2)**n))
    res=eq.subs(n,e)
    print(res)
fin=time.perf_counter_ns()
print("tardo" ,fin - st,"ns en calcularlo con la ecuacion.")
#%%

#d1
#Usando un loop hacia adelante, que para calcular F (n) inicializa dos 
#valores F (n- 1) = F (n- 2) = 1 y que se va calculando de manera iterativa haciendo 
#F (n) = F (n- 1) + F (n- 2), y con cada valor de F (n) nuevo calculado se van 
#sustituyendo los dos valores previos F (n -1) = F (n) y F (n -2) = F (n-1) 
#para calcular al siguiente F (n). Llame a esta funcion Fib3(n). 

def fib3(n):
    l=[0,1,1]
    if n<=0:
        f = 0
    elif n==1:
        f=1
    else:
        for e in range(n):
            f=l[-1]+l[-2]
            l[-2]=l[-1]
            l[-1]=f
            print(f)
        return f 
        
fib3(10)
            
 #%%   
 #d2
       
    





































def fib4(n):
    lista=[]
    if n <= len(lista):
        valor = lista[n]
    else:
        valor= fib1(n)
        lista.append(valor)
        print (valor)
        return valor

fib4(10)

#%%
#e
start1=time.perf_counter_ns()
print(fib1(40))
end1=time.perf_counter_ns()

start2=time.perf_counter_ns()
print(fib2(40))
end2=time.perf_counter_ns()

start3=time.perf_counter_ns()
print(fib3(40))
end3=time.perf_counter_ns()

start4=time.perf_counter_ns()
print(fib4(40))
end4=time.perf_counter_ns()

print("Tardo" ,end1 - start1,"ns en calcularlo con la funcion Fibonacci 1.")
print("Tardo" ,end2 - start2,"ns en calcularlo con la funcion Fibonacci 2.")
print("Tardo" ,end3 - start3,"ns en calcularlo con la funcion Fibonacci 3.")
print("Tardo" ,end4 - start4,"ns en calcularlo con la funcion Fibonacci 4.")

#%%















