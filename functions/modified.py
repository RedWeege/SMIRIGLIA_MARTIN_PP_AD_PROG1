def mostrarListasParalelas(producto:list, precio:list):
    '''
    Printea los valores de una lista de manera ordenada
    Modificado para mostrar 2 listas paralelas con el $ añadido
    al final de la segunda
    '''
    for i in range(len(producto)):
        print(f"{producto[i]} - {precio[i]}$")
def mostrarListaParalelasIndice(producto:list, precio:list, sel:int):
    '''
    Printea los valores de una lista de manera ordenada
    Modificado para mostrar 2 listas paralelas, con una siendo
    anidada, usando el 3er parametro como indice
    '''
    for i in range(len(producto)):
        print(f"{producto[i]} - {precio[i][sel]}$")
def paraListsSort(lista:list, listaNum:list, sort:str = "mM"):
    '''
    Funcion de ordenamiento de listas,
    si el 3er parametro es "mM", ordena de menor a mayor,
    si es "Mm", ordena de mayor a menor,
    si no es especificado o el 3er es invalido, ordena de mayor a menor
    modificada para ordenar listas paralelas sin modificar las listas originales
    '''
    listaImportada = [""] * len(lista)
    listaNumImportada = [""] * len(lista)
    for i in range(len(lista)):
        listaImportada[i] = lista[i]
        listaNumImportada[i] = listaNum[i]
    if sort == "mM":
        for i in range(len(listaNumImportada)-1):
            for j in range(i+1, len(listaNumImportada)):
                if listaNumImportada[i] > listaNumImportada[j]:
                    aux = listaNumImportada[i]
                    listaNumImportada[i] = listaNumImportada[j]
                    listaNumImportada[j] = aux
                    aux = listaImportada[i]
                    listaImportada[i] = listaImportada[j]
                    listaImportada[j] = aux
    elif sort == "Mm":
        for i in range(len(listaNumImportada)-1):
            for j in range(i+1, len(listaNumImportada)):
                if listaNumImportada[i] < listaNumImportada[j]:
                    aux = listaNumImportada[j]
                    listaNumImportada[j] = listaNumImportada[i]
                    listaNumImportada[i] = aux
                    aux = listaImportada[i]
                    listaImportada[i] = listaImportada[j]
                    listaImportada[j] = aux
    return listaImportada, listaNumImportada
def sortThroughLists(listaIndentada:list, index:int, sort:str="mM"):
    '''
    Funcion de ordenamiento de listas, modificada para encontrar el
    valor mas alto o mas bajo en un indice dentro de una serie de listas
    indentadas y retornarlo
    '''
    if sort == "mM":
        valorActual = listaIndentada[0][index]
        indiceRetorno = 0
        for i in range(len(listaIndentada)):
            if valorActual > listaIndentada[i][index]:
                valorActual = listaIndentada[i][index]
                indiceRetorno = i
    elif sort == "Mm":
        valorActual = listaIndentada[0][index]
        indiceRetorno = 0
        for i in range(len(listaIndentada)):
            if valorActual < listaIndentada[i][index]:
                valorActual = listaIndentada[i][index]
                indiceRetorno = i
    return indiceRetorno