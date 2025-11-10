#   ordenamiento externo por mezcla balanceada de k vias
# que es
#   mezcla varios runs a la vez usando una cola minima
# para que sirve
#   sirve cuando hay muchos runs y quiero mezclar mas de dos en paralelo
#   reduce el numero de pasadas sobre disco
# como funciona
#   genero runs iniciales ordenando bloques que si caben en memoria
#   abro un iterador por run
#   meto el primer elemento de cada run en una cola minima
#   saco siempre el menor y meto el siguiente del mismo run
#   escribo todo en output

import os
import heapq

def leer_flotado(ruta):
    # leo tokens del archivo uno por uno
    with open(ruta, "r", encoding="utf-8") as f:
        for pieza in f.read().split():
            yield int(pieza)

def generar_runs_iniciales(input_path, block_size):
    # genero runs ordenando bloques pequenos
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
    print("runs iniciales:", runs)
    return runs

def abrir_run_iter(ruta):
    # devuelvo numeros de un run uno por uno
    for linea in open(ruta, "r", encoding="utf-8"):
        for t in linea.split():
            yield int(t)

def mezcla_k_vias(runs, salida):
    # preparo un iterador por run
    iters = [abrir_run_iter(r) for r in runs]
    # cola minima con tuplas valor y indice del run
    heap = []
    for i, it in enumerate(iters):
        try:
            val = next(it)
            heapq.heappush(heap, (val, i))
        except StopIteration:
            pass
    # abro salida y saco minimos hasta terminar
    with open(salida, "w", encoding="utf-8") as out:
        buffer = []
        while heap:
            val, idx = heapq.heappop(heap)
            buffer.append(str(val))
            # si el buffer crece lo escribo para no usar mucha memoria
            if len(buffer) >= 2000:
                out.write(" ".join(buffer) + " ")
                buffer = []
            # tomo el siguiente del mismo run y lo meto a la cola
            try:
                nxt = next(iters[idx])
                heapq.heappush(heap, (nxt, idx))
            except StopIteration:
                pass
        if buffer:
            out.write(" ".join(buffer))
    print("mezcla k vias terminada")

if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        print("no hay input.txt")
    else:
        # defino un tamano de bloque pequeno para simular poca memoria
        block_size = 10
        runs = generar_runs_iniciales("input.txt", block_size)
        if not runs:
            print("no se generaron runs")
        else:
            mezcla_k_vias(runs, "output.txt")
            print("listo mezcla balanceada k vias en output.txt")