# metodo merge
# en este programa aplicamos divide y venceras
# primero partimos la lista en dos mitades hasta llegar a trozos de uno
# luego mezclamos dos mitades ya ordenadas tomando siempre el correcto segun asc o desc
# imprimimos pasos para ver como se va uniendo

def es_numero(t):
    return t.lstrip("-").isdigit()

def merge_num(a, l, m, r, desc):
    # aqui mezclamos el segmento izquierdo y el derecho ya ordenados
    i = l
    j = m + 1
    aux = []
    while i <= m and j <= r:
        if (not desc and a[i] <= a[j]) or (desc and a[i] >= a[j]):
            aux.append(a[i]); i += 1
        else:
            aux.append(a[j]); j += 1
    while i <= m:
        aux.append(a[i]); i += 1
    while j <= r:
        aux.append(a[j]); j += 1
    a[l:r+1] = aux
    print("paso:", a)

def ms_num(a, l, r, desc):
    if l >= r:
        return
    m = (l + r) // 2
    ms_num(a, l, m, desc)
    ms_num(a, m + 1, r, desc)
    merge_num(a, l, m, r, desc)

def merge_str(a, l, m, r, desc):
    i = l
    j = m + 1
    aux = []
    while i <= m and j <= r:
        if (not desc and a[i] <= a[j]) or (desc and a[i] >= a[j]):
            aux.append(a[i]); i += 1
        else:
            aux.append(a[j]); j += 1
    while i <= m:
        aux.append(a[i]); i += 1
    while j <= r:
        aux.append(a[j]); j += 1
    a[l:r+1] = aux
    print("paso:", a)

def ms_str(a, l, r, desc):
    if l >= r:
        return
    m = (l + r) // 2
    ms_str(a, l, m, desc)
    ms_str(a, m + 1, r, desc)
    merge_str(a, l, m, r, desc)

if __name__ == "__main__":
    linea = input("merge escribe numeros o palabras\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]

    if all(es_numero(t) for t in toks):
        datos = list(map(int, toks))
        ms_num(datos, 0, len(datos) - 1, desc)
    else:
        datos = toks[:]
        ms_str(datos, 0, len(datos) - 1, desc)

    print("ordenado:", datos)