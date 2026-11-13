import math

SIGMA_SB = 5.670374e-8
B_WIEN = 2.89777e-3
R_SOL = 6.957e8
L_SOL = 3.828e26
C_KMS = 299792.458


def menu_estelar():
    print("\n--- CUERPO NEGRO Y ESTRELLAS ---")
    T = float(input("Temp efectiva Teff (K): "))
    r_sol = float(input("Radio en Radios Solares (R/R_sol): "))

    R = r_sol * R_SOL
    lam_max_nm = (B_WIEN / T) * 1e9
    flujo = SIGMA_SB * (T**4)
    lum_w = 4.0 * math.pi * (R**2) * flujo
    lum_sol = lum_w / L_SOL
    m_bol = 4.74 - 2.5 * math.log10(lum_sol)

    print("\n--- RESULTADOS ---")
    print("Pico Wien: {:.1f} nm".format(lam_max_nm))
    print("Flujo sup: {:.4e} W/m2".format(flujo))
    print("Luminosidad: {:.4e} W".format(lum_w))
    print("L / L_sol  : {:.4f}".format(lum_sol))
    print("Mag Bolometrica: {:.2f}".format(m_bol))


def menu_redshift():
    print("\n--- DOPPLER Y REDSHIFT (z) ---")
    l0 = float(input("Lambda reposo l0 (nm o A): "))
    lobs = float(input("Lambda observada l_obs: "))

    z = (lobs - l0) / l0
    v_clas = z * C_KMS
    # Formula relativista exacta
    zp1_2 = (z + 1.0) ** 2
    beta = (zp1_2 - 1.0) / (zp1_2 + 1.0)
    v_rel = beta * C_KMS
    h0 = 70.0  # km/s/Mpc
    d_mpc = v_rel / h0

    print("\n--- RESULTADOS ---")
    print("Redshift z = {:.6f}".format(z))
    print("v clasica  = {:.2f} km/s".format(v_clas))
    print("v relativ. = {:.2f} km/s".format(v_rel))
    if z > 0.001:
        print("Dist Hubble (H0=70): {:.1f} Mpc".format(d_mpc))


def menu_altaz():
    print("\n--- ECUATORIAL A HORIZONTAL ---")
    lat = math.radians(float(input("Latitud obs (deg, MVD=-34.9): ")))
    dec = math.radians(float(input("Declinacion dec (deg): ")))
    ha_h = float(input("Angulo Horario H (en horas): "))
    ha = math.radians(ha_h * 15.0)

    sin_alt = math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(
        ha
    )
    alt = math.asin(max(-1.0, min(1.0, sin_alt)))
    alt_deg = math.degrees(alt)

    zenit = 90.0 - alt_deg
    airmass = 1.0 / math.cos(math.radians(zenit)) if alt_deg > 5.0 else 99.9
    print("\n--- RESULTADOS ---")
    print("Altura (h): {:.2f} deg".format(alt_deg))
    print("Dist Cenital (z): {:.2f} deg".format(zenit))
    print("Masa de Aire (X): {:.2f}".format(airmass))


while True:
    print("\n=== ASTROFISICA Y COSMOLOGIA ===")
    print("1: Estrellas (Wien y Stefan-Boltz)")
    print("2: Redshift, Doppler y Hubble")
    print("3: Coordenadas y Masa de Aire")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_estelar()
    elif op == "2":
        menu_redshift()
    elif op == "3":
        menu_altaz()
    elif op == "0":
        break
