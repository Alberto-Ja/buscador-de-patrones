def buscar_apariciones(texto, patron):
    contar = 0
    posiciones = []

    longitud_texto = len(texto)
    longitud_patron = len(patron)

    for i in  range(longitud_texto - longitud_patron + 1):

        if texto[i:i+longitud_patron] == patron:
            contar += 1
            posiciones.append(i)

    if contar > 0:
        return (True, contar, posiciones)   
    else:
        return (False, 0, [])  

    texto = input()
    patron = input()

    result = buscar_apariciones(texto, posiciones)
    print(result)  
    
