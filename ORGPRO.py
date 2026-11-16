import math


def menu_hibridacion():
    print("\n--- HIBRIDACION Y GEOMETRIA ---")
    ne = int(input("Num esterico (enlaces + pares libres): "))
    pl = int(input("Pares electronicos libres (0, 1, 2...): "))

    print("\n--- RESULTADO ---")
    if ne == 4:
        if pl == 0:
            print("Hibridacion: sp3")
            print("Geometria: Tetraedrica (109.5°)")
        elif pl == 1:
            print("Hibridacion: sp3")
            print("Geometria: Piramidal trigonal (~107°)")
        elif pl == 2:
            print("Hibridacion: sp3")
            print("Geometria: Angular / V (~104.5°)")
    elif ne == 3:
        if pl == 0:
            print("Hibridacion: sp2")
            print("Geometria: Trigonal plana (120°)")
        elif pl == 1:
            print("Hibridacion: sp2")
            print("Geometria: Angular / V")
    elif ne == 2:
        if pl == 0:
            print("Hibridacion: sp")
            print("Geometria: Lineal (180°)")
    else:
        print("Revisar datos ingresados.")


def menu_balance_energetico():
    print("\n--- BALANCE ENERGETICO (DH) ---")
    print("DH = Sum(En,rotos) - Sum(En,formados)")
    e_rotos = float(input("Suma E enlaces ROTOS (kJ/mol): "))
    e_form = float(input("Suma E enlaces FORMADOS (kJ/mol): "))

    dh = e_rotos - e_form
    print("\n--- RESULTADO ---")
    print("Delta H = {:.2f} kJ/mol".format(dh))
    if dh < 0:
        print("Reaccion EXOTERMICA ( favorable )")
    else:
        print("Reaccion ENDOTERMICA")


def menu_pka_efectos():
    print("\n--- EFECTOS ELECTRONICOS (Acidez) ---")
    print("Ayuda memoria pKa aproximados:")
    print("- Acidos carboxilicos: ~ 4 - 5")
    print("- Fenoles: ~ 10")
    print("- Alcoholes / Agua: ~ 15 - 16")
    print("- Alquinos terminales: ~ 25")
    print("- Aldehidos / Cetonas (alfa): ~ 20")
    print("- Alcanos: ~ 50")
    input("\n[Enter para continuar...]")


while True:
    print("\n=== QUIMICA ORGANICA PRO ===")
    print("1: Hibridacion y Geometria VSEPR")
    print("2: Balance Energetico (Delta H)")
    print("3: Guia Rapida pKa y Efectos")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_hibridacion()
    elif op == "2":
        menu_balance_energetico()
    elif op == "3":
        menu_pka_efectos()
    elif op == "0":
        break
