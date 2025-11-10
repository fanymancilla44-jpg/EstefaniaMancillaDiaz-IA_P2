# metodo burbuja
# en este programa ordenamos datos usando intercambios de vecinos
# sirve para entender la idea basica de ordenar paso a paso
# primero leemos una linea con datos separados por espacio
# si todos son numeros ordenamos como enteros
# si hay palabras ordenamos alfabetico
# al final mostramos el resultado
# ademas preguntamos si quieres orden descendente

def es_numero(t):
    # aqui revisamos si el token representa un entero
    return t.lstrip("-").isdigit()

def bubble_num(a, desc=False):
    # aqui recorremos la lista varias veces
    # en cada pasada comparamos vecinos y los cambiamos si estan mal
    n = len(a)
    for i in range(n - 1):
        # aqui marcamos si hubo intercambio
        hubo_swap = False
        # aqui hacemos la comparacion de vecinos
        for j in range(n - 1 - i):
            # si es ascendente comparamos mayor que
            # si es descendente comparamos menor que
            if (not desc and a[j] > a[j + 1]) or (desc and a[j] < a[j + 1]):
                # aqui hacemos el intercambio
                a[j], a[j + 1] = a[j + 1], a[j]
                # aqui mostramos el avance
                print("paso:", a)
                hubo_swap = True
        # si no hubo cambios en la pasada ya esta ordenado
        if not hubo_swap:
            break

def bubble_str(a, desc=False):
    # misma idea pero comparando como texto
    n = len(a)
    for i in range(n - 1):
        hubo_swap = False
        for j in range(n - 1 - i):
            if (not desc and a[j] > a[j + 1]) or (desc and a[j] < a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                print("paso:", a)
                hubo_swap = True
        if not hubo_swap:
            break

if __name__ == "__main__":
    # aqui pedimos la lista de datos
    linea = input("burbuja escribe numeros o palabras separados por espacio\n").strip()
    # aqui pedimos el sentido del orden
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    # aqui separamos los tokens y limpiamos vacios
    toks = [t for t in linea.split() if t]

    # aqui decidimos si trabajamos como numeros o como texto
    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        bubble_num(datos, desc)
    else:
        datos = toks[:]
        bubble_str(datos, desc)

    # aqui mostramos el resultado final
    print("ordenado:", datos)