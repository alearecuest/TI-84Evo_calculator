import math

R_J = 8.31446

def menu_vanthoff():
    print("\n--- ECUACION DE VAN 'T HOFF ---")
    t1 = float(input("Temp T1 (C): ")) + 273.15
    t2 = float(input("Temp T2 (C): ")) + 273.15
    k1 = float(input("Constante equilibrio K1: "))
    print("1: Calc K2 dado dH0 | 2: Calc dH0 y dS0 dada K2")
    op = input("Opcion: ")
    
    if op == "1":
        dh_kj = float(input("dH0 estandar (kJ/mol): "))
        ln_ratio = ((-dh_kj * 1000.0) / R_J) * ((1.0/t2) - (1.0/t1))
        k2 = k1 * math.exp(ln_ratio)
        print("\nK2 a T2 = {:.5e}".format(k2))
    else:
        k2 = float(input("Constante equilibrio K2: "))
        dh_j = (-R_J * math.log(k2 / k1)) / ((1.0/t2) - (1.0/t1))
        dg1_j = -R_J * t1 * math.log(k1)
        ds_j = (dh_j - dg1_j) / t1
        print("\n--- RESULTADOS ---")
        print("dH0 = {:.3f} kJ/mol".format(dh_j / 1000.0))
        print("dS0 = {:.3f} J/(mol*K)".format(ds_j))
        print("dG0(T1) = {:.3f} kJ/mol".format(dg1_j / 1000.0))

def menu_pi_amino():
    print("\n--- PUNTO ISOELECTRICO (pI) ---")
    pka1 = float(input("pKa1 (alfa-COOH, ej ~2.1): "))
    pka2 = float(input("pKa2 (alfa-NH3+, ej ~9.5): "))
    pkar = float(input("pKaR cadena lateral (0 si neutro): "))
    
    if pkar == 0:
        pi = (pka1 + pka2) / 2.0
    else:
        tipo = input("Cadena lateral: 1:Acida (Asp/Glu) | 2:Basica (Lys/Arg/His): ")
        if tipo == "1":
            pi = (pka1 + pkar) / 2.0
        else:
            pi = (pka2 + pkar) / 2.0
            
    print("\nPunto Isoelectrico pI = {:.2f}".format(pi))
    ph_medio = float(input("pH del buffer de trabajo: "))
    if ph_medio < pi:
        print("Carga neta: POSITIVA (+) -> Migra al Catodo (-)")
    elif ph_medio > pi:
        print("Carga neta: NEGATIVA (-) -> Migra al Anodo (+)")
    else:
        print("Carga neta: CERO (Zwitterion, no migra)")

def menu_fuerza_ionica():
    print("\n--- FUERZA IONICA Y DEBYE-HUCKEL ---")
    n = int(input("Cantidad de especies ionicas: "))
    suma = 0.0
    for j in range(1, n + 1):
        c = float(input("Conc ion {} (M): ".format(j)))
        z = float(input("Carga ion {} (ej 1, 2, -1): ".format(j)))
        suma += c * (z ** 2)
        
    mu = 0.5 * suma
    print("\nFuerza Ionica (I) = {:.4f} M".format(mu))
    z_eval = float(input("Carga z de ion para coef gamma: "))
    # Ley limite de Debye-Huckel en agua a 25 C (A = 0.509)
    log_g = (-0.509 * (z_eval ** 2) * math.sqrt(mu)) / (1.0 + math.sqrt(mu))
    gamma = 10.0 ** log_g
    print("Coeficiente actividad gamma = {:.4f}".format(gamma))

while True:
    print("\n=== TERMODINAMICA Y SOLUCIONES ===")
    print("1: Ecuacion de Van 't Hoff (Keq y T)")
    print("2: Punto Isoelectrico (pI) y Electroforesis")
    print("3: Fuerza Ionica y Coef. Actividad")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_vanthoff()
    elif op == "2":
        menu_pi_amino()
    elif op == "3":
        menu_fuerza_ionica()
    elif op == "0":
        break
