import math


def ver_constantes():
    print("\n--- CONSTANTES FUNDAMENTALES ---")
    print("c  = 2.99792458e8 m/s")
    print("h  = 6.62607e-34 J*s (4.1357e-15 eV*s)")
    print("G  = 6.67430e-11 N*m2/kg2")
    print("kB = 1.38065e-23 J/K (8.6173e-5 eV/K)")
    print("NA = 6.02214e23 mol^-1")
    print("R  = 8.31446 J/mol*K | 0.082057 L*atm")
    print("e  = 1.60218e-19 C | F = 96485.3 C/mol")
    input("\n[Enter para ver Masas y Astro...]")
    print("m_e = 9.10938e-31 kg (0.511 MeV)")
    print("m_p = 1.67262e-27 kg (938.27 MeV)")
    print("u   = 1.66054e-27 kg (931.49 MeV)")
    print("M_sol = 1.9885e30 kg | R_sol = 6.957e8 m")
    print("L_sol = 3.828e26 W   | UA = 1.4960e11 m")
    print("1 pc  = 3.0857e16 m  (3.2616 ly)")


def conv_energia_foton():
    print("\n--- FOTON: LAMBDA <-> ENERGIA ---")
    print("Que dato tenes? 1:nm | 2:eV | 3:Hz")
    op = input("Opcion: ")
    if op == "1":
        nm = float(input("Lambda (nm): "))
        ev = 1239.84193 / nm
        hz = 2.99792458e17 / nm
    elif op == "2":
        ev = float(input("Energia (eV): "))
        nm = 1239.84193 / ev
        hz = ev / 4.1356677e-15
    else:
        hz = float(input("Frecuencia (Hz): "))
        nm = 2.99792458e17 / hz
        ev = hz * 4.1356677e-15

    j = ev * 1.6021766e-19
    print("\nLambda : {:.3f} nm".format(nm))
    print("Energia: {:.4e} eV".format(ev))
    print("Energia: {:.4e} J".format(j))
    print("Frec   : {:.4e} Hz".format(hz))


def conv_presion_rad():
    print("\n--- PRESION Y RADIACION ---")
    print("1: Presion (atm -> Pa, mmHg, bar)")
    print("2: Actividad (Curie Ci <-> Becquerel Bq)")
    op = input("Opcion: ")
    if op == "1":
        atm = float(input("Presion en atm: "))
        print("{:.2f} Pa ( {:.4f} kPa )".format(atm * 101325.0, atm * 101.325))
        print("{:.2f} mmHg / Torr".format(atm * 760.0))
        print("{:.4f} bar".format(atm * 1.01325))
    else:
        mci = float(input("Actividad en mCi (miliCurie): "))
        bq = mci * 3.7e7
        print("Bq  = {:.4e} Bq".format(bq))
        print("MBq = {:.3f} MBq".format(bq / 1e6))


while True:
    print("\n=== CONSTANTES Y CONVERSOR ===")
    print("1: Tabla Constantes Fisicas/Astro")
    print("2: Conversor Foton (nm <-> eV <-> Hz)")
    print("3: Conversor Presion y Radiacion")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        ver_constantes()
    elif op == "2":
        conv_energia_foton()
    elif op == "3":
        conv_presion_rad()
    elif op == "0":
        break
