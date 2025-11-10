# metodo mezcla directa
# que es
#   ordenamiento externo por mezcla directa
#   trabaja con runs de tamano fijo que se van duplicando en cada fase
# para que sirve
#   sirve cuando la lista no cabe en memoria
#   usamos archivos auxiliares para mezclar partes ordenadas
# como funciona
#   parto la lista en runs de tamano 1 luego 2 luego 4 y asi
#   alterno esos runs entre A y B
#   mezclo run contra run hacia un archivo de salida
#   repito hasta que quede un solo run ordenado

import os

def leer_lista(ruta):
    # leo tokens del archivo y los convierto a enteros
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read().split()
    return [int(t) for t in texto]

def escribir_lista(ruta, datos):
    # escribo la lista final separada por espacios
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(" ".join(str(x) for x in datos))

def partir_en_runs(datos, run_size, fA, fB):
    # abro A y B para escribir runs alternados
    with open(fA, "w", encoding="utf-8") as a, open(fB, "w", encoding="utf-8") as b:
        hacia_A = True
        # recorro la lista en bloques del tamano run_size
        for i in range(0, len(datos), run_size):
            run = datos[i:i + run_size]
            destino = a if hacia_A else b
            destino.write(" ".join(map(str, run)) + "\n")
            hacia_A = not hacia_A
    print("parti runs de tamano", run_size)

def mezclar_lineas(l1, l2):
    # convierto lineas a listas de enteros
    r1 = [] if not l1.strip() else list(map(int, l1.split()))
    r2 = [] if not l2.strip() else list(map(int, l2.split()))
    # preparo indices y resultado
    i = 0
    j = 0
    res = []
    # mezclo tomando el menor disponible
    while i < len(r1) and j < len(r2):
        if r1[i] <= r2[j]:
            res.append(r1[i]); i += 1
        else:
            res.append(r2[j]); j += 1
    # copio lo que falte
    while i < len(r1): res.append(r1[i]); i += 1
    while j < len(r2): res.append(r2[j]); j += 1
    return res

def mezclar_archivos(fA, fB, fOut):
    # abro A B y salida y mezclo run por run
    with open(fA, "r", encoding="utf-8") as a, open(fB, "r", encoding="utf-8") as b, open(fOut, "w", encoding="utf-8") as o:
        A = a.readlines()
        B = b.readlines()
        i = 0
        j = 0
        while i < len(A) or j < len(B):
            l1 = A[i] if i < len(A) else ""
            l2 = B[j] if j < len(B) else ""
            mezcla = mezclar_lineas(l1, l2)
            o.write(" ".join(map(str, mezcla)) + "\n")
            i += 1
            j += 1
    print("mezcle una fase hacia", fOut)

def aplanar_fout(fOut):
    # convierto el archivo de salida en una lista plana
    res = []
    with open(fOut, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                res.extend(map(int, linea.split()))
    return res

if __name__ == "__main__":
    # leo datos
    datos = leer_lista("input.txt")
    if not datos:
        print("no hay datos")
    else:
        # arranco con run de 1
        run = 1
        while run < len(datos):
            partir_en_runs(datos, run, "fA.txt", "fB.txt")
            mezclar_archivos("fA.txt", "fB.txt", "fOut.txt")
            datos = aplanar_fout("fOut.txt")
            print("despues de run", run, "=>", datos)
            run *= 2
        escribir_lista("output.txt", datos)
        print("listo mezcla directa en output.txt")