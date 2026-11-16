import math

def menu_monod_quimiostato():
    print("\n--- MONOD Y QUIMIOSTATO ---")
    umax = float(input("mu_max (h^-1): "))
    ks = float(input("Ks afinidad (g/L): "))
    s0 = float(input("Sustrato entrada S0 (g/L): "))
    y_xs = float(input("Rendimiento Y_x/s (gX/gS): "))
    d = float(input("Tasa dilucion D = F/V (h^-1): "))
    
    d_crit = umax * (s0 / (ks + s0))
    print("\n--- RESULTADOS ---")
    print("D critica (Washout) = {:.4f} h^-1".format(d_crit))
    if d >= d_crit:
        print("ALERTA: D >= D_crit -> LAVADO CELULAR!")
    else:
        s_est = (ks * d) / (umax - d)
        x_est = y_xs * (s0 - s_est)
        prod_x = d * x_est
        print("Sustrato residual S* = {:.4f} g/L".format(s_est))
        print("Biomasa estacionaria X* = {:.4f} g/L".format(x_est))
        print("Productividad (D*X) = {:.4f} g/(L*h)".format(prod_x))

def menu_kla():
    print("\n--- TRANSFERENCIA OXIGENO (kLa) ---")
    kla = float(input("Coeficiente kLa (h^-1): "))
    c_star = float(input("O2 saturacion C* (mg/L, ej 8.0): "))
    c_l = float(input("O2 disuelto actual CL (mg/L): "))
    x = float(input("Biomasa X (g/L): "))
    
    otr = kla * (c_star - c_l)
    qo2 = otr / x if x > 0 else 0
    print("\n--- RESULTADOS ---")
    print("OTR = {:.2f} mg O2/(L*h)".format(otr))
    print("qO2 especifico = {:.2f} mg O2/(gX*h)".format(qo2))

def menu_escalado():
    print("\n--- ESCALADO DE BIORREACTORES ---")
    v1 = float(input("Volumen reactor piloto V1 (L): "))
    v2 = float(input("Volumen reactor planta V2 (L): "))
    n1 = float(input("RPM agitador 1 (N1): "))
    
    # Relacion geometrica D2/D1 = (V2/V1)^(1/3)
    ratio_d = (v2 / v1) ** (1.0 / 3.0)
    # Criterio 1: Velocidad en punta constante (N2 = N1 * (D1/D2))
    n2_tip = n1 / ratio_d
    # Criterio 2: P/V constante turbulento (N2 = N1 * (D1/D2)^(2/3))
    n2_pv = n1 * ((1.0 / ratio_d) ** (2.0 / 3.0))
    
    print("\n--- RESULTADOS ESCALADO ---")
    print("Factor diametro D2/D1 = {:.3f}x".format(ratio_d))
    print("N2 (P/V constante)   = {:.1f} RPM".format(n2_pv))
    print("N2 (V_tip constante) = {:.1f} RPM".format(n2_tip))

while True:
    print("\n=== BIOPROCESOS Y REACTORES ===")
    print("1: Monod y Quimiostato Continuo")
    print("2: Transferencia O2 (kLa y OTR)")
    print("3: Escalado de Biorreactores")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_monod_quimiostato()
    elif op == "2":
        menu_kla()
    elif op == "3":
        menu_escalado()
    elif op == "0":
        break
