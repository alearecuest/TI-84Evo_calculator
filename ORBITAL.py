import math

G = 6.67430e-11
G0 = 9.80665

def menu_hohmann():
    print("\n--- TRANSFERENCIA DE HOHMANN ---")
    m_c = float(input("Masa cuerpo central (kg, Tierra=5.972e24): "))
    r1_km = float(input("Radio orbita inicial r1 (km desde centro): "))
    r2_km = float(input("Radio orbita final r2 (km desde centro): "))
    
    mu = G * m_c
    r1 = r1_km * 1000.0
    r2 = r2_km * 1000.0
    a_t = (r1 + r2) / 2.0
    
    v1 = math.sqrt(mu / r1)
    v2 = math.sqrt(mu / r2)
    vt1 = math.sqrt(mu * ((2.0 / r1) - (1.0 / a_t)))
    vt2 = math.sqrt(mu * ((2.0 / r2) - (1.0 / a_t)))
    
    dv1 = abs(vt1 - v1)
    dv2 = abs(v2 - vt2)
    t_vuelo = math.pi * math.sqrt((a_t ** 3) / mu)
    
    print("\n--- RESULTADOS ---")
    print("dv1 (Inyeccion)   = {:.3f} m/s".format(dv1))
    print("dv2 (Circulariz.) = {:.3f} m/s".format(dv2))
    print("Delta-V TOTAL     = {:.3f} m/s".format(dv1 + dv2))
    print("Tiempo de vuelo   = {:.2f} h ({:.2f} d)".format(t_vuelo/3600, t_vuelo/86400))

def menu_tsiolkovsky():
    print("\n--- ECUACION COHETE TSIOLKOVSKY ---")
    isp = float(input("Impulso especifico Isp (s): "))
    m0 = float(input("Masa inicial total m0 (kg): "))
    mf = float(input("Masa final seca mf (kg): "))
    
    ve = isp * G0
    dv = ve * math.log(m0 / mf)
    frac = ((m0 - mf) / m0) * 100.0
    print("\nVelocidad escape gases ve = {:.1f} m/s".format(ve))
    print("Delta-V maximo = {:.2f} m/s ({:.3f} km/s)".format(dv, dv/1000.0))
    print("Fraccion propelente = {:.1f}%".format(frac))

def menu_roche_hill():
    print("\n--- LIMITE DE ROCHE Y ESFERA HILL ---")
    r_p = float(input("Radio cuerpo primario Rp (km): "))
    rho_p = float(input("Densidad primario (kg/m3): "))
    rho_s = float(input("Densidad satelite (kg/m3): "))
    
    roche_rig = r_p * ((2.0 * (rho_p / rho_s)) ** (1.0 / 3.0))
    roche_flu = 2.44 * r_p * ((rho_p / rho_s) ** (1.0 / 3.0))
    print("\nRoche (Cuerpo rigido) = {:.1f} km".format(roche_rig))
    print("Roche (Cuerpo fluido) = {:.1f} km".format(roche_flu))

while True:
    print("\n=== ASTRODINAMICA Y MISIONES ===")
    print("1: Transferencia de Hohmann (dv1, dv2)")
    print("2: Cohete de Tsiolkovsky (Isp y dv)")
    print("3: Limite de Roche (Fuerzas de Marea)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_hohmann()
    elif op == "2":
        menu_tsiolkovsky()
    elif op == "3":
        menu_roche_hill()
    elif op == "0":
        break
