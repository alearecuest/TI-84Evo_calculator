import math

G = 6.67430e-11
C = 299792458.0
M_SOL = 1.98847e30
R_TIERRA = 6.371e6
UA = 1.495978707e11


def menu_orbita():
    print("\n--- MECANICA ORBITAL ---")
    print("Masa cuerpo central:")
    print("1:En kg | 2:En Masas Solares")
    t_m = int(input("Opcion: "))
    m_in = float(input("Valor masa: "))
    M = m_in * M_SOL if t_m == 2 else m_in

    print("Distancia orbital (r / a):")
    print("1:Metros | 2:km | 3:UA")
    t_r = int(input("Opcion: "))
    r_in = float(input("Valor dist: "))
    if t_r == 2:
        r = r_in * 1000.0
    elif t_r == 3:
        r = r_in * UA
    else:
        r = r_in

    v_orb = math.sqrt(G * M / r)
    v_esc = math.sqrt(2.0 * G * M / r)
    T_seg = 2.0 * math.pi * math.sqrt((r**3) / (G * M))
    r_sch = (2.0 * G * M) / (C**2)

    print("\n--- RESULTADOS ---")
    print("v_orb: {:.3f} km/s".format(v_orb / 1000.0))
    print("v_esc: {:.3f} km/s".format(v_esc / 1000.0))
    print("T (s): {:.4e} s".format(T_seg))
    print("T (d): {:.3f} dias".format(T_seg / 86400.0))
    print("T (a): {:.4f} anios".format(T_seg / 31557600.0))
    print("R_Schw: {:.4e} m".format(r_sch))


def menu_optica():
    print("\n--- OPTICA TELESCOPIOS ---")
    D = float(input("Apertura D (mm): "))
    F = float(input("Focal Telesc F (mm): "))
    fe = float(input("Focal Ocular fe (mm): "))
    lam = float(input("Lambda (nm, ej 550): "))

    f_num = F / D
    mag = F / fe
    pupila = D / mag
    dawes = 116.0 / D
    # Rayleigh en arcsec: 1.22 * (lam / D) * 206265
    rayleigh = 1.22 * ((lam * 1e-9) / (D * 1e-3)) * 206264.8
    m_lim = 2.7 + 5.0 * math.log10(D)

    print("\n--- RESULTADOS ---")
    print("Relacion focal: f/{:.2f}".format(f_num))
    print("Aumento: {:.1f}x".format(mag))
    print("Pupila salida: {:.2f} mm".format(pupila))
    print("Dawes: {:.2f} arcsec".format(dawes))
    print("Rayleigh: {:.2f} arcsec".format(rayleigh))
    print("Mag limite aprox: {:.1f}".format(m_lim))


def menu_astrofisica():
    print("\n--- DISTANCIA Y MAGNITUD ---")
    p = float(input("Paralaje p (arcsec, 0 si no): "))
    if p > 0:
        d = 1.0 / p
        print("d = {:.3f} pc ({:.2f} ly)".format(d, d * 3.26156))
    else:
        d = float(input("Distancia d (en parsecs): "))

    m = float(input("Mag aparente (m): "))
    mod_dist = 5.0 * math.log10(d) - 5.0
    M = m - mod_dist
    print("Modulo (m-M): {:.3f}".format(mod_dist))
    print("Mag Absoluta (M): {:.3f}".format(M))


while True:
    print("\n=== SUITE ASTRONOMIA ===")
    print("1: Orbitas y Kepler")
    print("2: Optica e Instrumentos")
    print("3: Paralaje y Magnitudes")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_orbita()
    elif op == "2":
        menu_optica()
    elif op == "3":
        menu_astrofisica()
    elif op == "0":
        break
