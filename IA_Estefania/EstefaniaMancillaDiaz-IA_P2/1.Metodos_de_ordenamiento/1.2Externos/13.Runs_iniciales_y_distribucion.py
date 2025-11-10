#   utilidad para generar runs iniciales y repartirlos alternado
# para que sirve
#   sirve para preparar los archivos de trabajo de un ordenamiento externo
#   cuando la memoria es pequena hay que crear runs que si caben y guardarlos en disco
# como funciona
#   leo el archivo en bloques
#   ordeno cada bloque en memoria
#   guardo cada bloque como run separado
#   despues reparto alternando estos runs entre A y B

import os

def leer_flotado(ruta):
    # leo enteros uno por uno del archivo
    with open(ruta, "r", encoding="utf-8") as f:
        for t in f.read().split():
            yield int(t)

def generar_runs(input_path, block_size):
    # creo runs ordenados leyendo por bloques
    it = leer_flotado(input_path)
    runs = []
    bloque = []
    num = 0
    for x in it:
        bloque.append(x)
        if len(bloque) == block_size:
            bloque.sort()
            num += 1
            ruta = f"run_{num}.txt"
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(" ".join(map(str, bloque)) + "\n")
            runs.append(ruta)
            bloque = []
    if bloque:
        bloque.sort()
        num += 1
        ruta = f"run_{num}.txt"
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(" ".join(map(str, bloque)) + "\n")
        runs.append(ruta)
    print("runs generados:", runs)
    return runs

def repartir_alternado(runs, fA, fB):
    # reparto los archivos run alternando uno a A y el siguiente a B
    with open(fA, "w", encoding="utf-8") as a, open(fB, "w", encoding="utf-8") as b:
        hacia_A = True
        for ruta in runs:
            with open(ruta, "r", encoding="utf-8") as r:
                for linea in r:
                    if hacia_A:
                        a.write(linea)
                    else:
                        b.write(linea)
            hacia_A = not hacia_A
    print("reparto alternado a", fA, "y", fB, "listo")

if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        print("no hay input.txt")
    else:
        # defino el tamano del bloque para que quepa en memoria
        block_size = 8
        runs = generar_runs("input.txt", block_size)
        repartir_alternado(runs, "fA.txt", "fB.txt")
        print("listo generacion y distribucion de runs iniciales")