# metodo seleccion directa
# en este programa ordenamos colocando en cada posicion i el elemento correcto
# para eso buscamos el mas chico o el mas grande en el resto y lo movemos al frente
# primero leemos los datos y si es descendente
# si son numeros comparamos como enteros
# si hay palabras comparamos alfabetico
# mostramos pasos para ver el avance

def es_numero(t):
    return t.lstrip("-").isdigit()

def selection_num(a, desc=False):
    n = len(a)
    for i in range(n - 1):
        # aqui guardamos la posicion del candidato correcto
        pos = i
        # aqui recorremos lo que falta para hallar el minimo o el maximo
        for j in range(i + 1, n):
            if (not desc and a[j] < a[pos]) or (desc and a[j] > a[pos]):
                pos = j
        # aqui intercambiamos si encontramos uno mejor
        if pos != i:
            a[i], a[pos] = a[pos], a[i]
            print("paso:", a)

def selection_str(a, desc=False):
    n = len(a)
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if (not desc and a[j] < a[pos]) or (desc and a[j] > a[pos]):
                pos = j
        if pos != i:
            a[i], a[pos] = a[pos], a[i]
            print("paso:", a)

if __name__ == "__main__":
    linea = input("seleccion escribe numeros o palabras\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]

    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        selection_num(datos, desc)
    else:
        datos = toks[:]
        selection_str(datos, desc)

    #mostramos
    print("ordenado:", datos)