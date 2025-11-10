# metodo radix
# en este programa ordenamos por digitos usando conteo estable
# esta version acepta enteros que no sean negativos
# si hay negativos o palabras usa otro metodo como merge o quick
# la idea es ordenar por unidades luego decenas luego centenas hasta cubrir el maximo

def counting_por_exp(a, exp):
    # aqui contamos ocurrencias del digito en la posicion exp
    cnt = [0] * 10
    out = [0] * len(a)
    for x in a:
        d = (x // exp) % 10
        cnt[d] += 1
    # aqui acumulamos para convertir conteo en posiciones finales
    for i in range(1, 10):
        cnt[i] += cnt[i - 1]
    # aqui llenamos de atras hacia adelante para que sea estable
    for i in range(len(a) - 1, -1, -1):
        d = (a[i] // exp) % 10
        cnt[d] -= 1
        out[cnt[d]] = a[i]
    return out

if __name__ == "__main__":
    linea = input("radix escribe numeros enteros sin negativos\n").strip()
    desc = input("orden descendente s o n\n").strip().lower().startswith("s")
    toks = [t for t in linea.split() if t]
    datos = list(map(int, toks)) if toks else []

    if any(x < 0 for x in datos):
        print("este radix basico no acepta negativos usa merge o quick")
    else:
        m = max(datos) if datos else 0
        exp = 1
        # aqui repetimos por cada posicion de digito
        while m // exp > 0:
            datos = counting_por_exp(datos, exp)
            print("paso:", datos)
            exp *= 10
        if desc:
            datos.reverse()
        print("ordenado:", datos)