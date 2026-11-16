import math

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
          - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
          + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))

def menu_cramer3x3():
    print("\n--- SISTEMA 3x3 (REGLA DE CRAMER) ---")
    print("Ingresa coef de a1*x + b1*y + c1*z = d1")
    A = []
    B = []
    for i in range(1, 4):
        print("Ecuacion {}:".format(i))
        a = float(input("  a{}: ".format(i)))
        b = float(input("  b{}: ".format(i)))
        c = float(input("  c{}: ".format(i)))
        d = float(input("  d{} (indep): ".format(i)))
        A.append([a, b, c])
        B.append(d)
        
    dA = det3(A)
    Ax = [[B[0], A[0][1], A[0][2]], [B[1], A[1][1], A[1][2]], [B[2], A[2][1], A[2][2]]]
    Ay = [[A[0][0], B[0], A[0][2]], [A[1][0], B[1], A[1][2]], [A[2][0], B[2], A[2][2]]]
    Az = [[A[0][0], A[0][1], B[0]], [A[1][0], A[1][1], B[1]], [A[2][0], A[2][1], B[2]]]
    
    dx = det3(Ax)
    dy = det3(Ay)
    dz = det3(Az)
    
    print("\n--- DETERMINANTES ---")
    print("det(A)  = {:.4f}".format(dA))
    print("det(Ax) = {:.4f} | det(Ay) = {:.4f}".format(dx, dy))
    print("det(Az) = {:.4f}".format(dz))
    if abs(dA) > 1e-9:
        print("--- SOLUCION UNICA (SCD) ---")
        print("x = {:.5f}".format(dx / dA))
        print("y = {:.5f}".format(dy / dA))
        print("z = {:.5f}".format(dz / dA))
    else:
        print("det(A)=0 -> Sistema Indet (SCI) o Incomp (SI)")

def menu_autovalores2x2():
    print("\n--- AUTOVALORES E INVERSA 2x2 ---")
    a = float(input("a11: "))
    b = float(input("a12: "))
    c = float(input("a21: "))
    d = float(input("a22: "))
    
    tr = a + d
    det = a * d - b * c
    disc = (tr ** 2) - 4.0 * det
    
    print("\nTraza = {:.4f} | Det = {:.4f}".format(tr, det))
    print("Polinomio: L^2 - ({:.3g})*L + ({:.3g}) = 0".format(tr, det))
    
    if disc >= 0:
        l1 = (tr + math.sqrt(disc)) / 2.0
        l2 = (tr - math.sqrt(disc)) / 2.0
        print("Lambda 1 = {:.5f}".format(l1))
        print("Lambda 2 = {:.5f}".format(l2))
        if abs(b) > 1e-9:
            print("Autovector v1 ~ ({:.3f}, {:.3f})".format(b, l1 - a))
            print("Autovector v2 ~ ({:.3f}, {:.3f})".format(b, l2 - a))
    else:
        re = tr / 2.0
        im = math.sqrt(-disc) / 2.0
        print("Lambda = {:.4f} +/- {:.4f}i".format(re, im))
        
    if abs(det) > 1e-9:
        print("-- Matriz Inversa A^-1 --")
        print("[ {:.4f}  {:.4f} ]".format(d/det, -b/det))
        print("[ {:.4f}  {:.4f} ]".format(-c/det, a/det))

def menu_plano():
    print("\n--- PLANO Y DISTANCIA EN R3 ---")
    print("Plano A*x + B*y + C*z + D = 0 y Punto P0")
    A = float(input("Coef A: "))
    B = float(input("Coef B: "))
    C = float(input("Coef C: "))
    D = float(input("Coef D: "))
    x0 = float(input("Punto x0: "))
    y0 = float(input("Punto y0: "))
    z0 = float(input("Punto z0: "))
    
    norm = math.sqrt(A**2 + B**2 + C**2)
    dist = abs(A*x0 + B*y0 + C*z0 + D) / norm
    print("\n|Normal| = {:.4f}".format(norm))
    print("Distancia Punto-Plano = {:.5f}".format(dist))

while True:
    print("\n=== ALGEBRA LINEAL Y GEOM ===")
    print("1: Sistema 3x3 y Determinantes (Cramer)")
    print("2: Autovalores, Polinomio e Inversa 2x2")
    print("3: Distancia Punto a Plano en R3")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_cramer3x3()
    elif op == "2":
        menu_autovalores2x2()
    elif op == "3":
        menu_plano()
    elif op == "0":
        break
