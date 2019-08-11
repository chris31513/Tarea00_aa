def elementos_diferentes(arreglo):
    arreglo_ayuda = []

    for i in arreglo:
        if not i in arreglo_ayuda:
            arreglo_ayuda.append(i)

    return len(arreglo_ayuda)
