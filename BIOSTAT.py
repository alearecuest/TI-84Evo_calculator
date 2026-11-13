import math


def menu_diagnostico():
    print("\n--- TEST DIAGNOSTICO / CLINICO ---")
    vp = float(input("Verdaderos Positivos (VP): "))
    fp = float(input("Falsos Positivos     (FP): "))
    fn = float(input("Falsos Negativos     (FN): "))
    vn = float(input("Verdaderos Negativos (VN): "))

    sens = (vp / (vp + fn)) * 100.0
    esp = (vn / (vn + fp)) * 100.0
    vpp = (vp / (vp + fp)) * 100.0
    vpn = (vn / (vn + fn)) * 100.0
    acc = ((vp + vn) / (vp + fp + fn + vn)) * 100.0

    print("\n--- RESULTADOS ---")
    print("Sensibilidad : {:.2f}%".format(sens))
    print("Especificidad: {:.2f}%".format(esp))
    print("VPP (Positivo): {:.2f}%".format(vpp))
    print("VPN (Negativo): {:.2f}%".format(vpn))
    print("Exactitud global: {:.2f}%".format(acc))


def menu_t_student():
    print("\n--- TEST T DE DOS MUESTRAS ---")
    m1 = float(input("Media grupo 1 (x1): "))
    s1 = float(input("Desvio estandar 1 (s1): "))
    n1 = float(input("Tamano muestra 1 (n1): "))

    m2 = float(input("Media grupo 2 (x2): "))
    s2 = float(input("Desvio estandar 2 (s2): "))
    n2 = float(input("Tamano muestra 2 (n2): "))

    gl = n1 + n2 - 2.0
    sp2 = (((n1 - 1.0) * (s1**2)) + ((n2 - 1.0) * (s2**2))) / gl
    se = math.sqrt(sp2 * ((1.0 / n1) + (1.0 / n2)))
    t_val = abs(m1 - m2) / se

    print("\n--- RESULTADOS ---")
    print("Desvio agrupado Sp: {:.4f}".format(math.sqrt(sp2)))
    print("Error estandar SE : {:.4f}".format(se))
    print("Estadistico |t|   : {:.4f}".format(t_val))
    print("Grados libertad gl: {:.0f}".format(gl))


def menu_ic():
    print("\n--- INTERVALO DE CONFIANZA ---")
    media = float(input("Media muestral (x): "))
    s = float(input("Desvio estandar (s): "))
    n = float(input("Tamano muestra (n): "))

    se = s / math.sqrt(n)
    ic95 = 1.96 * se
    ic99 = 2.576 * se
    print("\nError Estandar (SEM): {:.4g}".format(se))
    print("IC 95%: {:.4g} +/- {:.4g}".format(media, ic95))
    print("  [{:.4g} , {:.4g}]".format(media - ic95, media + ic95))
    print("IC 99%: {:.4g} +/- {:.4g}".format(media, ic99))


while True:
    print("\n=== SUITE BIOESTADISTICA ===")
    print("1: Sensibilidad, Especif y VPP")
    print("2: Test t-Student (2 muestras)")
    print("3: Intervalo Confianza y SEM")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_diagnostico()
    elif op == "2":
        menu_t_student()
    elif op == "3":
        menu_ic()
    elif op == "0":
        break
