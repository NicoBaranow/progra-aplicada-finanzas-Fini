#%%
def es_palindromo(cadena):

    # Caso base: Si la cadena está vacía o tiene un solo carácter, es un palíndromo
    if len(cadena) <= 1:
        resultado = True
    else:
        # Comprobar si el primer y último carácter son iguales
        primer_letra = cadena[0]
        ultima_letra = cadena[-1]
        if primer_letra == ultima_letra:
            # Llamada recursiva eliminando el primer y último carácter
            letras_intermedias = cadena[1:-1]
            resultado = es_palindromo(letras_intermedias)
        else:
            # Si el primer y último carácter no son iguales, no es un palíndromo
            resultado = False

    # Devolver el resultado de la comprobación
    return resultado

es_palindromo('neuquen')


#%%
 
def quicksort(arr):
    
    if len(arr) <= 1:
        return arr    
    else:
        reference = arr[0]

        #left = []         
        #for x in arr[1:]:  
        #    if x < reference:  
        #        left.append(x)     
        
        # El loop de arriba se puede reescribir usando list_comprehension (más claro y eficiente)
        left = [x for x in arr[1:] if x < reference]
        right = [x for x in arr[1:] if x >= reference]
        left_side_sorted = quicksort(left)
        right_side_sorted = quicksort(right)
        return left_side_sorted + [reference] + right_side_sorted
 
# Example usage
arr = [1, 7, 4, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)

#%%



