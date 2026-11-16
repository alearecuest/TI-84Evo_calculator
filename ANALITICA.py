import math


def menu_estadistica_analitica():
    print("\n--- ESTADISTICA Y ERRORES ---")
    print("Comparacion de metodos (t de Student pareada o independiente)")
    n = int(input("Numero de replicas (n): "))
    d_vals = []
    sum_d = 0.0
    for i in range(1, n + 1):
        val = float(input("Diferencia o valor {}: ".format(i)))
        d_vals.append(val)
        sum_d += val

    media = sum_d / n
    sum_sq = sum((x - media) ** 2 for x in d_vals)
    s = math.sqrt(sum_sq / (n - 1)) if n > 1 else 0.0
    t_calc = (abs(media) / (s / math.sqrt(n))) if s > 0 else 0.0

    print("\n--- RESULTADOS ---")
    print("Media de diferencias: {:.4f}".format(media))
    print("Desvio estandar (s): {:.4f}".format(s))
    print("Estadistico t calc: {:.4f}".format(t_calc))
    print("Ref t-critico (gl={}): 2.776 (p=0.05, n=5)".format(n - 1))


def menu_volumetria():
    print("\n--- VOLUMETRIA Y ESTANDARIZACION ---")
    print("Formula: M_a * V_a / sto_a = M_b * V_b / sto_b")
    ma = float(input("Molaridad titulante (M1): "))
    va = float(input("Volumen gastado titulante (V1 en mL): "))
    sto_a = float(input("Estequiometria titulante (coef): "))

    vb = float(input("Volumen analito alicuota (V2 en mL): "))
    sto_b = float(input("Estequiometria analito (coef): "))
    pm = float(input("Peso molecular del analito (g/mol): "))

    # Moles titulante = moles analito * (sto_a / sto_b) -> M_b * V_b / 1000
    mb = (ma * va * sto_b) / (vb * sto_a)
    gramos_L = mb * pm
    mg_dL = gramos_L * 100.0

    print("\n--- RESULTADOS ---")
    print("Concentracion Analito (M) = {:.5e}".format(mb))
    print("Concentracion (g/L) = {:.4f}".format(gramos_L))
    print("Concentracion (mg/dL) = {:.2f}".format(mg_dL))


while True:
    print("\n=== SUITE QUIMICA ANALITICA ===")
    print("1: Estadistica Analitica y t-Student")
    print("2: Calculos Volumetricos y Estequiometria")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_estadistica_analitica()
    elif op == "2":
        menu_volumetria()
    elif op == "0":
        break
