import math


def menu_beer_lambert():
    print("\n--- LEY DE BEER-LAMBERT (UV-Vis) ---")
    print("Dejar en 0 el valor que deseas calcular:")
    a = float(input("Absorbancia (A): "))
    eps = float(input("Absortividad molar (epsilon en L/(mol*cm)): "))
    b = float(input("Paso optico (b en cm): "))
    c = float(input("Concentracion (c en mol/L): "))

    if a == 0:
        res = eps * b * c
        print("\nAbsorbancia (A) calculada = {:.4f}".format(res))
        print("Transmitancia (%T) = {:.2f}%".format(10.0 ** (-res) * 100.0))
    elif c == 0:
        res = a / (eps * b) if (eps * b) != 0 else 0
        print("\nConcentracion (c) calculada = {:.5e} mol/L".format(res))
    elif eps == 0:
        res = a / (b * c) if (b * c) != 0 else 0
        print("\nEpsilon calculada = {:.4e} L/(mol*cm)".format(res))


def menu_diluciones_seriadas():
    print("\n--- DILUCIONES SERIADAS ---")
    c_ini = float(input("Concentracion inicial (C0): "))
    vol_alicuota = float(input("Volumen transferido alicuota (mL): "))
    vol_balon = float(input("Volumen total balon/tubo (mL): "))
    pasos = int(input("Cantidad de diluciones sucesivas: "))

    factor = vol_alicuota / vol_balon
    c_actual = c_ini
    print("\n--- FACTOR DE DILUCION ---")
    print("Factor por paso = 1 / {:.2f}".format(vol_balon / vol_alicuota))

    for i in range(1, pasos + 1):
        c_actual *= factor
        print("Tubo {}: Concentracion = {:.5e}".format(i, c_actual))


while True:
    print("\n=== SUITE ESPECTRO Y DILUCIONES ===")
    print("1: Ley de Beer-Lambert y Transmitancia")
    print("2: Diluciones Seriadas (Curvas de Calibrado)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_beer_lambert()
    elif op == "2":
        menu_diluciones_seriadas()
    elif op == "0":
        break
