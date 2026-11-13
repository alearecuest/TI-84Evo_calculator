import math

R_GAS = 8.31446  # J/(mol*K)
F_FARADAY = 96485.3  # C/mol


def menu_gibbs():
    print("\n--- BIOENERGETICA (GIBBS) ---")
    dg0 = float(input("dG0' estandar (kJ/mol): "))
    t_c = float(input("Temperatura (C, ej 25 o 37): "))
    q = float(input("Cociente Q [Prod]/[React]: "))

    T = t_c + 273.15
    rt = (R_GAS * T) / 1000.0  # en kJ/mol
    dg_real = dg0 + rt * math.log(q)
    keq = math.exp(-dg0 / rt)

    print("\n--- RESULTADOS ---")
    print("RT = {:.3f} kJ/mol".format(rt))
    print("dG real = {:.3f} kJ/mol".format(dg_real))
    print("Keq' = {:.4e}".format(keq))
    if dg_real < 0:
        print("Estado: EXERGONICA (Espontanea)")
    elif dg_real > 0:
        print("Estado: ENDERGONICA (No espont)")
    else:
        print("Estado: EN EQUILIBRIO")


def menu_nernst():
    print("\n--- POTENCIAL DE NERNST ---")
    z = float(input("Carga del ion z (ej +1, +2, -1): "))
    c_out = float(input("Conc Externa [Out] (mM): "))
    c_in = float(input("Conc Interna [In] (mM): "))
    t_c = float(input("Temperatura (C, ej 37): "))

    T = t_c + 273.15
    # E en milivoltios (mV)
    e_mv = ((R_GAS * T) / (z * F_FARADAY)) * math.log(c_out / c_in) * 1000.0
    print("\n--- RESULTADOS ---")
    print("Potencial E = {:.2f} mV".format(e_mv))


def menu_adn():
    print("\n--- PUREZA Y CONC ADN/ARN ---")
    print("1: dsDNA (x50) | 2: ARN (x40) | 3: ssDNA (x33)")
    tipo = input("Tipo de muestra: ")
    factor = 50.0
    if tipo == "2":
        factor = 40.0
    elif tipo == "3":
        factor = 33.0

    a260 = float(input("Absorbancia A260: "))
    a280 = float(input("Absorbancia A280: "))
    dil = float(input("Factor dilucion (ej 1 o 50): "))

    conc = a260 * factor * dil
    ratio = a260 / a280 if a280 != 0 else 0
    print("\n--- RESULTADOS ---")
    print("Conc: {:.2f} ug/mL (o ng/uL)".format(conc))
    print("Ratio 260/280: {:.2f}".format(ratio))


def menu_pcr():
    print("\n--- PRIMERS PCR (Tm y %GC) ---")
    a = int(input("Cantidad de A: "))
    t = int(input("Cantidad de T: "))
    g = int(input("Cantidad de G: "))
    c = int(input("Cantidad de C: "))

    n = a + t + g + c
    gc_pct = ((g + c) / n) * 100.0
    tm_wallace = 2 * (a + t) + 4 * (g + c)
    tm_largo = 64.9 + 41.0 * ((g + c - 16.4) / n)

    print("\n--- RESULTADOS ---")
    print("Largo total: {} nt".format(n))
    print("%GC: {:.1f}%".format(gc_pct))
    print("Tm (Wallace <14nt): {:.1f} C".format(tm_wallace))
    print("Tm (Est. >14nt)   : {:.1f} C".format(tm_largo))


while True:
    print("\n=== SUITE BIOQUIMICA ===")
    print("1: Energia Libre Gibbs y Keq")
    print("2: Potencial de Nernst (Iones)")
    print("3: Cuantificacion ADN/ARN (260/280)")
    print("4: Primers PCR (Tm y %GC)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_gibbs()
    elif op == "2":
        menu_nernst()
    elif op == "3":
        menu_adn()
    elif op == "4":
        menu_pcr()
    elif op == "0":
        break
