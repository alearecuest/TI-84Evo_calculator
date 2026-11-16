import math

def menu_cromatografia():
    print("\n--- CROMATOGRAFIA (UNID. 16 UDELAR) ---")
    tm = float(input("Tiempo muerto tM (min): "))
    tr1 = float(input("Tiempo retencion pico 1 tR1: "))
    w1 = float(input("Ancho base pico 1 w1 (misma u.): "))
    L = float(input("Largo columna L (cm): "))
    
    k1 = (tr1 - tm) / tm
    n1 = 16.0 * ((tr1 / w1) ** 2)
    h_plato = L / n1 if n1 > 0 else 0
    
    print("\n--- PICO 1 ---")
    print("Factor capacidad k'1 = {:.3f}".format(k1))
    print("Platos teoricos N1   = {:.1f}".format(n1))
    print("Altura plato H (HETP)= {:.5f} cm".format(h_plato))
    
    tr2 = float(input("\ntR2 segundo pico (0 si solo hay 1): "))
    if tr2 > 0:
        w2 = float(input("Ancho base pico 2 w2: "))
        k2 = (tr2 - tm) / tm
        alfa = k2 / k1 if k1 > 0 else 0
        rs = (2.0 * abs(tr2 - tr1)) / (w1 + w2)
        print("--- SEPARACION PICOS 1 Y 2 ---")
        print("k'2 = {:.3f} | Selectividad alfa = {:.3f}".format(k2, alfa))
        print("Resolucion Rs = {:.3f}".format(rs))
        if rs >= 1.5:
            print("Separacion: COMPLETA (Linea base Rs>=1.5)")
        else:
            print("Separacion: SOLAPADA (Rs<1.5)")

def menu_kps():
    print("\n--- PRODUCTO DE SOLUBILIDAD (Kps) ---")
    print("Sal A_x B_y <-> x A + y B")
    x = int(input("Coef estequiometrico x (cation): "))
    y = int(input("Coef estequiometrico y (anion): "))
    kps = float(input("Valor de Kps (ej 1.8e-10): "))
    
    # Kps = (x*S)^x * (y*S)^y = (x^x * y^y) * S^(x+y)
    coef = (x ** x) * (y ** y)
    s_agua = (kps / coef) ** (1.0 / (x + y))
    print("\nSolubilidad molar en agua pura:")
    print("S = {:.5e} M".format(s_agua))
    
    c_com = float(input("\nConc ion comun agregado C (0 si no hay): "))
    if c_com > 0:
        es_x = input("El ion comun es A (1) o B (2)?: ")
        if es_x == "1":
            s_com = ((kps / (c_com ** x)) / (y ** y)) ** (1.0 / y)
        else:
            s_com = ((kps / (c_com ** y)) / (x ** x)) ** (1.0 / x)
        print("Solubilidad con ion comun:")
        print("S' = {:.5e} M".format(s_com))

def menu_gravimetria():
    print("\n--- ANALISIS GRAVIMETRICO (UNID. 6) ---")
    m_muestra = float(input("Masa muestra inicial (g): "))
    m_ppdo = float(input("Masa precipitado seco (g): "))
    pm_analito = float(input("PM del Analito buscado (g/mol): "))
    pm_ppdo = float(input("PM del Precipitado pesado (g/mol): "))
    a = float(input("Moles analito en formula (ej 2 en Fe2O3): "))
    b = float(input("Moles ppdo (usualmente 1): "))
    
    fg = (pm_analito * a) / (pm_ppdo * b)
    m_analito = m_ppdo * fg
    pct = (m_analito / m_muestra) * 100.0
    
    print("\n--- RESULTADOS ---")
    print("Factor Gravimetrico FG = {:.5f}".format(fg))
    print("Masa de Analito = {:.5f} g".format(m_analito))
    print("Porcentaje en muestra = {:.2f}%".format(pct))

while True:
    print("\n=== CROMATOGRAFIA, KPS Y GRAVIM ===")
    print("1: Cromatografia (N, H, k', alfa, Rs)")
    print("2: Solubilidad Kps e Ion Comun")
    print("3: Factor Gravimetrico y % Pureza")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_cromatografia()
    elif op == "2":
        menu_kps()
    elif op == "3":
        menu_gravimetria()
    elif op == "0":
        break
