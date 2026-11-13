import math

R_L = 0.082057  # L*atm/(mol*K)
R_J = 8.31446  # J/(mol*K)


def menu_vdw():
    print("\n--- GAS REAL VAN DER WAALS ---")
    n = float(input("Moles (n): "))
    V = float(input("Volumen V (Litros): "))
    T_c = float(input("Temp (C): "))
    a = float(input("Const a (L^2*atm/mol^2): "))
    b = float(input("Const b (L/mol): "))

    T = T_c + 273.15
    p_id = (n * R_L * T) / V
    p_vdw = ((n * R_L * T) / (V - n * b)) - ((a * (n**2)) / (V**2))
    z = (p_vdw * V) / (n * R_L * T)

    print("\n--- RESULTADOS ---")
    print("P Ideal: {:.4f} atm".format(p_id))
    print("P VdW  : {:.4f} atm".format(p_vdw))
    print("Factor compresib Z: {:.4f}".format(z))


def menu_coligativas():
    print("\n--- PROPIEDADES COLIGATIVAS ---")
    i = float(input("Factor Van't Hoff i (ej 1 o 2): "))
    m = float(input("Molalidad o Molaridad (m o M): "))
    t_c = float(input("Temperatura (C): "))

    T = t_c + 273.15
    pi_atm = i * m * R_L * T
    # Para agua: Kc = 1.86, Kb = 0.512
    dt_c = i * 1.86 * m
    dt_b = i * 0.512 * m

    print("\n--- RESULTADOS (En Agua) ---")
    print("Presion Osmotica: {:.3f} atm".format(pi_atm))
    print("Osmolaridad: {:.3f} Osm/L".format(i * m))
    print("Descenso criosc dTc: -{:.3f} C".format(dt_c))
    print("Aumento ebullosc dTb: +{:.3f} C".format(dt_b))


def menu_clausius():
    print("\n--- CLAUSIUS-CLAPEYRON (Pvap) ---")
    p1 = float(input("Presion P1: "))
    t1 = float(input("Temp T1 (C): ")) + 273.15
    t2 = float(input("Temp T2 (C): ")) + 273.15
    dh_kj = float(input("dH vaporizacion (kJ/mol): "))

    exponent = ((dh_kj * 1000.0) / R_J) * ((1.0 / t1) - (1.0 / t2))
    p2 = p1 * math.exp(exponent)
    print("\nPresion P2 = {:.4f} (misma u. que P1)".format(p2))


while True:
    print("\n=== SUITE FISICOQUIMICA ===")
    print("1: Gases Ideales vs Van der Waals")
    print("2: Osmosis y Coligativas")
    print("3: Clausius-Clapeyron (P vapor)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_vdw()
    elif op == "2":
        menu_coligativas()
    elif op == "3":
        menu_clausius()
    elif op == "0":
        break
