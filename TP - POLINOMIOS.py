#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:42:36 2024

@author: finiballester
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:16:04 2024

@author: finiballester
"""
#PENDEINTE:
    #RADD
    #RSUB

#%%
import matplotlib.pyplot as plt
class polinomios (object):
    
    def __init__ (self, grado=0, coef=[0]):
        self.grado = grado
        self.coef = coef
        
        if grado < len(coef)-1:
            raise ValueError ("No puede ingresar un grado inferior a la cantidad de coeficientes.")

        
    def get_expression (self):
        px=[]
        for c in range(len(self.coef)):
            co = str(c)
            e = str(self.coef[c])
            n = e + 'X^' + co
            px.append(n)
            
        
            for n in px:
                expression = "P(x)=" + "+".join(px)
                self.expression = expression
        print (expression)
        return expression

    def __call__(self,x):
        nums = []
        for e in range(len(self.coef)):
            n = (x**e)*self.coef[e]
            nums.append(n)
            
        y_value = sum(nums)
        self.y_value = y_value
        return y_value


    def poly_plt(self, a, b, **kwargs):
        x_values = list(range(a, b+1))
        y_values = []
        for x in x_values:
            y = self.__call__(x)
            y_values.append(y)
            
        plt.scatter(x_values, y_values)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(0,color = 'black', linewidth = 0.5)
        plt.axvline(0,color = 'black', linewidth = 0.5)
        plt.title(self.expression)
        plt.show()
        
        
    def __add__(self, other):
        nuevos_coeficientes = []
        if isinstance(other, (int, float)):
            coef_other = [0]*(len(self.coef) -1)
            coef_other.append(other)
            for e in range(len(self.coef)):
                nuevos_coeficientes.append(self.coef[e] + coef_other[e])
                
            resultado = polinomios(grado = self.grado, coef = nuevos_coeficientes)
            
        elif isinstance(other, polinomios):
            mayor_grado = max(self.grado, other.grado)
            if self.grado == mayor_grado:
                coef_other = [0]*(len(self.coef)-len(other.coef))
                for e in other.coef:
                    coef_other.append(e)
                
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(self.coef[i]+coef_other[i])
                  
            else:
                coef_poli = [0]*(len(other.coef)-len(self.coef))
                
                for e in self.coef:
                    coef_poli.append(e)
                
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(other.coef[i]+coef_poli[i])
                
            resultado = polinomios(grado = mayor_grado, coef = nuevos_coeficientes)
        
        
        #print(resultado.coef)
        return resultado
        
    def __sub__(self, other):
        nuevos_coeficientes = []
        if isinstance(other, (int, float)):
            coef_other = [0]*(len(self.coef) -1)
            coef_other.append(other)
            for e in range(len(self.coef)):
                nuevos_coeficientes.append(self.coef[e] - coef_other[e])
                
            resultado = polinomios(grado = self.grado, coef = nuevos_coeficientes)
        #Aca podria achicar codigo y que sea para >=    
        elif isinstance(other, polinomios):
            mayor_grado = max(self.grado, other.grado)
            if len(self.coef) == len(other.coef):
                coef_other = [0]*(len(self.coef)-len(other.coef))
                for e in other.coef:
                    coef_other.append(e)
                
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(self.coef[i]-coef_other[i])
                  
            else:
                coef_poli = [0]*(len(other.coef)-len(self.coef))
                
                for e in self.coef:
                    coef_poli.append(e)
                
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(other.coef[i]-coef_poli[i])
                
            resultado = polinomios(grado = mayor_grado, coef = nuevos_coeficientes)
        
        
        #print(resultado.coef)
        return resultado        
        
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            coef_poli = []
            for e in self.coef:
                r = e*other
                if (e < 0 and other<0) or (e > 0 and other>0):
                    coef_poli.append(abs(r))
                else:
                    coef_poli.append(r)
            
            resultado = polinomios(grado = self.grado, coef = coef_poli)
            
            
        elif isinstance(other, polinomios):
           productos = []
           mayor_grado_nuevo = self.grado + other.grado
           comunes = [[i,0]for i in range(mayor_grado_nuevo+1)]
           nuevos_coeficientes = []
           for potencia_poli, e in enumerate (self.coef):
               for potencia_other, i in enumerate (other.coef):
                   c = e*i
                   g = potencia_poli+potencia_other
                       
                   l = [c,g]
                   productos.append(l)
                    
           for c in comunes:
                for p in productos:
                    if c[0] == p[1]:
                        c[1]=c[1]+p[0]
                            
                                
           for lista in comunes:
                nuevos_coeficientes.append(lista[1])
            
           resultado = polinomios(grado = len(nuevos_coeficientes), coef = nuevos_coeficientes)
         
        #print(resultado.coef)
        return resultado 
        
    def __floordiv__(self,other):
        if isinstance(other, (int,float)):
            nuevos_coeficientes = []
            for e in self.coef:
                nuevos_coeficientes.append(e//other)
            
            resultado = polinomios(grado=self.grado, coef = nuevos_coeficientes)
        
        elif isinstance(other, polinomios):
          
            if other.grado > self.grado:
                raise ValueError ("No se puede dividir por un polinomio de mayor grado.")
            
             
            else:
                grado_de_resultado = self.grado - other.grado
                self_poli = self
                self_coef = self.coef
                
                
                poli = (grado_de_resultado+1) * [0]
                nuevos_coeficientes = []
                while len(self_coef)>=len(other.coef):
                    self_poli = polinomios((len(self_coef)-1),self_coef)
                    grado_de_multiplicar = len(self_coef)-len(other.coef)
                    c = self_coef[-1]//other.coef[-1]
                    poli[grado_de_multiplicar]=c
                    p = [0]*(grado_de_multiplicar+1)
                    p[-1]=c
                    p = polinomios(len(p)-1, p)
                    poli_que_resto = other*p
                    self_coef = (self_poli-poli_que_resto).coef
                    cantidad = len(self_coef)
                    for posicion, number in enumerate (self_coef[::-1]):
                        if round(number, 4) == 0:
                            self_coef.pop(cantidad - (posicion+1))
                        else:
                            None
                            break
                if len(self_coef)==0:
                    self_poli = polinomios(0, [0])
                   
                self.resto = self_coef
                self.gradoderesto = len(self_coef)
               
                
            resultado = polinomios(grado = grado_de_resultado, coef = poli)
        
        print(resultado.coef)
        return resultado

        



    def __mod__(self, other):
        if isinstance(other, polinomios):
            poli = self
            poli.__floordiv__(other)
            resultado = polinomios(grado = self.gradoderesto, coef = self.resto)
        # print(resultado.coef)
        return resultado
            
    def rootfind(self,a=1 ,b=1000):
        
        F_a = self.__call__(a)
        F_b = self.__call__(b)
        
        if F_a * F_b <=0: #Hay raiz entre medio
            if round(F_a,4) == 0:
                raiz = a
            elif round(F_b,4) ==0:
                raiz = b
            
            else:
                c = (a+b)/2
                F_c = self.__call__(c)
                if round(F_c * F_a, 4 )<0: #hay raiz entre a y c
                    b = c
                    raiz = self.rootfind(a,b)
                elif round(F_c * F_a , 4)== 0:
                    raiz = c
                else: #hay raiz entre c y b
                    a = c
                    raiz = self.rootfind(a,b)

            return round(raiz,2)
                    
    def findroots(self):
        raiz = self.rootfind(a=1 ,b=1000)
    
        if raiz == None:
            return polinomios(self.grado, self.coef).coef
        else:
            raices = {raiz:1}
            cociente =self.__floordiv__(polinomios(grado = 1, coef = [raiz*(-1), 1]))
            
            while raiz != None:
                raiz = cociente.rootfind(a=-1000 ,b=1000)
                if raiz == None:
                    break
                cociente =cociente.__floordiv__(polinomios(grado = 1, coef = [raiz*(-1), 1]))
                if raiz in raices:
                    raices[raiz]+=1
                else:
                    raices[raiz]=1
            claves_dic = raices.keys()
            values_dic = raices.values()
            lista_final  = list(zip(claves_dic, values_dic))
            self.raices = lista_final
            return lista_final, cociente

    def factorize(self):
        poli = self
        poli.findroots()
        raices = self.raices
        
        factorizado = []
        
        for e in raices:
            raiz = str(e[0])
            multiplicidad = str(e[1])
            
            e = ["(x-",raiz,")**", multiplicidad]
            j = ''.join(e)
            factorizado.append(j)
        
        respuesta = "P(x)="+"+".join(factorizado)
        
        print(respuesta)
        return respuesta
            
            
##### ME FALTA EL ULTIMO ITEM #######           
       
                     
#%%                

    

grado = 2
coef = [8,4,2]
poli = polinomios(grado,coef)
poli.get_expression()

# a=-20
# b=20
# poli.poly_plt(a, b)

# i = -2
#h= polinomios(2,[0,4,-1])
# n = poli.__add__(i)
# n.get_expression()
# m = poli.__add__(h)
# m.get_expression()

# k = polinomios(2, [0,4,-1])
# p = poli.__sub__(i)
# p.get_expression()
# l = poli.__sub__(k)
# l.get_expression()

# r = polinomios(1, [2,2])
# q = poli.__mul__(i)
# q.get_expression()
# q.poly_plt(a, b)
# w = poli.__mul__(3)
# w.get_expression()
# z = poli * 3
# z.get_expression()


# x = poli.__floordiv__(k)
# x.get_expression()
# o =poli.__mod__(k)
# o.get_expression()

# a=1
# b=1000
# print(poli.rootfind(a, b))

# poli.findroots()
# print (poli.findroots())
# poli.factorize()

"NOTES"
"Cuando tengo una parabola tengo que ajustar los valores de a y b para que funcione el metodo porque si son muy grandes cree que no hay cambio de signo." 
"Por lo tanto, graficar el polinomio y observar que paraemtros conviene poner."
    
    
    
    
    
 



#%%

class PolinomiosDeTaylor (polinomios):
    def __init__(self, fT, N, x0, h=0.01):
        self.fT = fT
        self.N = N
        self.x0 = x0
        self.h = h
        # self.feval = [self.fT(self.x0+(self.N-i)*self.h) for i in range(self.N + 1)]
        # self.fprime = [self.derivada_n(j) for j in range (self.N+1)]
        # self.prtTaylor = True
        #self.digits = digits
        #super(Taylor, self.__init__(self.get_parms))
    # def __str__(self):
    #     if self.prtTaylor==True:
    #         taylor = []
    #         for i in range(N):
    

    def numeros_combinatorios(n):
    
        triangulo_de_pascal = [[1],[1,1]]
    
        for i in range(2,n,):
            tira = triangulo_de_pascal[i-1]
            nueva_tira = [1]
            for posicion, num in enumerate(tira):
                if posicion+1 <len(tira):
                    nuevo_num = tira[posicion]+tira[posicion+1]
                    nueva_tira.append(nuevo_num)
               
                else:
                    nueva_tira.append(1)
                    
                    
                triangulo_de_pascal.append(nueva_tira)   
            
            
            
            print (triangulo_de_pascal)
            return triangulo_de_pascal
   
    def derivada_n(self,n):
        derivadas_de_i =[]
        h = self.h
        x0 = self.x0
        fT = self.fT
        derivadas_de_i = []
        for i in range (n):
            pascal= self.numeros_combinatorios(i)
            coeficientes = pascal[i]
            coeficientes_con_signo = []
            num = (n-(2*i))*h
            elementos=[]
            for posicion, coeficiente in coeficientes:
                signo = (-1)**posicion
                coef= signo*coeficiente
                coeficientes_con_signo.append(coef)
            
            for c in coeficientes_con_signo:
                elemento = c*fT(x0+num)
                elementos.append(elemento)
            
            derivada_de_i = sum(elementos)
            derivadas_de_i.append(derivada_de_i)
            
        suma = sum(derivadas_de_i)
        derivada_n = suma/((2*h)**n)
        
        print(derivada_n)
        return derivada_n
        
        
fT = poli
N = 2
x0 = 2

polyT = PolinomiosDeTaylor(fT, N, x0)
n =3
polyT.derivada_n(polyT, n)
 


            
            
    
        
        
        
