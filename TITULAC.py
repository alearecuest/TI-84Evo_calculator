import math

def menu_poliprotico():
    print("\n--- FRACCIONES ALFA (DIPROTICO) ---")
    print("Ej H2CO3 o aproximacion H3PO4")
    pka1 = float(input("pKa1: "))
    pka2 = float(input("pKa2: "))
    ph = float(input("pH de la solucion: "))
    
    h = 10.0 ** (-ph)
    k1 = 10.0 ** (-pka1)
    k2 = 10.0 ** (-pka2)
    
    den = (h ** 2) + (k1 * h) + (k1 * k2)
    a0 = (h ** 2) / den
    a1 = (k1 * h) / den
    a2 = (k1 * k2) / den
    
    print("\n--- DISTRIBUCION DE ESPECIES ---")
    print("a0 [H2A]  = {:.4f} ({:.2f}%)".format(a0, a0*100))
    print("a1 [HA-]  = {:.4f} ({:.2f}%)".format(a1, a1*100))
    print("a2 [A2-]  = {:.4f} ({:.2f}%)".format(a2, a2*100))

def menu_edta_dureza():
    print("\n--- EDTA Y DUREZA DEL AGUA ---")
    print("1: Dureza (ppm CaCO3) | 2: Kf' condicional")
    op = input("Opcion: ")
    if op == "1":
        m_edta = float(input("Molaridad EDTA (M, ej 0.01): "))
        v_edta = float(input("Volumen EDTA gastado (mL): "))
        v_muestra = float(input("Volumen muestra agua (mL): "))
        # PM CaCO3 = 100.0869 g/mol -> mg/L (ppm)
        ppm = (m_edta * v_edta * 100.087 * 1000.0) / v_muestra
        mmol_l = (m_edta * v_edta * 1000.0) / v_muestra
        print("\n--- RESULTADOS ---")
        print("Dureza = {:.2f} ppm (mg/L CaCO3)".format(ppm))
        print("Conc Ca+Mg = {:.3f} mmol/L".format(mmol_l))
        if ppm < 60:
            print("Clasificacion: Agua BLANDA")
        elif ppm <= 120:
            print("Clasificacion: MODERADAMENTE DURA")
        elif ppm <= 180:
            print("Clasificacion: DURA")
        else:
            print("Clasificacion: MUY DURA")
    else:
        log_kf = float(input("log Kf (ej Ca=10.65, Mg=8.79): "))
        ph = float(input("pH (8, 9, 10, 11 o 12): "))
        # log(alfa_Y4-) a pH tipicos de buffers amoniacales
        tabla_a = {8: -2.27, 9: -1.28, 10: -0.45, 11: -0.07, 12: 0.0}
        log_a = tabla_a.get(int(round(ph)), -0.45)
        log_kfp = log_kf + log_a
        print("\nlog(alfa_Y4-) aprox = {:.2f}".format(log_a))
        print("log(Kf' condicional)= {:.2f}".format(log_kfp))
        print("Kf' = {:.4e}".format(10.0 ** log_kfp))

def menu_potenciometria():
    print("\n--- PUNTO EQUIVALENCIA (2da DERIV) ---")
    print("Ingresa 4 puntos (V, E) alrededor del salto:")
    v = []
    e = []
    for i in range(1, 5):
        v.append(float(input("V{} (mL): ".format(i))))
        e.append(float(input("E{} (mV o pH): ".format(i))))
        
    # Primera derivada en puntos medios
    d1 = []
    vm1 = []
    for i in range(3):
        d1.append((e[i+1] - e[i]) / (v[i+1] - v[i]))
        vm1.append((v[i+1] + v[i]) / 2.0)
        
    # Segunda derivada en dos puntos centrales
    d2_a = (d1[1] - d1[0]) / (vm1[1] - vm1[0])
    d2_b = (d1[2] - d1[1]) / (vm1[2] - vm1[1])
    va = (vm1[1] + vm1[0]) / 2.0
    vb = (vm1[2] + vm1[1]) / 2.0
    
    print("\n--- DERIVADAS ---")
    for i in range(3):
        print("V={:.2f} -> dE/dV = {:.2f}".format(vm1[i], d1[i]))
    print("d2E/dV2 en {:.2f}: {:.2f}".format(va, d2_a))
    print("d2E/dV2 en {:.2f}: {:.2f}".format(vb, d2_b))
    
    if d2_a * d2_b < 0:
        v_eq = va + (vb - va) * (abs(d2_a) / (abs(d2_a) + abs(d2_b)))
        print("\n>>> V equivalencia = {:.4f} mL <<<".format(v_eq))
    else:
        print("Nota: d2E/dV2 no cambio de signo en el tramo.")

while True:
    print("\n=== TITULACIONES Y EQUILIBRIOS ===")
    print("1: Acidos Diproticos (Fracciones Alfa)")
    print("2: EDTA, Kf' y Dureza del Agua")
    print("3: Potenciometria (1ra y 2da Derivada)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_poliprotico()
    elif op == "2":
        menu_edta_dureza()
    elif op == "3":
        menu_potenciometria()
    elif op == "0":
        break
