import math

def menu_outliers():
    print("\n--- OUTLIERS: DIXON Y GRUBBS ---")
    n = int(input("Cantidad de replicas (n>=3): "))
    datos = []
    for i in range(1, n + 1):
        datos.append(float(input("Dato {}: ".format(i))))
    datos.sort()
    
    media = sum(datos) / n
    s = math.sqrt(sum((x - media)**2 for x in datos) / (n - 1))
    rango = datos[-1] - datos[0]
    
    # Sospechoso menor y mayor
    q_min = (datos[1] - datos[0]) / rango if rango > 0 else 0
    q_max = (datos[-1] - datos[-2]) / rango if rango > 0 else 0
    g_min = abs(datos[0] - media) / s if s > 0 else 0
    g_max = abs(datos[-1] - media) / s if s > 0 else 0
    
    print("\nOrdenados:", datos)
    print("Media = {:.4g} | s = {:.4g}".format(media, s))
    print("RSD (CV%) = {:.2f}%".format((s / abs(media)) * 100.0))
    print("-- Test Q de Dixon --")
    print("Q_min ({:.4g}) = {:.4f}".format(datos[0], q_min))
    print("Q_max ({:.4g}) = {:.4f}".format(datos[-1], q_max))
    print("Ref Q(95%): n3:0.97 n4:0.83 n5:0.71 n6:0.63")
    print("-- Test de Grubbs --")
    print("G_max = {:.4f} (Ref n4:1.48 n5:1.71 n6:1.89)".format(max(g_min, g_max)))

def menu_anova():
    print("\n--- ANOVA DE 1 VIA (k GRUPOS) ---")
    k = int(input("Numero de grupos/tratamientos (k): "))
    grupos = []
    n_tot = 0
    suma_tot = 0.0
    
    for i in range(1, k + 1):
        ni = int(input("Tamano grupo {}: ".format(i)))
        g = []
        for j in range(1, ni + 1):
            val = float(input("  G{} dato {}: ".format(i, j)))
            g.append(val)
        grupos.append(g)
        n_tot += ni
        suma_tot += sum(g)
        
    gran_media = suma_tot / n_tot
    ss_between = 0.0
    ss_within = 0.0
    
    print("\n--- MEDIAS POR GRUPO ---")
    for i, g in enumerate(grupos):
        mi = sum(g) / len(g)
        ss_between += len(g) * ((mi - gran_media) ** 2)
        ss_within += sum((x - mi) ** 2 for x in g)
        print("G{}: media = {:.4g} (n={})".format(i+1, mi, len(g)))
        
    df_b = k - 1
    df_w = n_tot - k
    ms_b = ss_between / df_b
    ms_w = ss_within / df_w if df_w > 0 else 0
    f_val = ms_b / ms_w if ms_w > 0 else 0
    
    print("\n--- TABLA ANOVA ---")
    print("SS_Entre = {:.4g} (gl={})".format(ss_between, df_b))
    print("SS_Dentro= {:.4g} (gl={})".format(ss_within, df_w))
    print("MS_Entre = {:.4g} | MS_Dentro = {:.4g}".format(ms_b, ms_w))
    print("Estadistico F = {:.4f}".format(f_val))

def fact(n):
    r = 1
    for i in range(2, int(n) + 1):
        r *= i
    return r

def menu_prob():
    print("\n--- BINOMIAL Y POISSON ---")
    print("1: Binomial (n, p, k) | 2: Poisson (lambda, k)")
    op = input("Opcion: ")
    if op == "1":
        n = int(input("Ensayos (n): "))
        p = float(input("Prob exito (p, ej 0.25): "))
        k = int(input("Exitos buscados (k): "))
        comb = fact(n) / (fact(k) * fact(n - k))
        pk = comb * (p ** k) * ((1.0 - p) ** (n - k))
        acum = 0.0
        for i in range(0, k + 1):
            ci = fact(n) / (fact(i) * fact(n - i))
            acum += ci * (p ** i) * ((1.0 - p) ** (n - i))
        print("\nP(X = {}) = {:.5f} ({:.2f}%)".format(k, pk, pk*100))
        print("P(X <= {}) = {:.5f}".format(k, acum))
        print("P(X >= {}) = {:.5f}".format(k, 1.0 - acum + pk))
        print("Media = {:.2f} | s = {:.3f}".format(n*p, math.sqrt(n*p*(1-p))))
    else:
        lam = float(input("Tasa media (lambda): "))
        k = int(input("Eventos (k): "))
        pk = (math.exp(-lam) * (lam ** k)) / fact(k)
        acum = sum((math.exp(-lam) * (lam ** i)) / fact(i) for i in range(0, k + 1))
        print("\nP(X = {}) = {:.5f} ({:.2f}%)".format(k, pk, pk*100))
        print("P(X <= {}) = {:.5f}".format(k, acum))

while True:
    print("\n=== BIOESTADISTICA PRO ===")
    print("1: Outliers (Dixon Q y Grubbs)")
    print("2: ANOVA de 1 Via (Tabla F)")
    print("3: Binomial y Poisson")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_outliers()
    elif op == "2":
        menu_anova()
    elif op == "3":
        menu_prob()
    elif op == "0":
        break
