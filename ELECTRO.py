import math

def menu_ciclotron():
    print("\n--- LORENTZ Y ESPECTROMETRO MASAS ---")
    q_elem = float(input("Carga en e (ej 1 para p+, -1 para e-): "))
    m_kg = float(input("Masa particula (kg, ej 1.67e-27): "))
    v = float(input("Velocidad v (m/s): "))
    B = float(input("Campo magnetico B (Teslas): "))
    
    q = abs(q_elem) * 1.6021766e-19
    f_mag = q * v * B
    r_giro = (m_kg * v) / (q * B)
    t_per = (2.0 * math.pi * m_kg) / (q * B)
    f_cic = 1.0 / t_per
    
    print("\n--- RESULTADOS ---")
    print("Fuerza magnetica F = {:.4e} N".format(f_mag))
    print("Radio de Larmor r  = {:.4e} m".format(r_giro))
    print("Frec ciclotron fc  = {:.4e} Hz".format(f_cic))

def menu_rlc():
    print("\n--- IMPEDANCIA RLC EN SERIE (AC) ---")
    r = float(input("Resistencia R (Ohms): "))
    l = float(input("Inductancia L (Henrios, ej 1e-3): "))
    c = float(input("Capacitancia C (Faradios, ej 1e-6): "))
    f = float(input("Frecuencia fuente f (Hz): "))
    
    w = 2.0 * math.pi * f
    xl = w * l
    xc = 1.0 / (w * c) if c > 0 else 0.0
    x_net = xl - xc
    z = math.sqrt((r ** 2) + (x_net ** 2))
    phi = math.degrees(math.atan2(x_net, r))
    f0 = 1.0 / (2.0 * math.pi * math.sqrt(l * c)) if (l*c) > 0 else 0
    
    print("\n--- RESULTADOS ---")
    print("XL = {:.3f} Ohm | XC = {:.3f} Ohm".format(xl, xc))
    print("Impedancia |Z| = {:.3f} Ohm".format(z))
    print("Fase phi = {:.2f} deg (FP = {:.3f})".format(phi, math.cos(math.radians(phi))))
    print("Frec Resonancia f0 = {:.2f} Hz".format(f0))

while True:
    print("\n=== ELECTROMAGNETISMO Y AC ===")
    print("1: Lorentz, Ciclotron y Espectrometro")
    print("2: Circuito RLC, Impedancia y Resonancia")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_ciclotron()
    elif op == "2":
        menu_rlc()
    elif op == "0":
        break
