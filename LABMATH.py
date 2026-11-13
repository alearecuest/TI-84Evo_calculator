import math


def prop_errores():
    print("\n--- PROPAGACION DE ERRORES ---")
    a = float(input("Valor A: "))
    da = float(input("Error dA: "))
    b = float(input("Valor B: "))
    db = float(input("Error dB: "))

    err_sum = math.sqrt(da**2 + db**2)
    print("\n[A + B] = {:.4g} +/- {:.4g}".format(a + b, err_sum))
    print("[A - B] = {:.4g} +/- {:.4g}".format(a - b, err_sum))

    if a != 0 and b != 0:
        rel = math.sqrt((da / a) ** 2 + (db / b) ** 2)
        prod = a * b
        print("[A * B] = {:.4g} +/- {:.4g}".format(prod, abs(prod) * rel))
        if b != 0:
            div = a / b
            print("[A / B] = {:.4g} +/- {:.4g}".format(div, abs(div) * rel))

    n = float(input("\nExponente n para A^n (0 omitir): "))
    if n != 0 and a != 0:
        pot = a**n
        dpot = abs(pot) * abs(n) * (da / abs(a))
        print("[A^n] = {:.4g} +/- {:.4g}".format(pot, dpot))


def kepler_solver():
    print("\n--- ECUACION DE KEPLER ---")
    print("Resuelve M = E - e*sin(E)")
    M_deg = float(input("Anomalia Media M (grados): "))
    e = float(input("Excentricidad e (0 a 1): "))
    M = math.radians(M_deg)

    E = M
    for i in range(1, 7):
        f = E - e * math.sin(E) - M
        fp = 1.0 - e * math.cos(E)
        E = E - f / fp
        print("Iter {}: E = {:.5f} rad".format(i, E))
        if abs(f) < 1e-7:
            break

    # Anomalia verdadera nu
    tan_nu2 = math.sqrt((1.0 + e) / (1.0 - e)) * math.tan(E / 2.0)
    nu = 2.0 * math.atan(tan_nu2)
    print("\nE final: {:.3f} deg".format(math.degrees(E)))
    print("Anom. Verdadera: {:.3f} deg".format(math.degrees(nu)))


while True:
    print("\n=== LAB Y METODOS NUMERICOS ===")
    print("1: Propagacion de Errores")
    print("2: Ecuacion de Kepler (Iterativo)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        prop_errores()
    elif op == "2":
        kepler_solver()
    elif op == "0":
        break
