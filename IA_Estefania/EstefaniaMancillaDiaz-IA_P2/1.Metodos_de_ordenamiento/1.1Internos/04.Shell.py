# metodo shell
# en este programa ordenamos usando insercion con saltos llamados gaps
# sirve para acelerar la insercion normal
# primero definimos un gap grande y luego lo reducimos a la mitad
# con cada gap aplicamos una especie de insercion
# al final queda como insercion normal con gap igual a uno

def es_numero(t):
    return t.lstrip("-").isdigit()

def shell_num(a, desc=False):
    n = len(a)
    gap = max(1, n // 2)
    while gap > 0:
        # aqui recorremos desde gap hasta el final
        for i in range(gap, n):
            # aqui guardamos el valor que vamos a acomodar
            x = a[i]
            j = i
            # aqui comparamos contra el elemento que esta a distancia gap
            while j >= gap and ((not desc and a[j - gap] > x) or (desc and a[j - gap] < x)):
                a[j] = a[j - gap]
                j -= gap
                print("paso:", a)
            a[j] = x
            print("paso:", a)
        # aqui reducimos el gap
        gap //= 2

def shell_str(a, desc=False):
    n = len(a)
    gap = max(1, n // 2)
    while gap > 0:
        for i in range(gap, n):
            x = a[i]
            j = i
            while j >= gap and ((not desc and a[j - gap] > x) or (desc and a[j - gap] < x)):
                a[j] = a[j - gap]
                j -= gap
                print("paso:", a)
            a[j] = x
            print("paso:", a)
        gap //= 2

if __name__ == "__main__":
    linea = input("shell escribe numeros o palabras\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]

    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        shell_num(datos, desc)
    else:
        datos = toks[:]
        shell_str(datos, desc)

    print("ordenado:", datos)