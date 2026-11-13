import math

R_GAS = 8.31446
F_FAR = 96485.3
C_LUZ = 299792458.0


def menu_ghk():
    print("\n--- ECUACION GOLDMAN (GHK) ---")
    t_c = float(input("Temp (C, ej 37): "))
    pk = float(input("Perm rel P_K (ej 1.0): "))
    pna = float(input("Perm rel P_Na (ej 0.04): "))
    pcl = float(input("Perm rel P_Cl (ej 0.45): "))

    k_o = float(input("[K+] ext (mM): "))
    k_i = float(input("[K+] int (mM): "))
    na_o = float(input("[Na+] ext (mM): "))
    na_i = float(input("[Na+] int (mM): "))
    cl_o = float(input("[Cl-] ext (mM): "))
    cl_i = float(input("[Cl-] int (mM): "))

    num = pk * k_o + pna * na_o + pcl * cl_i
    den = pk * k_i + pna * na_i + pcl * cl_o
    vm = ((R_GAS * (t_c + 273.15)) / F_FAR) * math.log(num / den) * 1000.0
    print("\nPotencial Membrana Vm = {:.2f} mV".format(vm))


def menu_optica_fis():
    print("\n--- OPTICA GEOM Y FISICA ---")
    print("1: Lentes Delgadas (1/f = 1/s + 1/s')")
    print("2: Ley de Snell, Critico y Brewster")
    m = input("Opcion: ")
    if m == "1":
        f = float(input("Focal f (cm, - si divergente): "))
        s = float(input("Dist objeto s (cm): "))
        sp = 1.0 / ((1.0 / f) - (1.0 / s))
        mag = -sp / s
        pot = 100.0 / f
        print("Dist imagen s' = {:.3f} cm".format(sp))
        print("Aumento M = {:.3f}x".format(mag))
        print("Potencia = {:.2f} dioptrias".format(pot))
    else:
        n1 = float(input("Indice n1 (incidente): "))
        n2 = float(input("Indice n2 (refractado): "))
        th1 = float(input("Angulo incidencia (grados): "))

        brew = math.degrees(math.atan(n2 / n1))
        print("Angulo Brewster = {:.2f} deg".format(brew))
        if n1 > n2:
            crit = math.degrees(math.asin(n2 / n1))
            print("Angulo Critico (TIR) = {:.2f} deg".format(crit))
        sin_th2 = (n1 / n2) * math.sin(math.radians(th1))
        if abs(sin_th2) <= 1.0:
            th2 = math.degrees(math.asin(sin_th2))
            print("Angulo refraccion = {:.2f} deg".format(th2))
        else:
            print("REFLEXION TOTAL INTERNA!")


def menu_mecanica_rel():
    print("\n--- MECANICA Y RELATIVIDAD ---")
    print("1: Choque Elastico 1D (v1f, v2f)")
    print("2: Relatividad Especial (Lorentz)")
    m = input("Opcion: ")
    if m == "1":
        m1 = float(input("Masa m1: "))
        v1 = float(input("Vel inicial v1: "))
        m2 = float(input("Masa m2: "))
        v2 = float(input("Vel inicial v2: "))
        v1f = ((m1 - m2) / (m1 + m2)) * v1 + ((2.0 * m2) / (m1 + m2)) * v2
        v2f = ((2.0 * m1) / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
        v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)
        print("v1 final = {:.4f}".format(v1f))
        print("v2 final = {:.4f}".format(v2f))
        print("v_CM (Inelastico) = {:.4f}".format(v_cm))
    else:
        beta = float(input("Velocidad en fraccion de c (ej 0.8): "))
        gamma = 1.0 / math.sqrt(1.0 - beta**2)
        print("Factor Gamma = {:.5f}".format(gamma))
        print("v = {:.4e} m/s".format(beta * C_LUZ))
        print("Contrac. Long (L/L0) = {:.4f}".format(1.0 / gamma))


while True:
    print("\n=== BIOFISICA, OPTICA Y MEC ===")
    print("1: Biofisica Membrana (Goldman)")
    print("2: Lentes, Snell y Brewster")
    print("3: Choques y Relatividad")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_ghk()
    elif op == "2":
        menu_optica_fis()
    elif op == "3":
        menu_mecanica_rel()
    elif op == "0":
        break
