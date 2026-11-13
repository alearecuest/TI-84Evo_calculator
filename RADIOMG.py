import math


def menu_vectores():
    print("\n--- VECTORES EN R3 ---")
    print("Vector U (ux, uy, uz):")
    ux = float(input("ux: "))
    uy = float(input("uy: "))
    uz = float(input("uz: "))
    print("Vector V (vx, vy, vz):")
    vx = float(input("vx: "))
    vy = float(input("vy: "))
    vz = float(input("vz: "))

    mod_u = math.sqrt(ux**2 + uy**2 + uz**2)
    mod_v = math.sqrt(vx**2 + vy**2 + vz**2)
    dot = ux * vx + uy * vy + uz * vz

    # Producto cruz U x V
    cx = uy * vz - uz * vy
    cy = uz * vx - ux * vz
    cz = ux * vy - uy * vx
    mod_c = math.sqrt(cx**2 + cy**2 + cz**2)

    ang_deg = 0.0
    if mod_u > 0 and mod_v > 0:
        cos_t = max(-1.0, min(1.0, dot / (mod_u * mod_v)))
        ang_deg = math.degrees(math.acos(cos_t))

    print("\n--- RESULTADOS ---")
    print("|U| = {:.4f} | |V| = {:.4f}".format(mod_u, mod_v))
    print("U . V (Escalar) = {:.4f}".format(dot))
    print("Angulo = {:.2f} grados".format(ang_deg))
    print("U x V = ({:.3f}, {:.3f}, {:.3f})".format(cx, cy, cz))
    print("|U x V| (Area) = {:.4f}".format(mod_c))


def menu_regresion():
    print("\n--- REGRESION LINEAL (y = m*x + b) ---")
    n = int(input("Cantidad de puntos (N): "))
    sx = sy = sxx = syy = sxy = 0.0
    for i in range(1, n + 1):
        print("Punto {}:".format(i))
        x = float(input("  x: "))
        y = float(input("  y: "))
        sx += x
        sy += y
        sxx += x * x
        syy += y * y
        sxy += x * y

    denom = n * sxx - sx * sx
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    r_num = n * sxy - sx * sy
    r_den = math.sqrt((n * sxx - sx**2) * (n * syy - sy**2))
    r = r_num / r_den if r_den != 0 else 0

    print("\n--- RESULTADOS ---")
    print("Pendiente (m) : {:.5e}".format(m))
    print("Ordenada (b)  : {:.5e}".format(b))
    print("r  = {:.5f} | R^2 = {:.5f}".format(r, r**2))

    interp = input("Interpolar valor Y para hallar X? (1:Si/0:No): ")
    if interp == "1":
        y_inc = float(input("Ingresa Y medido: "))
        print("X calculado = {:.5e}".format((y_inc - b) / m))


def menu_cuadratica():
    print("\n--- CUADRATICA a*x^2 + b*x + c = 0 ---")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    disc = b**2 - 4 * a * c
    xv = -b / (2 * a)
    yv = a * (xv**2) + b * xv + c
    print("\nVertice: ({:.4f}, {:.4f})".format(xv, yv))
    print("Discriminante: {:.4f}".format(disc))

    if disc >= 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        print("x1 = {:.5f}".format(x1))
        print("x2 = {:.5f}".format(x2))
    else:
        re = -b / (2 * a)
        im = math.sqrt(-disc) / (2 * a)
        print("Raices Complejas:")
        print("x1 = {:.4f} + {:.4f}i".format(re, im))
        print("x2 = {:.4f} - {:.4f}i".format(re, im))


while True:
    print("\n=== SUITE MATEMATICA ===")
    print("1: Vectores en R3 (Escalar y Cruz)")
    print("2: Regresion Lineal / Calibracion")
    print("3: Cuadratica y Vertice")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_vectores()
    elif op == "2":
        menu_regresion()
    elif op == "3":
        menu_cuadratica()
    elif op == "0":
        break
