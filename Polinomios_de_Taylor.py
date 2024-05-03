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
    #RMULT
    #ITEM M: DIVIDIR

#%% Super clase POLY
import math
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
            coef_other =[]
            coef_other.append(other)
            if len(coef_other)<len(self.coef):
                coef_other.append(0)
            
            for e in range(len(self.coef)):
                nuevos_coeficientes.append(self.coef[e] + coef_other[e])
                
            resultado = polinomios(grado = self.grado, coef = nuevos_coeficientes)
            
        elif isinstance(other, polinomios):
            mayor_grado = max(self.grado, other.grado)
            if self.grado == mayor_grado:
                coef_other = []
                for e in other.coef:
                    coef_other.append(e)
                if len(coef_other)<len(self.coef):
                    coef_other.append(0)
                for i in range(len(self.coef)):
                    nuevos_coeficientes.append(self.coef[i]+coef_other[i])
                  
            else:
                coef_poli = []
                
                for e in self.coef:
                    coef_poli.append(e)
                if len(coef_poli)<len(other.coef):
                    coef_poli.append(0)
                for i in range(len(other.coef)):
                    nuevos_coeficientes.append(other.coef[i]+coef_poli[i])
                
            resultado = polinomios(grado = mayor_grado, coef = nuevos_coeficientes)
        
        
        # print(resultado.coef)
        return resultado
        
    def __sub__(self, other):
        nuevos_coeficientes = []
        if isinstance(other, (int, float)):
            coef_other = []
            coef_other.append(other)
            if len(coef_other)<len(self.coef):
                coef_other.append(0)
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
                coef_poli = []
                
                for e in self.coef:
                    coef_poli.append(e)
                if len(coef_poli)<len(other.coef):
                    coef_poli.append(0)
                
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
        
        # print(resultado.coef)
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
        
        # print(respuesta)
        return respuesta
            
            
##### ME FALTA EL ULTIMO ITEM #######           
       
                     
#%%                

    

# grado = 2
# coef = [8,4,2]
# poli = polinomios(grado,coef)
# poli.get_expression()

# a=-20
# b=20
# poli.poly_plt(a, b)

# i = -2
# h= polinomios(0,[14])
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
    
#%% Sub clase Poly de Taylor

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



#%%       
#fT = math.sin       
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
            
"2"            
# fT= math.exp
# x0 = 0 

# # polyB = PolinomiosDeTaylor(fT, N, x0,0.01)
# # polyC = PolinomiosDeTaylor(fT, N, x0,0.001)

# a=-10
# b=10


# polyA= PolinomiosDeTaylor(fT, N, x0,0.1).get_parms() 
# a = polinomios(len(polyA)-1, polyA)
# a.poly_plt(a, b)      
        
#%% Sub clase Poly de Lagrange

class PolinomiosDeLagrange (polinomios):
    
    def __init__(self, serie_de_puntos):
        self.serie_de_puntos = serie_de_puntos
        self.grado_lagrange = len(serie_de_puntos)-1
        self.coef_lagrange = [i[1] for i in serie_de_puntos]
    
    def wi (self, punto):
        parte_de_arriba = []
        parte_de_abajo = []
        
        for e in self.serie_de_puntos:
            if e!= punto:
                pol_U = polinomios(1, [-e[0],1])
                parte_de_arriba.append(pol_U)
                div = punto-e[0]
                parte_de_abajo.append(div)
        productos = []
        for e in parte_de_arriba:
            for i in parte_de_arriba:
                if i!=e:
                    producto = e.__mul__(i)
                    productos.append(producto)           
        suma = productos[0]
        for x in productos:
            suma = suma.__add__(x)
            
        division = 1
        for e in parte_de_abajo:
            if e!=0:
                division*=e 
            
        resultado  = suma.__floordiv__(division) 
        return resultado


    def px(self):
        suma = polinomios(0,[0])
        for i in self.serie_de_puntos:
            productito =self.wi(i[0])* i[1] 
        
        suma.__add__(productito)
        
        
        
        return suma
            






            
                
serie_de_puntos = [[-1,0],[0,-1],[2,3]]      
lagrangiano = PolinomiosDeLagrange(serie_de_puntos) 

a=lagrangiano.px()
a.get_expression()
