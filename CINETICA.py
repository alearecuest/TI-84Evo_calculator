import math

def menu_ordenes():
    print("\n--- CINETICA ORDEN 0, 1 Y 2 ---")
    orden = int(input("Orden de reaccion (0, 1 o 2): "))
    a0 = float(input("Conc inicial [A]0: "))
    k = float(input("Constante de velocidad k: "))
    t = float(input("Tiempo transcurrido t: "))
    
    if orden == 0:
        at = max(0.0, a0 - k * t)
        t_half = a0 / (2.0 * k)
        v = k
    elif orden == 1:
        at = a0 * math.exp(-k * t)
        t_half = math.log(2.0) / k
        v = k * at
    else:
        at = 1.0 / ((1.0 / a0) + k * t)
        t_half = 1.0 / (k * a0)
        v = k * (at ** 2)
        
    print("\n--- RESULTADOS ---")
    print("Conc final [A](t) = {:.5e}".format(at))
    print("Consumido = {:.2f}%".format(((a0 - at) / a0) * 100.0))
    print("Semivida (t1/2) = {:.4e}".format(t_half))
    print("Velocidad inst v(t) = {:.4e}".format(v))

def menu_hallar_orden():
    print("\n--- DETERMINAR ORDEN (METODO TASAS) ---")
    c1 = float(input("Conc 1 [A]1: "))
    v1 = float(input("Vel inicial 1 (v1): "))
    c2 = float(input("Conc 2 [A]2: "))
    v2 = float(input("Vel inicial 2 (v2): "))
    
    n = math.log(v2 / v1) / math.log(c2 / c1)
    k = v1 / (c1 ** n)
    print("\n--- RESULTADOS ---")
    print("Orden calculado n = {:.2f} (redondear: {})".format(n, round(n)))
    print("Constante k = {:.4e}".format(k))

def menu_secuencial():
    print("\n--- REACCION SECUENCIAL A -> B -> C ---")
    print("O decaimiento en cadena (Bateman)")
    a0 = float(input("Cantidad inicial A0: "))
    k1 = float(input("k1 (o lambda_1 de A->B): "))
    k2 = float(input("k2 (o lambda_2 de B->C): "))
    t = float(input("Tiempo t: "))
    
    at = a0 * math.exp(-k1 * t)
    if abs(k1 - k2) > 1e-9:
        bt = a0 * (k1 / (k2 - k1)) * (math.exp(-k1 * t) - math.exp(-k2 * t))
        t_max = math.log(k1 / k2) / (k1 - k2)
        b_max = a0 * ((k1 / k2) ** (k2 / (k1 - k2)))
    else:
        bt = a0 * k1 * t * math.exp(-k1 * t)
        t_max = 1.0 / k1
        b_max = a0 / math.e
    ct = max(0.0, a0 - at - bt)
    
    print("\n--- RESULTADOS EN t ---")
    print("[A](t) = {:.4e}".format(at))
    print("[B](t) = {:.4e}".format(bt))
    print("[C](t) = {:.4e}".format(ct))
    if t_max > 0:
        print("Tiempo pico max de B (tmax) = {:.4f}".format(t_max))
        print("Cantidad max de B (Bmax) = {:.4e}".format(b_max))

while True:
    print("\n=== CINETICA DE ORDEN SUPERIOR ===")
    print("1: Leyes Integradas (Orden 0, 1, 2)")
    print("2: Hallar Orden (Velocidades Iniciales)")
    print("3: Cadena A -> B -> C (Bateman)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_ordenes()
    elif op == "2":
        menu_hallar_orden()
    elif op == "3":
        menu_secuencial()
    elif op == "0":
        break
