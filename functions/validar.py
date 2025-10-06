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