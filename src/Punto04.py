def cuenta_renglones(mxn):
    grupo_de_1s = []
    grupos = []
    
    for i in range(0,len(mxn)):
        
        for j in range(0,len(mxn[i])):
            
            if mxn[i][j] == 1:
                grupo_de_1s.append((i,j))
            else:
                if j > 0 and len(grupo_de_1s) > 0:
                    grupos.append(grupo_de_1s)
                    grupo_de_1s = []
                    
        if len(grupo_de_1s) > 0:
            grupos.append(grupo_de_1s)
            grupo_de_1s = []
            
    return cuenta_adyacencias(grupos)

def cuenta_adyacencias(grupos):
    if len(grupos) <= 0:
        return 0
    else:
        j = 1
        adyacencias_hechas = []
        pre_grupo_ayuda = []
        pre_grupo = []
        grupos_completos = []
        
        for grupo in grupos:
            for cord in grupo:
                posible_adyacencia = busca_adyacencias(cord, grupos[j:])
                
                if posible_adyacencia != None:
                    pre_grupo.append(cord)
                    pre_grupo.append(posible_adyacencia)
                    adyacencias_hechas.append(posible_adyacencia)

                else:
                    pre_grupo.append(busca_adyacencias(cord, pre_grupo_ayuda))
                    pre_grupo.append(cord)
                    pre_grupo.remove(None)
                
            if len(adyacencias_hechas) > 0:
                pre_grupo_ayuda.append(adyacencias_hechas)
                adyacencias_hechas = []
                
            if len(pre_grupo) > 0:
                grupos_completos.append(pre_grupo)
                pre_grupo = []

            j += 1

        return mezcla_listas(grupos_completos)

def busca_adyacencias(cord, grupos):
    for grupo in grupos:
        for cords in grupo:
            if (cords[0] == cord[0] + 1 and cords[1] == cord[1]) or (cords[0] == cord[0] - 1 and cords[1] == cord[1]) or (cords[1] == cord[1] + 1 and cords[0] == cord[0]) or (cords[1] == cord[1] - 1 and cords[0] == cord[0]):
                return grupo.pop(grupo.index(cords))

def mezcla_listas(lista):
    j = 1
    for sublista in lista:
        for tupla in sublista:
            tupla_cord = indice(tupla, lista[j:], factor_de_conteo = j)
            if  tupla_cord != (-1,-1):
                lista.pop(tupla_cord[0])
                

        j += 1
        
    return len(lista)
            
def indice(cord, lista, factor_de_conteo):
    for sublista in lista:
        if cord in sublista:
            return (lista.index(sublista) + factor_de_conteo,sublista.index(cord))
        else:
            continue
        
    return (-1,-1)
    
if __name__ == '__main__':
    print(cuenta_renglones([(1,1,0,1,0,0,1,1),
                            (1,1,0,1,0,0,0,0)]))
