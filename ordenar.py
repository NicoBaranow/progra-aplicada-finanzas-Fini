def ordenar(lista):
    if (lista[0][0]>lista[1][0]) or (lista[0][0]==lista[1][0] and lista[0][1]>lista[1][1]):
        lista[0],lista[1]=lista[1],lista[0]
    
    if len(lista)>2:
        new_list = lista[1::]
        lista= [lista[0]]+ordenar(new_list)
        new_list= lista[:-1:]
        lista= ordenar(new_list)+[lista[-1]]
    return lista


l1=[(0,1),(1,2),(0,2),(0,3),(1,1),(1,0),(1,1)]

print(ordenar(l1))
