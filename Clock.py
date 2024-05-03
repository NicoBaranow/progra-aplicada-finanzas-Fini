#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:06:29 2024

@author: finiballester
"""
import datetime
import time

class clock (object):
    
    def __init__(self, hora = 00, minuto = 00, segundo = 00):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        
    def onesec (self):
        contador = 0
        for e in range (75489258):
            contador += 1      
    
    def update (self):
        self.onesec()
        self.segundo += 1
            
        if self.segundo == 60:
            self.minuto += 1
                
            if self.minuto == 60:
                self.hora +=1
                    
                if self.hora ==24:
                        self.hora = 0
        
    def PrintCurrentTime(self):
        print ("The current time is ", self.hora, ":", self.minuto, ":", self.segundo)
        
    
    def SetClock (self, tupla = None):
        if tupla == None:
            self.hora = datetime.datetime.now().hour
            self.minuto = datetime.datetime.now().minute
            self.segundo = datetime.datetime.now().second
        
        else:
            self.hora = tupla[0]
            self.minuto = tupla[1]
            self.segundo = tupla [2]
            
            
    def work(self, tupla = None):
        self.SetClock()
        
        while True:
            self.onesec()
            self.update()
            tecla = input("Ingrese la letra p si quiere saber el horario y que  el reloj siga funcionando. De lo contrario ingrese q.  ")
            if tecla == "p":
                self.PrintCurrentTime()
                print (datetime.datetime.now().time())
            elif tecla == "q":
                self.PrintCurrentTime()
                print (datetime.datetime.now().time())
                print ("Stopping clock.")
                break
        
        
a = clock()    
a.onesec()  
a.update()
a.SetClock()
a.PrintCurrentTime()
a.work()
        
        
        
        
        
        
        
        
#%% ONE SEC

# Necesito 1,000,000,000 nano segundos para tener un segundo. 

# import time
# def onesec ():
#     contador = 0
#     start = time.perf_counter_ns()
#     for e in range (75489258):
#         contador += 1      
#     end = time.perf_counter_ns()
#     tiempo = end - start
#     print (tiempo)
#     return None

onesec()
#%%
 # if keyboard.is_pressed("p"):
 #     self.PrintCurrentTime()
 #     print (datetime.datetime.now(time()))
 # elif keyboard.is_pressed("q"):
 #     self.PrintCurrentTime()
 #     print (datetime.datetime.now(time()))
 #     print ("Stopping clock.")
 #     break