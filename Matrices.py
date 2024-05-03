#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:46:07 2024

@author: finiballester
"""

#%% MYARRAY
class myarray():
    
    def __init__(self, elems, r, c):
        self.elems=elems
        self.r = r
        self.c = c
        self.byrow= True
   
    def get_pos(self, j, k):
        if len(self.elems)!= (self.r)*(self.c):
            raise ValueError ("En la lista elems no hay suficientes elementos para crear la matriz de esa dimension.")
        else:
            if self.byrow == True:
                posicion = (j-1)*self.c+(k-1)
                # m =self.elems[posicion]
            else:
                posicion = (k-1)*self.r+(j-1)
                # m =self.elems[posicion]
            # print ("La posicion del elemento", m, "en la lista elems es", posicion)
            return posicion

    def get_coords(self, m):
        fila = 1
        columna = m+1
        while columna > self.c:
            fila+=1
            columna -= self.c
        print ("El numero en la posicion incertada(m) en la lista es", self.elems[m])
        print("La posicion del elemento en la matriz es", (fila, columna))
        return (fila,columna)
    
    
    def switch (self):
        elements_nuevos = []

        if self.byrow == True:
            for e in range (self.c):
                pos=e
                for i in range (self.r):
                    elements_nuevos.append(self.elems[pos+(i*self.c)])
            self.byrow = False

        else:
            for e in range (self.r):
                pos=e

                for i in range (self.c):
                    elements_nuevos.append(self.elems[pos+(i*self.r)])
            self.byrow = True

        self.elems = elements_nuevos
        print(self.elems)
        return myarray(self.elems, self.r, self.c)   
    
    def get_row (self, j):
        primer_elemento_pos = self.c * (j-1)
        fila = []
        for posicion in range(self.c):
            fila.append(self.elems[primer_elemento_pos+posicion])
        return fila
    
    def get_col (self,k):
        primer_elemento_pos = k-1
        salteador = self.c
        columna = []
        for posicion in range(self.r):
            columna.append(self.elems[primer_elemento_pos+(posicion*salteador)]) 
        return columna
    
    def get_elem(self, j,k):
        fila = self.get_row(j)
        element = fila[k-1]
        return element
        
    def get_submatrix (self, row_list, col_list):
        sub_matrix = []
        for i in row_list:
            fila = self.get_row(i)
            for e in col_list:
                element = fila[e-1]
                sub_matrix.append(element)
        print(sub_matrix)        
        return myarray(sub_matrix, len(row_list), len(col_list))
    
    def add (self, B):
        suma = self.elems
        if isinstance (B, myarray):
            for posicion, i in enumerate(B.elems):
                suma[posicion]+=i
        else:
            raise ValueError ("No se pueden sumar matrices de distinta dimension. ")
        print (suma)
        return myarray(suma, self.r, self.c)    
            
    def sub (self,B):
        resta = self.elems
        if isinstance (B, myarray):
            for posicion, i in enumerate(B.elems):
                resta[posicion]-=i
        else:
            raise ValueError ("No se pueden restar matrices de distinta dimension. ")
        print (resta)
        return myarray(resta, self.r, self.c)    

    def mult_x_derecha(self, B):
        producto = []
        if isinstance(B, myarray):
            if self.c != B.r:
                raise ValueError ("La primer matriz debe tener el mismo numero de columnas que la segunda de filas.")
            
            else:
                for i in range(self.r):
                    row = self.get_row(i+1)
                    
                    for e in range (B.c):
                        column = B.get_col(e+1)
                        
                        aux = []
                        for j in range (self.c):
                            p = row[j]*column[j]
                            aux.append(p)
                        
                        productito = sum(aux)
                        producto.append(productito)
            resultado = myarray(producto, self.r, B.c)
        elif isinstance(B, (int,float)):
            for element in self.elems:
                producto.append(element*B)
            resultado = myarray(producto, self.r, self.c)
        else:
            None
                
        # print(producto)
        
        return resultado
    
    def mult_x_izquierda(self, B):
        producto = []
        if isinstance(B, myarray):
            if B.c != self.r:
                raise ValueError ("La primer matriz debe tener el mismo numero de columnas que la segunda de filas.")
            
            else:
                for i in range(B.r):
                    row = B.get_row(i+1)
                    
                    for e in range (self.c):
                        column = self.get_col(e+1)
                        
                        aux = []
                        for j in range (B.c):
                            p = row[j]*column[j]
                            aux.append(p)
                        
                        productito = sum(aux)
                        producto.append(productito)
            resultado = myarray(producto, B.r, self.c)
        elif isinstance(B, (int,float)):
            for element in self.elems:
                producto.append(element*B)
            resultado = myarray(producto, self.r, self.c)   
        else:
            None
                
        # print(producto)
        return resultado

    def power(self,n):
        if self.c != self.r:
            raise ValueError ("No se puede elevar una matriz que no es cuadrada.")
        
        else:
            if n==0:
                resultado = myarray(1, 1, 1)
            elif n ==1:
                resultado = self
            
            else:
                resultado = self
                for i in range (n):
                    resultado = resultado.mult_x_derecha(self)
          
        return myarray(resultado, self.r, self.c)
    
    
    
    def matriz_identidad(self,a, b):
        elements = [0]*(a*b)
        for i in range (0,len(elements),b+1):
            elements[i]=1
            
        self.elements_identidad=elements
        # print(elements)
        return myarray(elements, a, b)


    # def del_row_primer_version(self, j):
    #     elements = []
    #     primer_elemento_pos = self.c * (j-1)
        
    #     for posicion in range(0, primer_elemento_pos):
    #         elements.append(self.elems[posicion])
            
    #     for posicion in range(primer_elemento_pos+self.c,len(self.elems),):
    #         elements.append(self.elems[posicion])
        
    #     print (elements)
    #     return myarray(elements, self.r-1, self.c)


    def del_row (self,j):
        element = self.get_elem(j,1)
        nuevos_elements = self.elems[0:element-1:1]+self.elems[element+self.c-1:len(self.elems):1]
        
        print(nuevos_elements)
        return myarray(nuevos_elements, self.r-1, self.c)    
        
   
    def del_col (self,k):
        nuevos_elements = self.elems
        primer_elemento = k-1
        indices_a_eliminar =[]
        
        for i in range(primer_elemento,len(self.elems), self.c-1):
            indices_a_eliminar.append(i)
        
        for posicion, element in enumerate(nuevos_elements):
            for indice in indices_a_eliminar:
                if posicion == indice:
                    nuevos_elements.pop(indice)
                
        print (nuevos_elements)
        return myarray(nuevos_elements, self.r, self.c-1)


    def get_transpose(self):
        nuevos_elements = []
        for i in range(1,self.c+1):
            column = self.get_col(i)
            
            for c in column:
                nuevos_elements.append(c)
        
        print(nuevos_elements)
        return myarray(nuevos_elements, self.c, self.r)
    
    
    def swap_rows(self,i,j):
        if i >self.r or j > self.r:
            raise ValueError("No hay tantas filas en esta matriz")
        else:
            identidad = self.matriz_identidad(a=self.r,b=self.r)
            
            posicion_i = identidad.get_pos(i, i)
            posicion_j = identidad.get_pos(j, j)
            
            elements_identidad = identidad.elems
            
            elements_permuta = elements_identidad
            
            elements_permuta[posicion_i]=0
            elements_permuta[posicion_j]=0
            
            elements_permuta[(posicion_i)-(i-j)]=1
            elements_permuta[(posicion_j)-(j-i)]=1

            # print(elements_permuta)
            matriz_permuta = myarray(elements_permuta, identidad.r, identidad.c)
            
        
        
        resultado = self.mult_x_izquierda(matriz_permuta)
        
        # print(resultado.elems)
        return resultado
   
    
    def swap_cols(self,l,k):
        if l >self.c or k > self.c:
            raise ValueError("No hay tantas filas en esta matriz")
        else:
            identidad = self.matriz_identidad(a=self.c, b=self.c)
            
            posicion_l = identidad.get_pos(l, l)
            posicion_k = identidad.get_pos(k, k)
            
            elements_identidad = identidad.elems
            
            elements_permuta = elements_identidad
            
            elements_permuta[posicion_l]=0
            elements_permuta[posicion_k]=0
            
            elements_permuta[(posicion_l)-(l-k)]=1
            elements_permuta[(posicion_k)-(k-l)]=1

            # print(elements_permuta)
            matriz_permuta = myarray(elements_permuta, identidad.r, identidad.c)
            
        
        
        resultado = self.mult_x_derecha(matriz_permuta)
        
        # print(resultado.elems)
        return resultado
    
    def scale_row(self,j,x):
        identidad = self.matriz_identidad(self.r, self.r)
        elems_permutantes = identidad.elems
        posicion_permutante = identidad.get_pos(j,j)
        elems_permutantes[posicion_permutante]=x
        
        resultado = self.mult_x_izquierda(myarray(elems_permutantes, self.r, self.r))
        # print(resultado.elems)
        return resultado


    def scale_col(self,k,y):
        identidad = self.matriz_identidad(self.c, self.c)
        elems_permutantes = identidad.elems
        posicion_permutante = identidad.get_pos(k,k)
        elems_permutantes[posicion_permutante]=y
        
        resultado = self.mult_x_derecha((myarray(elems_permutantes, self.c, self.c)))
        return resultado



    def flip_rows(self):
        matriz = self
        for i in range(1,int(self.r/2)+1):
            j = (self.r-i)+1
            resultado =matriz.swap_rows(i, j)
            matriz = resultado
           
     
        return resultado

    def flip_cols(self):
        matriz = self
        for i in range(1,int(self.c/2)+1):
            j = (self.c-i)+1
            resultado =matriz.swap_cols(i, j)
            matriz = resultado
           
        return resultado

   
    def det(self):
        if self.r != self.c:
            raise ValueError ("Las matrices que no son cuadradas no tienen determinante")
        
        elif self.c == 2 and self.r ==2:
             return (self.elems[0]*self.elems[3])-(self.elems[1]*self.elems[2])
        
        else:
            first_row = self.get_row(1)
            determinante =0
            row_list = [n for n in range (2,self.r+1)]
            # print (row_list)
            for e in range(1,self.c+1):
                col_list =  [m for m in range (1, self.c+1) if m!=e]
                # print (col_list)
                matriz = self.get_submatrix(row_list, col_list)
                determinante += first_row[e-1]*((-1)**(e+1))*matriz.det()
 
            return determinante
       


    def Minverse(self):
        if self.det()==0 or self.r!= self.c:
            raise ValueError ("No se puede calcular la inversa de esta matriz.")
        
        else:
            A = myarray(self.elems, self.r, self.c)
            inversa = self.matriz_identidad(self.r, self.r)
            for i in range(1,self.c+1):
                columna = A.get_col(i)
                pivot = columna[i-1]
                col = myarray(columna, self.r, 1)
                col_alterada = col.mult_x_izquierda(-1/pivot)
                col_alterada.elems[i-1]=1/pivot
                # print(col_alterada.elems)
                primer_element_de_col = i-1
                pos_col = 0
                identidad_alterada = A.matriz_identidad(self.r, self.r)
                for pos, element in enumerate(identidad_alterada.elems):
                    # identidad = self.matriz_identidad(self.r, self.r)
                    if primer_element_de_col == pos:
                        identidad_alterada.elems[pos] = col_alterada.elems[pos_col]
                        primer_element_de_col += self.c
                        pos_col+=1
                A = A.mult_x_izquierda(identidad_alterada)
                # print("identidad alterada:")
                # print(A.elems)
                inversa = inversa.mult_x_izquierda(identidad_alterada)
                # print("inversa:")
                # print(inversa.elems)
            print(inversa.elems)
            return inversa

     
                    
                
                
        


elems = [2,3,3,5]
r = 2
c = 2

matriz = myarray(elems, r, c)
# j = 3
# k = 1
# matriz.get_pos(j, k)

# matriz.get_coords(8)
# print(matriz.get_row(1))
# print(matriz.get_col(2))
# print(matriz.get_elem(1,2))
# print(matriz.get_submatrix([1,2], [2,3]))
# matriz.del_row(1)
# matriz.switch()

B_elems = [1,2,3,4,5,6,7,8,9]
B = myarray(B_elems, 3, 3)
# B=4
# matriz.add(B)
# matriz.sub(B)
# matriz.mult_x_derecha(B)
# print(matriz.mult_x_izquierda(2))
# matriz.power(3)
# matriz.matriz_identidad()
# matriz.del_col(1)
# matriz.del_row(2)
# A =matriz.get_transpose()
# A.get_transpose()
# matriz.swap_rows(1, 3)
# matriz.swap_cols(2, 3)
# matriz.scale_row(2, 5)
# matriz.scale_col(1,3)
# print(matriz.flip_rows().elems)
# matriz.flip_cols()
# print(matriz.det())
matriz.Minverse()

#%%

class lineq(myarray):
    
    def __init__(self, lista_A, N, byrow, lista_b):
        self.lista_A = lista_A
        self.N = N
        self.byrow = True
        self.lista_b = lista_b
    
    
















 