#   ordenamiento externo por mezcla natural
# que es
#   usa runs que ya vienen crecientes en los datos
# para que sirve
#   sirve cuando los datos ya tienen pedazos en orden
#   reduce el numero de fases porque aprovecha lo que ya esta ordenado
# como funciona
#   detecto runs naturales en la lista
#   los alterno entre A y B
#   mezclo run contra run hacia salida
#   repito hasta que toda la lista sea un solo run

import os

def leer_lista(ruta):
    # leo archivo y regreso enteros
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read().split()
    return [int(t) for t in texto]

def escribir_lista(ruta, datos):
    # escribo la lista final
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(" ".join(str(x) for x in datos))

def detectar_runs_naturales(datos):
    # recorro y corto cuando la secuencia deja de crecer
    runs = []
    actual = []
    for i, x in enumerate(datos):
        if i == 0 or x >= datos[i - 1]:
            actual.append(x)
        else:
            runs.append(actual)
            actual = [x]
    if actual:
        runs.append(actual)
    return runs

def distribuir_alternado(runs, fA, fB):
    # escribo runs alternados en A y B
    with open(fA, "w", encoding="utf-8") as a, open(fB, "w", encoding="utf-8") as b:
        hacia_A = True
        for run in runs:
            destino = a if hacia_A else b
            destino.write(" ".join(map(str, run)) + "\n")
            hacia_A = not hacia_A
    print("reparti runs naturales en A y B")

def mezclar_lineas(l1, l2):
    # mezcla de dos runs en memoria
    r1 = [] if not l1.strip() else list(map(int, l1.split()))
    r2 = [] if not l2.strip() else list(map(int, l2.split()))
    i = 0
    j = 0
    res = []
    while i < len(r1) and j < len(r2):
        if r1[i] <= r2[j]:
            res.append(r1[i]); i += 1
        else:
            res.append(r2[j]); j += 1
    while i < len(r1): res.append(r1[i]); i += 1
    while j < len(r2): res.append(r2[j]); j += 1
    return res

def mezclar_AB_a_out(fA, fB, fOut):
    # leo A y B por lineas y mezclo por pares
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
    print("mezcle una fase natural")

def aplanar_fout(fOut):
    # paso salida a una sola lista
    res = []
    with open(fOut, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                res.extend(map(int, linea.split()))
    return res

def es_un_solo_run(datos):
    # checo si ya esta todo creciente
    for i in range(1, len(datos)):
        if datos[i] < datos[i - 1]:
            return False
    return True

if __name__ == "__main__":
    # leo
    datos = leer_lista("input.txt")
    if not datos:
        print("no hay datos")
    else:
        # repito hasta que quede un solo run
        while not es_un_solo_run(datos):
            runs = detectar_runs_naturales(datos)
            distribuir_alternado(runs, "fA.txt", "fB.txt")
            mezclar_AB_a_out("fA.txt", "fB.txt", "fOut.txt")
            datos = aplanar_fout("fOut.txt")
            print("paso natural =>", datos)
        escribir_lista("output.txt", datos)
        print("listo mezcla natural en output.txt")