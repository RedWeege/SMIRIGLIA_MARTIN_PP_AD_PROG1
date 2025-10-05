def mostrarLista(lista:list):
    '''
    Printea los valores de una lista de manera ordenada
    '''
    for i in range(len(lista)):
        print(lista[i])

def listsSort(lista:list, sort:str = "mM"):
    '''
    Funcion de ordenamiento de listas,
    si el 3er parametro es "mM", ordena de menor a mayor,
    si es "Mm", ordena de mayor a menor,
    si no es especificado o el 3er es invalido, ordena de mayor a menor
    modificada para ordenar listas paralelas
    '''
    if sort == "mM":
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    elif sort == "Mm":
        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if lista[i] < lista[j]:
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
    return lista
def avgList(lista:list):
    '''
    Saca el promedio de todos los numeros de una lista
    '''
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return (total / len(lista))