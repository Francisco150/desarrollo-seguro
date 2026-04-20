

def cadena_mas_larga (lista_cadenas):

    if not lista_cadenas:
            return ""

    if not isinstance(lista_cadenas,list):
        raise TypeError("No se ha introducido una lista de cadenas.")
    
    if not all(isinstance(i,str) for i in lista_cadenas):
        raise ValueError ("La lista debe contener solo cadenas.")
    
    longitud_max = max(len(palabra) for palabra in lista_cadenas)

    lista_maxima = []

    for cadena in lista_cadenas:
        if len(cadena) == longitud_max:
             lista_maxima.append(cadena)

    lista_maxima.sort()
    
    return lista_maxima[0]


if __name__ == "__main__":
     
    lista=[]
    for i in range(5):
        lista.append(input("Introduce una palabra: "))

    try:
        
        print("La palabra mas larga es: ",cadena_mas_larga(lista))

    except (ValueError,TypeError) as e:
        print("Error: ",e)

    
