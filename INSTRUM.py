import math


def menu_ccd():
    print("\n--- SENSOR CCD/CMOS Y FOV ---")
    f = float(input("Focal telescopio/lente F (mm): "))
    px = float(input("Tamano pixel (um, ej 3.76): "))
    nx = int(input("Resolucion ancho (px, ej 4096): "))
    ny = int(input("Resolucion alto  (px, ej 2160): "))

    # Escala en arcsec/pixel
    scale = 206.265 * (px / f)
    fov_x = (scale * nx) / 3600.0
    fov_y = (scale * ny) / 3600.0

    print("\n--- RESULTADOS ---")
    print("Escala: {:.2f} arcsec/px".format(scale))
    print("FOV: {:.2f} x {:.2f} grados".format(fov_x, fov_y))
    print("FOV: {:.1f}' x {:.1f}' arcmin".format(fov_x * 60, fov_y * 60))
    print('Seeing ideal Nyquist: {:.2f}"'.format(scale * 2.5))


def menu_snr():
    print("\n--- SNR FOTOMETRIA / SENSOR ---")
    s = float(input("Fotones fuente (S): "))
    b = float(input("Fotones fondo cielo (B/px): "))
    d = float(input("Dark current (e-/px/s): "))
    t = float(input("Tiempo exposicion (s): "))
    rn = float(input("Read noise (e- rms): "))
    npix = float(input("Pixeles apertura (Npix): "))

    senal = s * t
    ruido = math.sqrt(senal + npix * (b * t + d * t + (rn**2)))
    snr = senal / ruido
    err_mag = 1.0857 / snr

    print("\n--- RESULTADOS ---")
    print("Senal total: {:.1f} e-".format(senal))
    print("Ruido total: {:.2f} e-".format(ruido))
    print("SNR = {:.2f} ({:.2f} dB)".format(snr, 20 * math.log10(snr)))
    print("Error Fotom: +/- {:.4f} mag".format(err_mag))


def menu_electronica():
    print("\n--- FILTROS RC Y DECIBELES ---")
    print("1: Filtro RC (Frec corte y Tau)")
    print("2: Ganancia en dB y Divisor V")
    m = input("Opcion: ")
    if m == "1":
        r = float(input("Resistencia R (Ohms): "))
        c = float(input("Capacitancia C (Faradios, ej 1e-6): "))
        tau = r * c
        fc = 1.0 / (2.0 * math.pi * tau)
        print("Const tiempo Tau = {:.4e} s".format(tau))
        print("Frec corte fc = {:.2f} Hz".format(fc))
    else:
        vin = float(input("Voltaje entrada Vin: "))
        vout = float(input("Voltaje salida Vout: "))
        db_v = 20.0 * math.log10(vout / vin)
        db_p = 10.0 * math.log10(vout / vin)
        print("dB (Voltaje 20log): {:.2f} dB".format(db_v))
        print("dB (Potencia 10log): {:.2f} dB".format(db_p))


while True:
    print("\n=== INSTRUMENTACION Y SENSORES ===")
    print("1: Escala CCD/CMOS y FOV")
    print("2: SNR Sensor y Error Mag")
    print("3: Filtros RC y Decibeles")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_ccd()
    elif op == "2":
        menu_snr()
    elif op == "3":
        menu_electronica()
    elif op == "0":
        break
