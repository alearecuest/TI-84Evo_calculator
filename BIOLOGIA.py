import math


def menu_hardy():
    print("\n--- HARDY-WEINBERG (p + q = 1) ---")
    print("Que dato tenes?")
    print("1: Frec genotipo recesivo (q^2)")
    print("2: Frec alelo dominante (p)")
    print("3: Individuos recesivos y Total N")
    modo = input("Opcion: ")

    N = 1.0
    if modo == "1":
        q2 = float(input("Ingresa q^2 (ej 0.04): "))
        q = math.sqrt(q2)
        p = 1.0 - q
        N = float(input("Poblacion total N (1 si no hay): "))
    elif modo == "2":
        p = float(input("Ingresa p (ej 0.7): "))
        q = 1.0 - p
        N = float(input("Poblacion total N (1 si no hay): "))
    else:
        rec = float(input("Cant. ind. recesivos (aa): "))
        N = float(input("Poblacion total N: "))
        q = math.sqrt(rec / N)
        p = 1.0 - q

    p2 = p**2
    pq2 = 2.0 * p * q
    q2 = q**2

    print("\n--- ALELOS ---")
    print("p (Dom) = {:.4f} | q (Rec) = {:.4f}".format(p, q))
    print("--- GENOTIPOS ---")
    print("AA (p^2) = {:.4f} (N = {:.1f})".format(p2, p2 * N))
    print("Aa (2pq) = {:.4f} (N = {:.1f})".format(pq2, pq2 * N))
    print("aa (q^2) = {:.4f} (N = {:.1f})".format(q2, q2 * N))


def menu_chi():
    print("\n--- CHI-CUADRADO GENETICA ---")
    k = int(input("Numero de clases fenotipicas: "))
    chi2 = 0.0
    for i in range(1, k + 1):
        print("-- Clase {} --".format(i))
        o = float(input("Observados (O): "))
        e = float(input("Esperados  (E): "))
        term = ((o - e) ** 2) / e
        chi2 += term
        print("(O-E)^2/E = {:.4f}".format(term))

    print("\n--- RESULTADOS ---")
    print("Chi^2 Total = {:.4f}".format(chi2))
    print("Grados libertad (gl) = {}".format(k - 1))
    print("Ref p=0.05 -> gl1:3.84 | gl2:5.99 | gl3:7.81")


def menu_neubauer():
    print("\n--- CAMARA DE NEUBAUER ---")
    c_tot = float(input("Total celulas contadas: "))
    cuad = float(input("Cuadrantes grandes contados: "))
    dil = float(input("Factor dilucion (ej 2 si 1:2): "))

    prom = c_tot / cuad
    conc_ml = prom * dil * 10000.0
    print("\n--- RESULTADOS ---")
    print("Promedio/cuadrante: {:.2f}".format(prom))
    print("Conc: {:.3e} cel/mL".format(conc_ml))


def menu_shannon():
    print("\n--- BIODIVERSIDAD SHANNON ---")
    s = int(input("Numero de especies (S): "))
    inds = []
    tot = 0.0
    for i in range(1, s + 1):
        n_i = float(input("Individuos especie {}: ".format(i)))
        inds.append(n_i)
        tot += n_i

    h_shannon = 0.0
    d_simpson = 0.0
    for n_i in inds:
        if n_i > 0:
            pi = n_i / tot
            h_shannon -= pi * math.log(pi)
            d_simpson += pi**2

    h_max = math.log(s)
    equit = h_shannon / h_max if h_max > 0 else 0
    print("\n--- RESULTADOS ---")
    print("Total N: {:.0f} | Riqueza S: {}".format(tot, s))
    print("Shannon H' (ln): {:.4f}".format(h_shannon))
    print("Equitatividad J': {:.4f}".format(equit))
    print("Simpson (1-D)  : {:.4f}".format(1.0 - d_simpson))


while True:
    print("\n=== SUITE BIOLOGIA ===")
    print("1: Equilibrio Hardy-Weinberg")
    print("2: Test Chi-Cuadrado (Cruzas)")
    print("3: Conteo Camara Neubauer")
    print("4: Diversidad Shannon y Simpson")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_hardy()
    elif op == "2":
        menu_chi()
    elif op == "3":
        menu_neubauer()
    elif op == "4":
        menu_shannon()
    elif op == "0":
        break
