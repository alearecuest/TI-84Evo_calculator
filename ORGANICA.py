import math


def menu_idh():
    print("\n--- IDH (INSATURACION) Y PM ---")
    c = int(input("Carbonos (C): "))
    h = int(input("Hidrogenos (H): "))
    n = int(input("Nitrogenos (N): "))
    o = int(input("Oxigenos (O): "))
    x = int(input("Halogenos (F,Cl,Br,I): "))

    # IDH = C - H/2 - X/2 + N/2 + 1
    idh = c - (h / 2.0) - (x / 2.0) + (n / 2.0) + 1.0
    pm = c * 12.011 + h * 1.008 + n * 14.007 + o * 15.999

    print("\n--- RESULTADOS ---")
    print("IDH (Anillos + enlaces pi) = {:.1f}".format(idh))
    if idh >= 4:
        print("Tip: IDH >= 4 sugiere anillo bencenico!")
    print("Masa Molar (sin X): {:.2f} g/mol".format(pm))
    if pm > 0 and x == 0:
        print(
            "%C: {:.2f}% | %H: {:.2f}%".format(
                (c * 12.011 / pm) * 100, (h * 1.008 / pm) * 100
            )
        )
        print(
            "%N: {:.2f}% | %O: {:.2f}%".format(
                (n * 14.007 / pm) * 100, (o * 15.999 / pm) * 100
            )
        )


def menu_empirica():
    print("\n--- FORMULA DESDE % ELEMENTAL ---")
    pc = float(input("% Carbono: "))
    ph = float(input("% Hidrogeno: "))
    pn = float(input("% Nitrogeno (0 si no hay): "))
    po = float(input("% Oxigeno (pone -1 para autocompletar): "))
    if po < 0:
        po = max(0.0, 100.0 - (pc + ph + pn))
        print("%O calculado = {:.2f}%".format(po))

    mc = pc / 12.011
    mh = ph / 1.008
    mn = pn / 14.007
    mo = po / 15.999
    vals = [v for v in [mc, mh, mn, mo] if v > 0.001]
    min_v = min(vals)

    print("\n--- RELACION MOLAR (EMPIRICA) ---")
    print("C : {:.2f}".format(mc / min_v))
    print("H : {:.2f}".format(mh / min_v))
    if mn > 0:
        print("N : {:.2f}".format(mn / min_v))
    if mo > 0:
        print("O : {:.2f}".format(mo / min_v))


def menu_polarimetria():
    print("\n--- QUIRALIDAD Y POLARIMETRIA ---")
    a_obs = float(input("Rotacion observada (grados): "))
    l_dm = float(input("Largo tubo L (en dm, ej 1.0): "))
    c_gml = float(input("Concentracion c (en g/mL): "))

    a_esp = a_obs / (l_dm * c_gml)
    print("Rotacion especifica [a]D = {:.2f}".format(a_esp))

    a_puro = float(input("[a]D del enantiomero puro (0 omitir): "))
    if a_puro != 0:
        ee = (abs(a_esp) / abs(a_puro)) * 100.0
        mayor = 50.0 + (ee / 2.0)
        menor = 50.0 - (ee / 2.0)
        print("Exceso Enantiomerico (ee): {:.2f}%".format(ee))
        print("Isomero Mayoritario: {:.2f}%".format(mayor))
        print("Isomero Minoritario: {:.2f}%".format(menor))


def menu_arrhenius():
    print("\n--- CINETICA DE ARRHENIUS ---")
    t1_c = float(input("Temp T1 (C): "))
    t2_c = float(input("Temp T2 (C): "))
    t1 = t1_c + 273.15
    t2 = t2_c + 273.15
    print("1: Calc k2/k1 dada Ea | 2: Calc Ea dadas k1 y k2")
    m = input("Opcion: ")
    if m == "1":
        ea_kj = float(input("Ea (kJ/mol): "))
        ratio = math.exp(((ea_kj * 1000.0) / 8.31446) * ((1.0 / t1) - (1.0 / t2)))
        print("Relacion de velocidades k2/k1 = {:.3f}x".format(ratio))
    else:
        k1 = float(input("Constante k1: "))
        k2 = float(input("Constante k2: "))
        ea_j = (8.31446 * math.log(k2 / k1)) / ((1.0 / t1) - (1.0 / t2))
        print("Energia Activacion Ea = {:.2f} kJ/mol".format(ea_j / 1000.0))


while True:
    print("\n=== SUITE QUIMICA ORGANICA ===")
    print("1: IDH (Insaturacion) y % Masa")
    print("2: Formula Empirica desde %")
    print("3: Polarimetria y Enantiomeros (%ee)")
    print("4: Arrhenius (Ea y Temperatura)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_idh()
    elif op == "2":
        menu_empirica()
    elif op == "3":
        menu_polarimetria()
    elif op == "4":
        menu_arrhenius()
    elif op == "0":
        break
