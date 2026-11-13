import math


def menu_buffer():
    print("\n--- HENDERSON-HASSELBALCH ---")
    pka = float(input("pKa (si tenes Ka pone 0): "))
    if pka == 0:
        ka = float(input("Ingresa Ka (ej 1.8e-5): "))
        pka = -math.log10(ka)

    print("1: Calc pH | 2: Calc [A-]/[HA]")
    modo = input("Opcion: ")
    if modo == "1":
        ca = float(input("Conc Acido [HA]: "))
        cb = float(input("Conc Base [A-]: "))
        ph = pka + math.log10(cb / ca)
        print("pKa = {:.3f}".format(pka))
        print("pH  = {:.3f}".format(ph))
        print("pOH = {:.3f}".format(14.0 - ph))
    else:
        ph = float(input("pH deseado: "))
        ratio = 10.0 ** (ph - pka)
        print("Relacion [A-]/[HA]: {:.4f}".format(ratio))
        print("% Base: {:.2f}%".format((ratio / (1.0 + ratio)) * 100.0))


def menu_michaelis():
    print("\n--- MICHAELIS-MENTEN ---")
    vmax = float(input("Vmax: "))
    km = float(input("Km: "))
    s = float(input("Conc Sustrato [S]: "))

    v = (vmax * s) / (km + s)
    sat = (v / vmax) * 100.0
    print("\n--- RESULTADOS ---")
    print("Velocidad v: {:.5e}".format(v))
    print("Saturacion: {:.2f}%".format(sat))
    print("-- Lineweaver-Burk --")
    print("1/[S]: {:.4e}".format(1.0 / s))
    print("1/v  : {:.4e}".format(1.0 / v))
    print("Pendiente (Km/Vmax): {:.4e}".format(km / vmax))


def menu_beer_dilucion():
    print("\n--- BEER-LAMBERT / DILUCION ---")
    print("1: Beer-Lambert (A = e*b*c)")
    print("2: Dilucion (C1*V1 = C2*V2)")
    m = input("Opcion: ")
    if m == "1":
        print("Deja en 0 la incognita:")
        A = float(input("Absorbancia A: "))
        e = float(input("Coef extincion (e): "))
        b = float(input("Paso optico b (cm): "))
        c = float(input("Concentracion c: "))
        if A == 0:
            A = e * b * c
            print("A = {:.4f}".format(A))
        elif c == 0:
            c = A / (e * b)
            print("c = {:.5e}".format(c))
        elif e == 0:
            e = A / (b * c)
            print("e = {:.4e}".format(e))
        T = (10.0 ** (-A)) * 100.0
        print("Transmitancia: {:.2f}%".format(T))
    else:
        c1 = float(input("C1 (Stock): "))
        c2 = float(input("C2 (Final): "))
        v2 = float(input("V2 (Vol final total): "))
        v1 = (c2 * v2) / c1
        print("Tomar V1 = {:.4f}".format(v1))
        print("Agregar solvente = {:.4f}".format(v2 - v1))


def menu_crecimiento():
    print("\n--- CRECIMIENTO CELULAR ---")
    n0 = float(input("Poblacion inicial N0: "))
    nt = float(input("Poblacion final Nt: "))
    t = float(input("Tiempo transcurrido t: "))

    gen = (math.log10(nt) - math.log10(n0)) / math.log10(2.0)
    mu = math.log(nt / n0) / t
    td = math.log(2.0) / mu
    print("\n--- RESULTADOS ---")
    print("Generaciones (n): {:.2f}".format(gen))
    print("Vel esp (mu): {:.4f} t^-1".format(mu))
    print("Tiempo dupl (td): {:.3f}".format(td))


while True:
    print("\n=== SUITE BIOTEC / QUIMICA ===")
    print("1: Buffers y pH")
    print("2: Cinetica Michaelis-Menten")
    print("3: Beer-Lambert y Diluciones")
    print("4: Crecimiento Microbiano")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_buffer()
    elif op == "2":
        menu_michaelis()
    elif op == "3":
        menu_beer_dilucion()
    elif op == "4":
        menu_crecimiento()
    elif op == "0":
        break
