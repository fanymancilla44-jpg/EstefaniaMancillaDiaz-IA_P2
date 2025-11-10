# metodo quicksort
# en este programa ordenamos usando particionado con un pivote
# la idea es separar menores y mayores alrededor del pivote
# luego repetimos el proceso en cada lado
# es rapido en promedio
# mostramos pasos para ver como se mueve

def es_numero(t):
    return t.lstrip("-").isdigit()

def quick_num(a, l, r, desc):
    if l >= r:
        return
    i, j = l, r
    # aqui elegimos un pivote sencillo el elemento del medio
    p = a[(l + r) // 2]
    # aqui movemos i y j hasta cruzarse
    while i <= j:
        if not desc:
            while a[i] < p: i += 1
            while a[j] > p: j -= 1
        else:
            while a[i] > p: i += 1
            while a[j] < p: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            print("paso:", a)
            i += 1
            j -= 1
    # aqui aplicamos recursion a los dos lados
    if l < j: quick_num(a, l, j, desc)
    if i < r: quick_num(a, i, r, desc)

def quick_str(a, l, r, desc):
    if l >= r:
        return
    i, j = l, r
    p = a[(l + r) // 2]
    while i <= j:
        if not desc:
            while a[i] < p: i += 1
            while a[j] > p: j -= 1
        else:
            while a[i] > p: i += 1
            while a[j] < p: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            print("paso:", a)
            i += 1
            j -= 1
    if l < j: quick_str(a, l, j, desc)
    if i < r: quick_str(a, i, r, desc)

if __name__ == "__main__":
    linea = input("quicksort escribe numeros o palabras\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]

    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        quick_num(datos, 0, len(datos) - 1, desc)
    else:
        datos = toks[:]
        quick_str(datos, 0, len(datos) - 1, desc)

    print("ordenado:", datos)