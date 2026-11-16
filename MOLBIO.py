import math

def menu_qpcr():
    print("\n--- qPCR: METODO 2^(-ddCt) ---")
    print("Gen Target (GOI) y Housekeeping (HK):")
    ct_t_goi = float(input("Ct Tratado (Target): "))
    ct_t_hk  = float(input("Ct Tratado (Housekeeping): "))
    ct_c_goi = float(input("Ct Control (Target): "))
    ct_c_hk  = float(input("Ct Control (Housekeeping): "))
    
    dct_t = ct_t_goi - ct_t_hk
    dct_c = ct_c_goi - ct_c_hk
    ddct = dct_t - dct_c
    fold = 2.0 ** (-ddct)
    
    print("\n--- RESULTADOS ---")
    print("dCt Tratado = {:.3f}".format(dct_t))
    print("dCt Control = {:.3f}".format(dct_c))
    print("ddCt = {:.3f}".format(ddct))
    print("Expresion relativa (Fold) = {:.4f}x".format(fold))
    if fold < 1.0:
        print("Sub-expresion: -{:.2f}x ({:.1f}%)".format(1.0/fold, fold*100))

def menu_ligacion():
    print("\n--- LIGACION VECTOR : INSERTO ---")
    ng_vec = float(input("Masa de Vector (ng, ej 50): "))
    kb_vec = float(input("Tamano Vector (kb o pb): "))
    kb_ins = float(input("Tamano Inserto (misma u.): "))
    ratio = float(input("Relacion molar Ins:Vec (ej 3 para 3:1): "))
    
    ng_ins = ng_vec * (kb_ins / kb_vec) * ratio
    print("\n--- RESULTADOS ---")
    print("Masa de Inserto necesaria = {:.2f} ng".format(ng_ins))
    c_ins = float(input("Conc stock inserto (ng/uL, 0 omitir): "))
    if c_ins > 0:
        print("Volumen inserto a pipetear = {:.2f} uL".format(ng_ins / c_ins))

def menu_centrifuga():
    print("\n--- CENTRIFUGA: RPM <-> RCF (xg) ---")
    r_cm = float(input("Radio del rotor r (en cm): "))
    print("1: RPM a xg (RCF) | 2: xg (RCF) a RPM")
    op = input("Opcion: ")
    if op == "1":
        rpm = float(input("Velocidad (RPM): "))
        rcf = 1.118e-5 * r_cm * (rpm ** 2)
        print("Fuerza RCF = {:.1f} x g".format(rcf))
    else:
        rcf = float(input("Fuerza deseada (x g): "))
        rpm = math.sqrt(rcf / (1.118e-5 * r_cm))
        print("Configurar a = {:.0f} RPM".format(rpm))

while True:
    print("\n=== BIOLOGIA MOLECULAR LAB ===")
    print("1: qPCR Expresion Relativa (ddCt)")
    print("2: Clonado y Ligacion (Inserto:Vector)")
    print("3: Centrifugacion (RPM <-> RCF xg)")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_qpcr()
    elif op == "2":
        menu_ligacion()
    elif op == "3":
        menu_centrifuga()
    elif op == "0":
        break
