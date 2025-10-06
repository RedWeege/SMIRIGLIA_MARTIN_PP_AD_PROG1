from functions.listas import *
from functions.modified import *
from functions.validar import *

# Productos en orden
productos = ["Leche", "Fideos", "Polenta", "Jugo de Manzana"]

# Matriz de precios, cada columna correspondiente a una tienda
# columna 0 = tienda 1
# columna 1 = tienda 2
# columna 2 = tienda 3
precios = [[1300, 1002, 1700], # Leche
           [800,   534, 1000], # Fideos
           [500,   800, 1300], # Polenta
           [850,   600,  900]] # Jugo de Manzana
avgPrices = [0] * 4

sel = -1
while sel != "4":
    sel = input('''[1] - Listar productos de una tienda
[2] - Listar los productos mas caros y mas baratos de cada tienda
[3] - Mostrar productos por precio promedio
[4] - Salir\n''')
    if sel == "1":
        print('''Listar de:
[1] - Tienda 1
[2] - Tienda 2
[3] - Tienda 3''')
        sel = -1
        while sel != 1 and sel != 2 and sel != 3:
            sel = inputInt()
        mostrarListaParalelasIndice(productos, precios, sel-1)
    elif sel == "2":
        for i in range(len(precios)-1):
            productoCaro = sortThroughLists(precios, i, "Mm")
            productoBarato = sortThroughLists(precios, i, "mM")
            print(f'''Tienda {i + 1} | producto mas caro - {productos[productoCaro]} ({precios[productoCaro][i]}$)
Tienda {i+1} | producto mas barato - {productos[productoBarato]} ({precios[productoBarato][i]}$)''')
    elif sel == "3":
        for i in range(len(precios)):
            avgPrices[i] = avgList(precios[i]) # type: ignore
        display = paraListsSort(productos, avgPrices)
        mostrarListasParalelas(display[0], display[1])