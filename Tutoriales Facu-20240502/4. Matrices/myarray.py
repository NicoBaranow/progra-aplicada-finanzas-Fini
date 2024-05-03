class myarray:
    def __init__(self, lista, r, c, by_row=True):
        self.elems = lista
        self.r = r
        self.c = c
        self.by_row = by_row
        self.original_by_row = by_row
        
        if not self.by_row:
            aux = self.switch()
            self.elems = aux.elems
            self.by_row = aux.by_row
            
    def get_pos(self, j, k):
        """ Devuelve el índice en la lista elems para el elemento en la posición (j, k) de la matriz. """
        if j > self.r or k > self.c:
            print('Coordenadas fuera del rango de la matriz')
            return None
            
        if self.by_row:
            return (j-1) * self.c + k - 1
        else:
            return (k-1) * self.r + j - 1

    def get_coords(self, m):
        """ Devuelve las coordenadas (j, k) en la matriz para el índice m en la lista elems. """
        if self.by_row:
            return (m // self.c + 1, m % self.c + 1)
        else:
            return (m % self.r + 1, m // self.r + 1)

    def switch(self):
        """ Cambia el modo de almacenamiento de la matriz de fila a columna o viceversa. """
        new_elems = []
        if self.by_row:
            for k in range(1, self.c + 1):
                for j in range(1, self.r + 1):
                    new_elems.append(self.elems[self.get_pos(j, k)])
        else:
            for j in range(1, self.r + 1):
                for k in range(1, self.c + 1):
                    new_elems.append(self.elems[self.get_pos(j, k)])
                    
        new_obj = myarray(new_elems, self.r, self.c, not(self.by_row))
        return new_obj
        
    def __str__(self):
        need_switch = self.original_by_row != self.by_row
        if need_switch:
            self.switch()  
        result = ""
        for j in range(1, self.r + 1):
            row = [self.elems[self.get_pos(j, k)] for k in range(1, self.c + 1)]
            result += "[" + ", ".join(map(str, row)) + "]\n"
        if need_switch:
            self.switch()  
        return result
    
    def get_row(self, j):
        """ Devuelve la fila j de la matriz. """
        elems = [self.elems[self.get_pos(j, k)] for k in range(1, self.c + 1)]
        return myarray(elems, 1, self.c)

    def get_col(self, k):
        """ Devuelve la columna k de la matriz. """
        elems = [self.elems[self.get_pos(j, k)] for j in range(1, self.r + 1)]
        return myarray(elems, self.r, 1)
    
    def get_elem(self, j, k):
        """ Devuelve el elemento en las coordenadas (j, k). """
        return self.elems[self.get_pos(j, k)]
    
    
    def _row_getter(self, j):
        getter_elems = [1 if i == j else 0 for i in range(1, self.r+1)]
        return myarray(getter_elems, 1, self.r)
    
    def _col_getter(self, j):
        getter_elems = [1 if i == j else 0 for i in range(1, self.c+1)]
        return myarray(getter_elems, self.c, 1)
        
    def get_row_algebra(self, j):
        row_getter = self._row_getter(j)
        return row_getter * self
    
    def get_col_algebra(self, j):
        col_getter = self._col_getter(j)
        return self * col_getter
        
    def get_elem_algebra(self, j, k):
        row_getter = self._row_getter(j)
        col_getter = self._col_getter(k)
        return row_getter * self * col_getter

    def get_submatrix(self, row_list, col_list):
        """ Devuelve una submatriz especificada por listas de índices de filas y columnas. """
        submatrix = []
        for j in row_list:
            for k in col_list:
                submatrix.append(self.elems[self.get_pos(j, k)])
        return myarray(submatrix, len(row_list), len(col_list), by_row = True)

    def del_row(self, j):
        """ Retorna un nuevo objeto myarray sin la fila j. """
        all_cols = set(range(1, self.c + 1))
        all_rows = set(range(1, self.r + 1))
        needed_rows = all_rows - {j}
        return self.get_submatrix(list(needed_rows), list(all_cols))

    def del_col(self, k):
        """ Retorna un nuevo objeto myarray sin la columna k. """
        all_cols = set(range(1, self.c + 1))
        all_rows = set(range(1, self.r + 1))
        needed_cols = all_cols - {k}
        return self.get_submatrix(list(all_rows), list(needed_cols))

    
    def swap_rows(self, j, k):
        """ Intercambia dos filas j y k de la matriz. """

        new_elems = self.elems.copy()
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        
        row_j = new_obj.get_row(j).elems
        row_k = new_obj.get_row(k).elems
        for col in range(1, self.c + 1):
            new_obj.elems[new_obj.get_pos(j, col)] = row_k[col-1]
            new_obj.elems[new_obj.get_pos(k, col)] = row_j[col-1]
        
        return new_obj
    
    def swap_cols(self, l, m):
        """ Intercambia dos columnas l y m de la matriz. """
        new_elems = self.elems.copy()
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        
        col_l = new_obj.get_col(l).elems
        col_m = new_obj.get_col(m).elems
        for row in range(1, self.r + 1):
            new_obj.elems[self.get_pos(row, l)] = col_m[row-1]
            new_obj.elems[self.get_pos(row, m)] = col_l[row-1]
                
        return new_obj


    def get_zeros(self):
        elems = [0 for j in range(1, self.r+1) for k in range(1, self.c+1)]
        return myarray(elems, self.r, self.c, by_row = True)
        
    def swap_rows_algebra(self, j, k):
        perm_rows = self.get_identity()
        perm_rows.elems[perm_rows.get_pos(j, j)] = 0
        perm_rows.elems[perm_rows.get_pos(k, k)] = 0
        perm_rows.elems[perm_rows.get_pos(j, k)] = 1
        perm_rows.elems[perm_rows.get_pos(k, j)] = 1
        
        return perm_rows * self
    
    
    def swap_cols_algebra(self, j, k):
        perm_cols = self.get_identity(n = self.c)
        perm_cols.elems[perm_cols.get_pos(j, j)] = 0
        perm_cols.elems[perm_cols.get_pos(k, k)] = 0
        perm_cols.elems[perm_cols.get_pos(j, k)] = 1
        perm_cols.elems[perm_cols.get_pos(k, j)] = 1
        
        return self * perm_cols
    
    def _get_row_deleter(self, j):
        identity = self.get_identity()
        
        row_start = identity.get_pos(j, 1)
        row_end = identity.get_pos(j, identity.c)
        
        new_elems = []
        for i, elem in enumerate(identity.elems):
            if row_start <= i <= row_end:
                continue
            new_elems.append(elem)

        del_rows = myarray(new_elems, self.r-1, self.r)
        return del_rows
    
    
    def del_row_algebra(self, j):
        del_rows = self._get_row_deleter(j)    
        return del_rows * self                
                        
    def _get_col_deleter(self, j):
        identity = self.get_identity(n = self.c)
        
        row_start = identity.get_pos(j, 1)
        row_end = identity.get_pos(j, identity.c)
        
        new_elems = []
        for i, elem in enumerate(identity.elems):
            if row_start <= i <= row_end:
                continue
            new_elems.append(elem)

        del_cols = myarray(new_elems, self.c, self.c-1, by_row = False)
        return del_cols
    
    def del_col_algebra(self, j):
        del_cols = self._get_col_deleter(j)
        return self * del_cols
                        

    def scale_row(self, j, x):
        """ Escala la fila j por el factor x, retornando una nueva matriz sin alterar la original. """
        new_elems = self.elems.copy() # Copy the elements list
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        for k in range(1, new_obj.c + 1):
            new_obj.elems[new_obj.get_pos(j, k)] *= x
        return new_obj

    def scale_col(self, k, y):
        """ Escala la columna k por el factor y, retornando una nueva matriz sin alterar la original. """
        new_elems = self.elems.copy() # Copy the elements list
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        for j in range(1, new_obj.r + 1):
            new_obj.elems[new_obj.get_pos(j, k)] *= y
        return new_obj
    
    def transpose(self):
        """ Devuelve la transposición de la matriz. """
        transposed_elems = []
        for k in range(1, self.c + 1):
            for j in range(1, self.r + 1):
                transposed_elems.append(self.elems[self.get_pos(j, k)])
        return myarray(transposed_elems, self.c, self.r, by_row = True)
    
    def flip_cols(self):
        """ Refleja la matriz especularmente a lo largo de sus columnas. """
        new_elems = self.elems.copy()  # Copy the elements list
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        for j in range(1, new_obj.r + 1):
            start = self.get_pos(j, 1)
            end = self.get_pos(j, self.c)
            new_obj.elems[start:end+1] = new_obj.elems[start:end+1][::-1]
        return new_obj

    def flip_rows(self):
        """ Refleja la matriz especularmente a lo largo de sus filas. """
        new_elems = self.elems.copy()  # Copy the elements list
        new_obj = myarray(new_elems, self.r, self.c, self.by_row)
        for k in range(1, new_obj.c + 1):
            for j in range(1, (new_obj.r + 1)):
                new_obj.elems[new_obj.get_pos(j, k)] = self.elems[self.get_pos(self.r - j + 1, k)]
            
        return new_obj
    
    def det(self):
        if self.r != self.c:
            raise ValueError("Determinante solo definido para matrices cuadradas.")
        if self.r == 1:
            return self.elems[0]
        result = 0
        for col in range(1, self.c + 1):
            arbitrary_row = 1
            submatrix = self.get_submatrix([i for i in range(1, self.r + 1) if i != arbitrary_row],
                                           [j for j in range(1, self.c + 1) if j != col])
            sign = (-1) ** (arbitrary_row + col)
            result += sign * self.elems[self.get_pos(arbitrary_row, col)] * submatrix.det()
        return result


    
    def __add__(self, B):
        """ Suma de dos matrices. """
        if isinstance(B, (int, float)):
            new_elems = [self.elems[i] + B for i in range(len(self.elems))]
        elif isinstance(B, myarray) and self.r == B.r and self.c == B.c:
            new_elems = [self.elems[i] + B.elems[i] for i in range(len(self.elems))]
        else:
            raise ValueError("Las dimensiones deben coincidir para la suma.")
        return myarray(new_elems, self.r, self.c, self.by_row)
    
    def __radd__(self,B):
        return self + B
    

    def __sub__(self, B):
        """ Resta de dos matrices. """
        if isinstance(B, (int, float)):
            new_elems = [self.elems[i] - B for i in range(len(self.elems))]
        elif isinstance(B, myarray) and self.r == B.r and self.c == B.c:
            new_elems = [self.elems[i] - B.elems[i] for i in range(len(self.elems))]
        else:
            raise ValueError("Las dimensiones deben coincidir para la resta.")
        return myarray(new_elems, self.r, self.c, self.by_row)
    
    def __rsub__(self,B):
        if isinstance(B, (int, float)):
            new_elems = [B - self.elems[i] for i in range(len(self.elems))]
        elif isinstance(B, myarray) and self.r == B.r and self.c == B.c:
            new_elems = [B.elems[i] - self.elems[i] for i in range(len(self.elems))]
        else:
            raise ValueError("Las dimensiones deben coincidir para la resta.")
        return myarray(new_elems, self.r, self.c, self.by_row)
    
    def __mul__(self, B):
        """ Producto a la derecha por otra matriz o escalar. """
        if isinstance(B, myarray):  # Matriz por matriz
            if self.c != B.r:
                raise ValueError("Incompatibilidad de dimensiones para el producto.")
            result = []
            for i in range(1, self.r + 1):
                for j in range(1, B.c + 1):
                    sum_prod = sum(self.get_elem(i, k) * B.get_elem(k, j) for k in range(1, self.c + 1))
                    result.append(sum_prod)
            return myarray(result, self.r, B.c, True)
        elif isinstance(B, (int, float)):  # Matriz por escalar
            new_elems = [x * B for x in self.elems]
            return myarray(new_elems, self.r, self.c, self.by_row)
    
    def __rmul__(self, B):
        return self * B
        
    def __pow__(self, n):
        """ Potencia de una matriz. """
        if isinstance(n, int):
            if n == 0:
                return self.get_identity()
            result = self
            for _ in range(1, n):
                result = result * self
            return result
        else:
            raise TypeError("Se debe elevar por un entero.")

    def get_identity(self, n = None):
        if not n:
            n = self.r
        identity = [1 if j == k else 0 for j in range(1, n+1) for k in range(1, n+1)]
        return myarray(identity, n, n, by_row = True)

