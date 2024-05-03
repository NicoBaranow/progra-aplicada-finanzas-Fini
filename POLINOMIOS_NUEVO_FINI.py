#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:34:53 2024

@author: finiballester
"""
#%% Super Class Polinomios

import matplotlib.pyplot as plt
class polinomios (object):
    
    def __init__ (self, grado=0, coef=[0]):
        self.grado = grado 
        self.coef = coef
        if grado < len(coef)-1:
            raise ValueError ("No puede ingresar un grado inferior a la cantidad de coeficientes.")
            
    def get_expression(self):
        funcion = ["P(X)="]
        for exp, c in enumerate(self.coef):
            if c > 0 :
                expresion = "+"+str(c)+"X^"+str(exp)
            elif c > 0 and exp ==0:
                expresion = str(c)+"X^"+str(exp)
            elif c < 0:
                expresion = str(c)+"X^"+str(exp)
            else:
                continue
            funcion.append(expresion)
        final_expression = "".join(funcion)
        return final_expression
    
    
    def __str__(self):
        return self.get_expression()
    
    
    def __call__(self,x):
        y_value = 0
        for exp, c in enumerate(self.coef):
            y_value += (x**exp)*c
        return y_value
    
    
    def poly_plt(self,a,b,**kwargs):
        x_values = [n for n in range(a,b+1)]
        y_values = [self.__call__(x) for x in x_values]
        plt.plot(x_values, y_values,**kwargs)
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.axhline(0,color = 'black', linewidth = 0.5)
        plt.axvline(0,color = 'black', linewidth = 0.5)
        plt.title(f"{self.get_expression()}")
        plt.grid(True)
        plt.show()
    
    def __add__(self, other):
        nuevos_coeficientes = []
        if isinstance (other, (int,float)):
            mayor_grado = self.grado
            nuevos_coeficientes = self.coef
            nuevos_coeficientes[0]+=other
        elif isinstance (other, polinomios):
            mayor_grado = max(self.grado, other.grado)
            if self.grado == mayor_grado:
                other_coeficientes = other.coef +[0]*(len(self.coef)-len(other.coef))
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(self.coef[i]+other_coeficientes[i])
            else:
                self_coeficientes = self.coef +[0]*(len(other.coef)-len(self.coef))
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(self_coeficientes[i]+other.coef[i])
        else:
            raise ValueError ("No sumamos cosas raras")
        return polinomios(mayor_grado, nuevos_coeficientes)
                
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        nuevos_coeficientes = []
        if isinstance (other, (int,float)):
            mayor_grado = self.grado
            nuevos_coeficientes = self.coef
            nuevos_coeficientes[0]-=other
        elif isinstance (other, polinomios):
            mayor_grado = max(self.grado, other.grado)
            if self.grado == mayor_grado:
                other_coeficientes = other.coef +[0]*(len(self.coef)-len(other.coef))
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(self.coef[i]-other_coeficientes[i])
            else:
                self_coeficientes = self.coef +[0]*(len(other.coef)-len(self.coef))
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(self_coeficientes[i]-other.coef[i])       
        else:
            raise ValueError ("No sumamos cosas raras")
        return polinomios(mayor_grado, nuevos_coeficientes)
    
    def __rsub__(self, other):
        if isinstance(other, (int,float)):
            otherPoly = polinomios(0, [other])
            return otherPoly - self
        elif isinstance (other, polinomios):
            nuevos_coeficientes = []
            mayor_grado = max(self.grado, other.grado)
            if self.grado == mayor_grado:
                other_coeficientes = other.coef +[0]*(len(self.coef)-len(other.coef))
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(other_coeficientes[i]-self.coef[i])
            else:
                self_coeficientes = self.coef +[0]*(len(other.coef)-len(self.coef))
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(other.coef[i]-self_coeficientes[i])  
                
                return polinomios(mayor_grado, nuevos_coeficientes)
        else:
            raise ValueError ("No restamos cosas raras")
            
    def __mul__(self,other):
        if isinstance (other, (int,float)):
            nuevos_coeficientes = []
            nuevo_grado= self.grado
            for c in self.coef:
                nuevos_coeficientes.append(c*other)
        
        elif isinstance (other, polinomios):
            nuevo_grado = self.grado + other.grado
            mayor_grado = max(self.grado, other.grado)
            nuevos_coeficientes = [0]*(nuevo_grado+1)
            if mayor_grado == self.grado:
                for exp, c in enumerate(self.coef):
                    for expo, o in enumerate(other.coef):
                        nuevo_coeficiente = c*o
                        nuevo_exponente = exp + expo
                        nuevos_coeficientes[nuevo_exponente]+=nuevo_coeficiente
        
            else:
                for exp, c in enumerate(other.coef):
                    for expo, o in enumerate(self.coef):
                        nuevo_coeficiente = c*o
                        nuevo_exponente = exp + expo
                        nuevos_coeficientes[nuevo_exponente]+=nuevo_coeficiente
            
        else:
            raise ValueError ("No multiplicamos cosas raras")
        
        return polinomios(nuevo_grado, nuevos_coeficientes)
            
    def __rmul__(self,other):
        return self.__mul__(other)
    
    
    def __floordiv__(self, other):
        if isinstance (other, (int,float)):
            nuevos_coeficientes=[]
            nuevo_grado = self.grado
            for c in self.coef:
                nuevos_coeficientes.append(c/other)
        elif isinstance(other, polinomios) and other.grado<=self.grado:
            nuevo_grado = self.grado - other.grado
            resto = self
            nuevos_coeficientes = [0]*(nuevo_grado+1)
            while len(resto.coef)>=len(other.coef):
                cociente = resto.coef[-1]/other.coef[-1]
                grado_de_cociente = len(resto.coef)-len(other.coef)
                cociente_coef = [0]*(grado_de_cociente)
                cociente_coef.append(cociente)
                poli_de_cociente = polinomios(grado_de_cociente,cociente_coef)
                nuevos_coeficientes[grado_de_cociente]=cociente
                poli_que_resto = poli_de_cociente.__mul__(other)
                resto-= poli_que_resto
                while resto.coef[-1]==0:
                    resto.coef.pop(-1)
                    resto.grado -=1
                self.resto = resto
        else:
            raise ValueError("No dividimos cosas raras.")
        # print(nuevos_coeficientes)
        return polinomios(nuevo_grado, nuevos_coeficientes)
                
    def __rfloordiv__(self,other):
        if isinstance(other, polinomios):
            return other.__floordiv__(self)[1]
        else:
            return polinomios(0, [other]).__floordiv__(self)[1]
        
    def __mod__(self, other):
        if isinstance(other, polinomios):
            poli = self
            poli.__floordiv__(other)
        return self.resto

    def __rmod__(self, other):
        if isinstance(other, polinomios):
            return other.__floordiv__(self)[1]
        else:
            return polinomios(0, [other]).__floordiv__(self)[1]


    def PrimeraDerivada(self):
        primera_derivada_coef=[self.coef[i]*i for i in range(1, self.grado +1)]
        return polinomios(self.grado-1, primera_derivada_coef)
        
    def rootfindNewton(self, x0=1, tolerance = 1e-5, iter = 1000):
        aproximacion_actual = x0
        it = 0
        f_xa = 0
        while it < iter:
            f_xa = self(aproximacion_actual)  #Esto e slo mismo que call
            if abs(f_xa) < tolerance: return aproximacion_actual
            
            derivada_xn = self.PrimeraDerivada()(f_xa) #Usar doble parentesis, es lo mismo que hacer polis(a), porque self.Primeraderivada() devuelve un polinomio
            
            if derivada_xn == 0: raise ValueError (f"La derivada en el punto {aproximacion_actual} es cero")
            
            aproximacion_actual = aproximacion_actual - f_xa/derivada_xn
            iter +=1
        return None

    # def rootfindBiseccion(self,a=0 ,b=1000):
    #     F_a = self.__call__(a)
    #     F_b = self.__call__(b)
    #     if F_a * F_b <=0: #Hay raiz entre medio
    #         if round(F_a,4) == 0:
    #             raiz = a
    #         elif round(F_b,4) ==0:
    #             raiz = b
    #         else:
    #             c = (a+b)/2
    #             F_c = self.__call__(c)
    #             if round(F_c * F_a, 4 )<0: #hay raiz entre a y c
    #                 b = c
    #                 raiz = self.rootfindBiseccion(a,b)
    #             elif round(F_c * F_a , 4)== 0:
    #                 raiz = c
    #             else: #hay raiz entre c y b
    #                 a = c
    #                 raiz = self.rootfindBiseccion(a,b)
    #         return round(raiz,2)
    def rootfindBiseccion(self, a = -1, b = 3, tolerance = 1e-5, iter = 1000):
        '''
        Toma como parametro dos valores entre los cuales buscar la raiz real del polinomio; tolerancia del 0; iteraciones.
        a*b <= 0. 
        Devuelve una raiz real del polinomio. Caso contrario, da error
        '''
        iter_count = 0
        if a * b > 0: raise ValueError("No se puede garantizar la existencia de una raíz en el intervalo dado.")

        while iter_count < iter:
            c = (a+b) / 2
            if abs(self(c)) <= tolerance: return c
            if self(a) * self(c) < 0: b = c
            else: a = c
            iter_count += 1
        
        print(f"El método de bisección no convergió después de {iter} iteraciones.")
        return None
    
    def rootfindSecante(self, x0=-10, x1=10, tolerance=1e-5, iter=100000):
        iterations = 0
        while iterations<iter:
            # print(f'El polinomio {self.get_expression()} en X0 = {x0}, es = {self(x0)}')
            # print(f'El polinomio {self.get_expression()} en X1 = {x1}, es = {self(x1)}')
            if abs(self(x1)-self(x0))<1e-10: raise ValueError("la diferencia entre x0 y x1 es demasiado chcia")
            
            root = x0 - self(x0) *(x1-x0) / (self(x1) - self(x0))
            if abs(self(root))<tolerance: 
                return root
            x0 = x1
            x1 = root
            iterations +=1
            
        
        return None



# "QUOTIENTE ES LO QUE ME DEVUELVE FLOORDIV"    
# "REMAINDER ES LO QUE ME DEVUELVE MOD"         
    def findroots(self):
        roots = []
        polinomio_residual = self
    
        while polinomio_residual.grado > 0:
            root = polinomio_residual.rootfindSecante()   
            if not root:
                break
            
            multiplicidad = 0

            
            cociente = polinomio_residual.__floordiv__(polinomios(1, [-root, 1]))
            resto = polinomio_residual.__mod__(polinomios(1, [-root,1]))

            if resto.grado == 0 and abs(resto.coef[0]) < 1e-3:
                multiplicidad += 1
                polinomio_residual = cociente
            else:
                break

            if multiplicidad > 0:
                roots.append((round(root,3), multiplicidad))
        print (roots)
        print(polinomio_residual.get_expression())
        return roots, polinomio_residual
             

        

grado = 2
coef = [-5,-2,10]
poli = polinomios(grado,coef)
# poli.get_expression()
# # print(poli.__call__(2))
# poli.poly_plt(-10,10)
# poliB = polinomios(1,[-2,1])
# # suma = poli.__add__(poliB)
# # resta = poli-poliB
# # multi = poli*3
# division = poli//poliB
# print(division.get_expression())
# mod = poli.__mod__(poliB)
# print(mod.get_expression())
# # mod = poli.__mod__(poliB)
# print(poli.rootfindNewton())
# print(poli.rootfindBiseccion())
# print(poli.rootfindSecante())
print(poli.findroots())




#%% Sub Class Polinomios de Lagrange

class PolinomiosDeTaylor (polinomios):
    def __init__(self, fT, N, x0, h):
        self.fT = fT
        self.N = N
        self.x0 = x0
        self.h = h
        self.feval = [self.fT(self.x0+(self.N-(2*i))*self.h) for i in range(self.N + 1)]
        self.fprime = [self.derivada_n(j) for j in range (self.N+1)]
        self.prtTaylor = True
        # self.digits = digits
        # super(Taylor, self.__init__(self.get_parms()))
    
    

    def pascal(self,n):
            
            triangulo_de_pascal = [[1],[1,1]]
            if n==0: 
                resultado = [triangulo_de_pascal[0]]
            elif n==1: 
                resultado = triangulo_de_pascal
            else:
                for i in range(2,n+1,):
                    tira = triangulo_de_pascal[i-1]
                    nueva_tira = [1]
                    for posicion, num in enumerate(tira):
                        if posicion+1 <len(tira):
                            nuevo_num = tira[posicion]+tira[posicion+1]
                            nueva_tira.append(nuevo_num)
                       
                        else:
                            nueva_tira.append(1)
                            break
                            
                    triangulo_de_pascal.append(nueva_tira)   
                    resultado = triangulo_de_pascal 
                    
                    
            # print (resultado)
            return resultado

    def numero_combinatorio (self,n,i):
        triangulo = self.pascal(n)
        
        combinatorio = triangulo[n][i]
        
        # print(combinatorio)
        return combinatorio
        

    def derivada_n(self,n):
        h = self.h
        derivada_n = 0
        for i in range(n+1):
            derivada_n += ((-1)**i)*self.numero_combinatorio(n,i)*self.feval[i]
        
        derivada_n = derivada_n/((2*h)**n)
        
        # print(round(derivada_n,2))
        return round(derivada_n,4)
    
   

    def factorial (self,n):
        factorial = 1
        for i in range (1,n+1):
            factorial *=i
            
        return factorial
    
    
    
    def get_parms(self):
        f0 = self.fT(self.x0) 
        lista = [self.x0*(-1),1]
        producto= polinomios(0,[f0])
        
        for i in range (1,n+1):
            poli = polinomios(len(lista)-1, lista)
            derivada_i = self.derivada_n(i)
            num = derivada_i/self.factorial(i)
            # print(num)
            "Aca tengo el coeficiente que multiplica al (x-x0)**i"
            if i==1:
                poli = poli*num
                
            else: 
                for e in range (2, i+1):
                    poli = poli*poli
                poli = poli*num                
            "Aca el producto del coeficeinte por (x-x0)**i"
            
            producto += poli
           
        coeficientes = producto.coef
        
        
        # print(coeficientes)
        return (coeficientes)
           
    def __str__(self):
        if self.prtTaylor==True:
            print(self.fT(self.x0),end="")
            for i in range(1, n+1):
                print("+",self.fprime[i],"* ((x -", self.x0, ") **", i, ")/", i, "!")
        
        else:
            coeficientes = self.get_parms()
            poli = polinomios(len(coeficientes)-1,coeficientes)
            return poli.get_expression()     

# fT = poli
# N = 2
# x0 = 1
# h= 0.0001

# polyT = PolinomiosDeTaylor(fT, N, x0,h)
# n =2
# k=2
# polyT.derivada_n(n)
# polyT.__str__()

# polyT.get_parms()

            

            
                
#%% Sub Class Polinomios de Taylor

class PolinomiosDeTaylor (polinomios):
    def __init__(self, fT, N, x0, h):
        self.fT = fT
        self.N = N
        self.x0 = x0
        self.h = h
        self.feval = [self.fT(self.x0+(self.N-(2*i))*self.h) for i in range(self.N + 1)]
        self.fprime = [self.derivada_n(j) for j in range (self.N+1)]
        self.prtTaylor = True
        # self.digits = digits
        # super(Taylor, self.__init__(self.get_parms()))
    
    

    def pascal(self,n):
            
            triangulo_de_pascal = [[1],[1,1]]
            if n==0: 
                resultado = [triangulo_de_pascal[0]]
            elif n==1: 
                resultado = triangulo_de_pascal
            else:
                for i in range(2,n+1,):
                    tira = triangulo_de_pascal[i-1]
                    nueva_tira = [1]
                    for posicion, num in enumerate(tira):
                        if posicion+1 <len(tira):
                            nuevo_num = tira[posicion]+tira[posicion+1]
                            nueva_tira.append(nuevo_num)
                       
                        else:
                            nueva_tira.append(1)
                            break
                            
                    triangulo_de_pascal.append(nueva_tira)   
                    resultado = triangulo_de_pascal 
                    
                    
            # print (resultado)
            return resultado

    def numero_combinatorio (self,n,i):
        triangulo = self.pascal(n)
        
        combinatorio = triangulo[n][i]
        
        # print(combinatorio)
        return combinatorio
        

    def derivada_n(self,n):
        h = self.h
        derivada_n = 0
        for i in range(n+1):
            derivada_n += ((-1)**i)*self.numero_combinatorio(n,i)*self.feval[i]
        
        derivada_n = derivada_n/((2*h)**n)
        
        # print(round(derivada_n,2))
        return round(derivada_n,4)
    
   

    def factorial (self,n):
        factorial = 1
        for i in range (1,n+1):
            factorial *=i
            
        return factorial
    
    
    
    def get_parms(self):
        f0 = self.fT(self.x0) 
        lista = [self.x0*(-1),1]
        producto= polinomios(0,[f0])
        
        for i in range (1,n+1):
            poli = polinomios(len(lista)-1, lista)
            derivada_i = self.derivada_n(i)
            num = derivada_i/self.factorial(i)
            # print(num)
            "Aca tengo el coeficiente que multiplica al (x-x0)**i"
            if i==1:
                poli = poli*num
                
            else: 
                for e in range (2, i+1):
                    poli = poli*poli
                poli = poli*num                
            "Aca el producto del coeficeinte por (x-x0)**i"
            
            producto += poli
           
        coeficientes = producto.coef
        
        
        # print(coeficientes)
        return (coeficientes)
           
    def __str__(self):
        if self.prtTaylor==True:
            print(self.fT(self.x0),end="")
            for i in range(1, n+1):
                print("+",self.fprime[i],"* ((x -", self.x0, ") **", i, ")/", i, "!")
        
        else:
            coeficientes = self.get_parms()
            poli = polinomios(len(coeficientes)-1,coeficientes)
            return poli.get_expression()     
# fT = poli
# N = 2
# x0 = 1
# h= 0.0001

# polyT = PolinomiosDeTaylor(fT, N, x0,h)
# n =2
# k=2
# polyT.derivada_n(n)
# polyT.__str__()

# polyT.get_parms()
            

#%% Sub Class de Polinomios de Lagrange
class PolinomiosDeLagrange (polinomios):
    
    def __init__(self, serie_de_puntos):
        self.serie_de_puntos = serie_de_puntos
        self.x_values = [tupla[0] for tupla in self.serie_de_puntos]
        self.y_values = [tupla[1] for tupla in self.serie_de_puntos]
        self.lagrange_coef = self.GetLagrange()
        self.lagrange_grado = len(self.lagrange_coef) - 1
        super().__init__(self.lagrange_grado, self.lagrange_coef)
    
    def GetLagrange (self):
        px= 0
        for posy, y in enumerate(self.y_values):
            wi = 1
            xi = self.x_values[posy]
            for posx, x in enumerate(self.x_values):
                if xi == x:
                    continue
                poli = polinomios(1, [-x,1])
                div = xi-x
                monomio = poli // div
                wi*= monomio
                # print(wi.get_expression())
            
            resultado = wi * y
            px+=resultado
        print(px.coef)
        return px.coef
        
    def get_poli(self):
        return polinomios(self.lagrange_grado, self.lagrange_coef)

# serie_de_puntos = [(-1,0),(0,-1),(2,3)]      
# lagrangiano = PolinomiosDeLagrange(serie_de_puntos) 


# coefs=lagrangiano.GetLagrange()
# a = lagrangiano.get_poli()
# print(a.get_expression())
# a.poly_plt(-10, 10)

#%% Sub Class Regresion Lineal
class linreg (polinomios):
    
    def __init__(self, datos):
        self.datos = datos
        self.x_values = [tupla[0] for tupla in self.datos]
        self.y_values = [tupla[1] for tupla in self.datos]
        self.x_mean = sum(self.x_values)/len(self.x_values)
        self.y_mean = sum(self.y_values)/len(self.y_values)
        self.beta_MCO = self.beta_MCO()
        self.alpha = self.y_mean - (self.beta_MCO*self.x_mean)
        
        super().__init__(grado=1, coef=[self.alpha, self.beta_MCO])
    
    def beta_MCO(self):
        num = 0
        denom =0
        for d in self.datos:
            num += ((d[0]-self.x_mean)*((d[1])-self.y_mean))
            denom += ((d[0]-self.x_mean)**2)
        beta = num/denom
        print(beta)
        return beta
    
    def __str__(self):
        expresion = ["Y=", str(round(self.alpha,3)), "+", str(round(self.beta_MCO,3)), "X"]
        respuesta = "".join(expresion)
        self.expresion = respuesta
        print(self.expresion)
        return (self.expresion)
        
    def regplot(self):
        plt.scatter(self.x_values,self.y_values)
        self.y_values_interpolated = self._interpolate()
        plt.plot(self.x_values, self.y_values_interpolated, color = 'red', label = self.__str__())
        plt.legend()
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("Regresion Lineal")
        plt.show()
    
    def _interpolate(self):
        new_y_values = [(self.alpha+(self.beta_MCO*x)) for x in self.x_values]
        return new_y_values
    
    def l(self,b):
        suma = []
        for d in self.datos:
            L = (d[1]-(self.alpha + b*d[0]))**2
            suma.append(L)
        suma_final = suma[0]
        for s in range(1, len(suma)):
            suma_final.__add__(s)
            return suma_final
    
    def lp(self, b, h=0.0001):
        primero = self.l(b-h)
        segundo = self.l(b+h)
        return (segundo - primero)// (2*h)
    
    def lpp(self, b, h=0.0001):
        primero = self.lp(b-h)
        segundo = self.lp(b+h)
        return (segundo - primero)// (2*h)
    
    
    def NR_reg(self):
        beta_encontrado = self.rootfind(self.lp(), self.lpp())
        print(beta_encontrado)
        return beta_encontrado
        
    
            
# datos = [(1,3),(2,1),(3,5),(4,7),(5,10)]     
# a = linreg(datos)
# a.regplot()

