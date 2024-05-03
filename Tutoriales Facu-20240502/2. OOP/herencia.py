# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:40:02 2024

@author: gbasa
"""
#%% Delegating to superclass methods

class Base1:
    def amethod(self): print("Base1")

class Base2(Base1): 
    def amethod(self): print("Base2")
    
class Base3(Base1):
    def amethod(self): print("Base3")

class Derived(Base2, Base3): 
    def amethod(self):
        super(Derived,self).amethod()
        
aninstance = Derived( )
aninstance.amethod( )        #barre las clases de izquierda a derecha y dps sube

#%% Llama multiples veces a met de clase A
class A(object):
    def met(self):
        print('A.met')

class B(A):
    def met(self):
        print('B.met')
        A.met(self)

class C(A):
    def met(self):
        print('C.met')
        A.met(self)

class D(B,C):
    def met(self):
        print('D.met')
        B.met(self)
        C.met(self)
        
        
a = D()        
a.met()
#%% Cooperative superclass method calling

"""The solution is to use built-in type super. super(aclass, obj), which
returns a special superobject of object obj. 
When we look up an attribute (e.g., a method) in this superobject, the lookup 
begins after class aclass in obj’s MRO (method resolution order).
El superobject resuelve las posibles redundancias que puedan existir arriba en 
la jerarquia"""

class A(object):
    def met(self):
        print( 'A.met')
        
class B(A):
    def met(self):
        print('B.met')
        super(B,self).met( )
        
class C(A):
    def met(self):
        print('C.met')
        super(C,self).met( )

class D(B,C):
    def met(self):
        print('D.met')
        super(D,self).met( )
        
a = D()
a.met()


#%%

class A(object):
    def met(self):
        print( 'A.met')
        #super(A, self).met()
        
class B(A):
    def met(self):
        print('B.met')
        super(B,self).met( )
        
class C(A):
    def met(self):
        print('C.met')
        super(C,self).met( )

class E():
    def met(self):
        print('E.met')
        
class D(B,C,E):
    def met(self):
        print('D.met')
        super(D,self).met( )
        
a = D()
a.met()




