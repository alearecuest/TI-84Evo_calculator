import math

def menu_eficiencia():
    print("\n--- KCAT Y EFICIENCIA CATALITICA ---")
    vmax = float(input("Vmax (en M/s o uM/s): "))
    et = float(input("Conc Enzima [Et] (misma u. M/uM): "))
    km = float(input("Km (en M, ej 1e-5): "))
    
    kcat = vmax / et
    efic = kcat / km
    t_rec = 1.0 / kcat if kcat > 0 else 0
    
    print("\n--- RESULTADOS ---")
    print("kcat (Recambio) = {:.4e} s^-1".format(kcat))
    print("Tiempo por ciclo = {:.4e} s".format(t_rec))
    print("kcat / Km = {:.4e} M^-1*s^-1".format(efic))
    if efic >= 1e8:
        print("Nota: Limite de difusion (perfeccion)!")

def menu_inhibicion():
    print("\n--- DIAGNOSTICO DE INHIBICION ---")
    vmax = float(input("Vmax sin inhibidor: "))
    km = float(input("Km sin inhibidor: "))
    vmax_ap = float(input("Vmax aparente (con I): "))
    km_ap = float(input("Km aparente (con I): "))
    i_conc = float(input("Conc Inhibidor [I]: "))
    
    print("\n--- RESULTADOS ---")
    tol_v = abs(vmax - vmax_ap) / vmax
    tol_k = abs(km - km_ap) / km
    
    if tol_v < 0.05 and km_ap > km:
        print("Tipo: COMPETITIVA")
        alpha = km_ap / km
        ki = i_conc / (alpha - 1.0)
        print("Factor alpha = {:.3f}".format(alpha))
        print("Constante Ki = {:.4e}".format(ki))
    elif tol_k < 0.05 and vmax_ap < vmax:
        print("Tipo: NO COMPETITIVA PURA")
        alpha_p = vmax / vmax_ap
        ki = i_conc / (alpha_p - 1.0)
        print("Factor alpha' = {:.3f}".format(alpha_p))
        print("Ki = Ki' = {:.4e}".format(ki))
    elif vmax_ap < vmax and km_ap < km:
        ratio_orig = km / vmax
        ratio_ap = km_ap / vmax_ap
        if abs(ratio_orig - ratio_ap) / ratio_orig < 0.08:
            print("Tipo: ACOMPETITIVA (Uncompetitive)")
            alpha_p = vmax / vmax_ap
            kip = i_conc / (alpha_p - 1.0)
            print("Factor alpha' = {:.3f}".format(alpha_p))
            print("Constante Ki' = {:.4e}".format(kip))
        else:
            print("Tipo: MIXTA")
            alpha_p = vmax / vmax_ap
            alpha = (km_ap / km) * alpha_p
            ki = i_conc / (alpha - 1.0) if alpha > 1 else 0
            kip = i_conc / (alpha_p - 1.0) if alpha_p > 1 else 0
            print("Ki  (union a E)  = {:.4e}".format(ki))
            print("Ki' (union a ES) = {:.4e}".format(kip))
    else:
        print("Tipo: MIXTA")
        alpha_p = vmax / vmax_ap
        alpha = (km_ap / km) * alpha_p
        ki = i_conc / (alpha - 1.0) if alpha > 1 else 0
        kip = i_conc / (alpha_p - 1.0) if alpha_p > 1 else 0
        print("Ki  (union a E)  = {:.4e}".format(ki))
        print("Ki' (union a ES) = {:.4e}".format(kip))

def menu_hill():
    print("\n--- ALOSTERISMO (EC. DE HILL) ---")
    vmax = float(input("Vmax: "))
    v = float(input("Velocidad medida v: "))
    s = float(input("Conc Sustrato [S]: "))
    k05 = float(input("K0.5 (S al 50% Vmax): "))
    n_h = float(input("Coef Hill nH (0 para despejarlo): "))
    
    theta = v / vmax
    y_hill = theta / (1.0 - theta)
    print("\nFraccion saturacion Y = {:.4f}".format(theta))
    print("log(v / (Vmax - v)) = {:.4f}".format(math.log10(y_hill)))
    if n_h == 0 and s != k05:
        nh_calc = math.log10(y_hill) / math.log10(s / k05)
        print("Coef Hill nH = {:.3f}".format(nh_calc))
        if nh_calc > 1.05:
            print("Cooperatividad POSITIVA")
        elif nh_calc < 0.95:
            print("Cooperatividad NEGATIVA")
    elif n_h > 0:
        v_teo = (vmax * (s ** n_h)) / ((k05 ** n_h) + (s ** n_h))
        print("v teorica = {:.4e}".format(v_teo))

while True:
    print("\n=== ENZIMOLOGIA AVANZADA ===")
    print("1: kcat y Eficiencia (kcat/Km)")
    print("2: Inhibicion (Ki, Comp/Mixta/Acomp)")
    print("3: Alosterismo y Ecuacion de Hill")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_eficiencia()
    elif op == "2":
        menu_inhibicion()
    elif op == "3":
        menu_hill()
    elif op == "0":
        break
