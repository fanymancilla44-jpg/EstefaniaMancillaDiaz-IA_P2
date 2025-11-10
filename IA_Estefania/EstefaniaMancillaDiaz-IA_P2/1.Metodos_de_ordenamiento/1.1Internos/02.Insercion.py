# metodo de insercion
# en este programa ordenamos metiendo cada dato en su lugar correcto
# sirve cuando la lista es pequena o ya casi esta ordenada
# primero leemos los datos y el sentido del orden
# luego vamos dejando a la izquierda la parte ya ordenada
# mostramos pasos para ver como avanza

def es_numero(t):
    # aqui revisamos si el token es un entero valido
    return t.lstrip("-").isdigit()

def insertion_num(a, desc=False):
    # aqui recorremos desde la segunda posicion
    for i in range(1, len(a)):
        # aqui guardamos el valor que queremos acomodar
        x = a[i]
        # aqui tomamos el indice anterior
        j = i - 1
        # mientras el de la izquierda este mal ubicado lo corremos a la derecha
        while j >= 0 and ((not desc and a[j] > x) or (desc and a[j] < x)):
            # aqui movemos el mayor hacia la derecha
            a[j + 1] = a[j]
            j -= 1
            # aqui mostramos el estado despues de mover
            print("paso:", a)
        # aqui colocamos a x en el hueco que quedo
        a[j + 1] = x
        # aqui mostramos como va quedando
        print("paso:", a)

def insertion_str(a, desc=False):
    # misma logica pero comparando como texto
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and ((not desc and a[j] > x) or (desc and a[j] < x)):
            a[j + 1] = a[j]
            j -= 1
            print("paso:", a)
        a[j + 1] = x
        print("paso:", a)

if __name__ == "__main__":
    # aqui pedimos los datos
    linea = input("insercion escribe numeros o palabras\n").strip()
    # aqui definimos si es descendente
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    # aqui separamos tokens
    toks = [t for t in linea.split() if t]

    # aqui decidimos el modo de trabajo
    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        insertion_num(datos, desc)
    else:
        datos = toks[:]
        insertion_str(datos, desc)

    #aqui mostramos el orden final
    print("ordenado:", datos)