import math


def menu_idh_organica():
    print("\n--- INDICE DE DEFICIENCIA (IDH) ---")
    c = int(input("Carbonos (C): "))
    h = int(input("Hidrogenos (H): "))
    n = int(input("Nitrogenos (N): "))
    hal = int(input("Halogenos (F,Cl,Br,I): "))

    idh = c - (h / 2.0) - (hal / 2.0) + (n / 2.0) + 1.0
    print("\nIDH (Insaturacion / Anillos) = {:.1f}".format(idh))
    if idh == 1:
        print("Sugerencia: 1 doble enlace o 1 ciclo.")
    elif idh >= 4:
        print("Sugerencia: Posible sistema aromatico (bencenico).")


def menu_estereoisomeros():
    print("\n--- ESTEREOCENTROS Y CONFIGURACION ---")
    n = int(input("Numero de centros quirales (n): "))
    max_iso = 2**n
    print("Maximo de estereoisomeros teoricos (2^n) = {}".format(max_iso))

    print("\nCalculo de Exceso Enantiomerico (ee):")
    a_obs = float(input("Rotacion optica observada [alpha]_obs: "))
    a_puro = float(input("Rotacion optica del enantiomero puro [alpha]_puro: "))

    if a_puro != 0:
        ee = (abs(a_obs) / abs(a_puro)) * 100.0
        r_pct = 50.0 + (ee / 2.0)
        s_pct = 50.0 - (ee / 2.0)
        print("Exceso Enantiomerico (ee) = {:.2f}%".format(ee))
        print("Fraccion Isomero Mayoritario = {:.2f}%".format(r_pct))
        print("Fraccion Isomero Minoritario = {:.2f}%".format(s_pct))


while True:
    print("\n=== SUITE ESTEREO Y ESTRUCTURA ===")
    print("1: IDH (Grado de Insaturacion)")
    print("2: Estereoisomeros maximos y Exceso Enantiomerico")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_idh_organica()
    elif op == "2":
        menu_estereoisomeros()
    elif op == "0":
        break
