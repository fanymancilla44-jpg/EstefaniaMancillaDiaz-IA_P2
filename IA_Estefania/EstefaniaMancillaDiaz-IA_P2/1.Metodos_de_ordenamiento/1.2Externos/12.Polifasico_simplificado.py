#   ordenamiento externo polifasico simplificado
# que es
#   reparte runs de forma desigual y rota archivos por fases
# para que sirve
#   sirve para reducir archivos en cada fase sin que se queden vacios a mitad del proceso
#   esta version es educativa y simplificada
# como funciona
#   genero runs iniciales cortos
#   reparto mas runs en A que en B y dejo C vacio
#   mezclo emparejando runs hacia C
#   roto nombres para la siguiente fase y repito hasta quedar con un run

import os

def leer_lista(ruta):
    if not os.path.exists(ruta): return []
    with open(ruta, "r", encoding="utf-8") as f:
        return [int(t) for t in f.read().split()]

def escribir_lineas(ruta, lineas):
    with open(ruta, "w", encoding="utf-8") as f:
        for run in lineas:
            f.write(" ".join(map(str, run)) + "\n")

def runs_iniciales(datos, tam):
    # corto en trozos de tamano fijo y ordeno cada trozo
    runs = []
    for i in range(0, len(datos), tam):
        trozo = sorted(datos[i:i + tam])
        runs.append(trozo)
    return runs

def mezclar_run(a, b):
    # mezcla de dos listas ordenadas
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    while i < len(a): res.append(a[i]); i += 1
    while j < len(b): res.append(b[j]); j += 1
    return res

def polifasico(runs):
    # reparto desigual simple dos para A uno para B
    A = []
    B = []
    C = []
    toggle = 0
    for r in runs:
        if toggle < 2:
            A.append(r)
        else:
            B.append(r)
        toggle = 0 if toggle == 2 else toggle + 1

    # rotacion de fases
    while True:
        total = len(A) + len(B) + len(C)
        if total <= 1:
            break
        C = []
        i = 0
        j = 0
        # mezclo emparejando runs de A y B
        while i < len(A) or j < len(B):
            ra = A[i] if i < len(A) else []
            rb = B[j] if j < len(B) else []
            C.append(mezclar_run(ra, rb))
            i += 1
            j += 1
        print("fase polifasica produjo", len(C), "runs")
        # roto roles para la siguiente fase
        A, B = C, []
        C = []
    return A[0] if A else []

if __name__ == "__main__":
    datos = leer_lista("input.txt")
    if not datos:
        print("no hay datos")
    else:
        # genero runs cortos para ver la rotacion
        runs = runs_iniciales(datos, tam=4)
        escribir_lineas("runs_iniciales.txt", runs)
        resultado = polifasico(runs)
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, resultado)))
        print("listo polifasico simplificado en output.txt")