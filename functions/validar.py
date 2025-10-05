def par(num1:int) -> bool:
    '''
    Verifica si el numero ingresado en el parametro es par, retorna como booleano
    '''
    if num1 % 2 == 0:
        pair = True
    else:
        pair = False
    return pair
def AskInRange(desde:int, hasta:int) -> int:
    '''
    Pide un numero entre los 2 parametros ingresados (inclusivo), y lo retorna cuando es valido
    '''
    num1 = "nun"
    while num1 == "nun" or num1 < desde or num1 > hasta:
        num1 = int(input(f"Ingrese un numero entre {desde} y {hasta} inclusivo: "))
        if num1 < desde or num1 > hasta:
            print("Error, numero invalido")
    return num1
def InRange(num:float, desde:int, hasta:int) -> bool:
    '''
    Verifica si el primer numero parametro ingresado cae entre el segundo y tercer parametro inclusive
    '''
    if num <= hasta and num >= desde:
        isinrange = True
    else:
        isinrange = False
    return isinrange
def inputInt() -> int:
    '''
    Pide un valor y solo lo retorna si es entre 1 y 9,
    evita roturas por ingreso invalido
    '''
    sel = -1
    while sel < 48 or sel > 57:
        sel = input()
        if len(sel) == 1:
            sel = ord(sel)
        else:
            sel = -1
            continue
    sel = int(chr(sel))
    return sel