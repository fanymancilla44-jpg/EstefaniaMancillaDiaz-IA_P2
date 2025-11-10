# metodo tree sort
# en este programa metemos los datos en un arbol binario de busqueda
# luego hacemos un recorrido en orden para obtenerlos ordenados
# si quieres descendente solo invertimos el resultado
# si los datos ya vienen casi ordenados el arbol puede desbalancearse

class NodoI:
    # aqui definimos un nodo para enteros
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

class NodoS:
    # aqui definimos un nodo para cadenas
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def es_numero(t):
    return t.lstrip("-").isdigit()

def insI(n, v):
    # aqui insertamos un entero comparando menor que para ir a la izquierda
    if n is None:
        return NodoI(v)
    if v < n.v:
        n.l = insI(n.l, v)
    else:
        n.r = insI(n.r, v)
    return n

def inorderI(n, out):
    # aqui recorremos en orden izquierda nodo derecha
    if not n:
        return
    inorderI(n.l, out)
    out.append(n.v)
    inorderI(n.r, out)

def insS(n, v):
    # aqui insertamos una cadena segun orden alfabetico simple
    if n is None:
        return NodoS(v)
    if v < n.v:
        n.l = insS(n.l, v)
    else:
        n.r = insS(n.r, v)
    return n

def inorderS(n, out):
    if not n:
        return
    inorderS(n.l, out)
    out.append(n.v)
    inorderS(n.r, out)

if __name__ == "__main__":
    linea = input("tree sort escribe numeros o palabras\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]

    if all(es_numero(t) for t in toks):
        root = None
        for t in toks:
            root = insI(root, int(t))
        res = []
        inorderI(root, res)
    else:
        root = None
        for t in toks:
            root = insS(root, t)
        res = []
        inorderS(root, res)

    if desc:
        res.reverse()
    print("ordenado:", res)