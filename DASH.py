import math
try:
    import ti_draw as draw
    HAS_DRAW = True
except ImportError:
    HAS_DRAW = False

def dashboard_orbita():
    print("\n--- VISUALIZADOR ORBITAL ---")
    e = float(input("Excentricidad e (0 a 0.85): "))
    a_ua = float(input("Semieje mayor a (UA): "))
    t_anios = math.sqrt(a_ua ** 3)
    rp = a_ua * (1.0 - e)
    ra = a_ua * (1.0 + e)

    if not HAS_DRAW:
        print("Periodo T = {:.2f} anios".format(t_anios))
        return

    draw.clear()
    draw.set_color(15, 20, 35)
    draw.fill_rect(0, 0, 320, 240)

    draw.set_color(0, 180, 255)
    draw.fill_rect(0, 0, 320, 26)
    draw.set_color(255, 255, 255)
    draw.draw_text(10, 18, "ASTRO-OS // SIMULADOR KEPLER")

    cx, cy = 115, 130
    rx = 85
    ry = int(rx * math.sqrt(1.0 - e**2))
    foco_x = cx + int(rx * e)

    draw.set_color(40, 50, 70)
    draw.draw_line(15, cy, 215, cy)
    draw.draw_line(cx, 45, cx, 215)

    draw.set_color(0, 230, 200)
    px_ant = cx + rx
    py_ant = cy
    for deg in range(10, 370, 10):
        rad = math.radians(deg)
        px = cx + int(rx * math.cos(rad))
        py = cy + int(ry * math.sin(rad))
        draw.draw_line(px_ant, py_ant, px, py)
        px_ant, py_ant = px, py

    draw.set_color(255, 210, 0)
    draw.fill_circle(foco_x, cy, 7)

    draw.set_color(255, 80, 80)
    draw.fill_circle(cx + rx, cy, 4)

    draw.set_color(30, 40, 65)
    draw.fill_rect(222, 35, 92, 195)
    draw.set_color(0, 255, 140)
    draw.draw_text(228, 55, "TELEMETRIA")
    draw.set_color(220, 220, 220)
    draw.draw_text(228, 80, "a: {:.2f} UA".format(a_ua))
    draw.draw_text(228, 100, "e: {:.3f}".format(e))
    draw.draw_text(228, 125, "T (Kepler):")
    draw.set_color(255, 220, 0)
    draw.draw_text(228, 142, "{:.2f} yr".format(t_anios))
    draw.set_color(180, 200, 255)
    draw.draw_text(228, 170, "q: {:.2f} UA".format(rp))
    draw.draw_text(228, 190, "Q: {:.2f} UA".format(ra))
    draw.set_color(130, 130, 130)
    draw.draw_text(228, 220, "[clear] Salir")
    draw.show_draw()

def dashboard_michaelis():
    print("\n--- GRAFICADOR ENZIMATICO ---")
    vmax = float(input("Vmax: "))
    km = float(input("Km: "))

    if not HAS_DRAW:
        return

    draw.clear()
    draw.set_color(15, 20, 35)
    draw.fill_rect(0, 0, 320, 240)

    draw.set_color(180, 0, 255)
    draw.fill_rect(0, 0, 320, 26)
    draw.set_color(255, 255, 255)
    draw.draw_text(10, 18, "BIOTECH-OS // MICHAELIS-MENTEN")

    ox, oy = 40, 205
    w, h = 250, 150
    draw.set_color(150, 150, 150)
    draw.draw_line(ox, oy, ox + w, oy)
    draw.draw_line(ox, oy, ox, oy - h)

    draw.set_color(80, 90, 110)
    draw.draw_line(ox, oy - h, ox + w, oy - h)
    draw.draw_line(ox, oy - int(h/2), ox + w, oy - int(h/2))

    s_max = 5.0 * km
    draw.set_color(0, 255, 150)
    px_ant, py_ant = ox, oy
    for i in range(1, 51):
        s = (i / 50.0) * s_max
        v = (vmax * s) / (km + s)
        px = ox + int((s / s_max) * w)
        py = oy - int((v / vmax) * h)
        draw.draw_line(px_ant, py_ant, px, py)
        px_ant, py_ant = px, py

    kx = ox + int((km / s_max) * w)
    ky = oy - int(h / 2)
    draw.set_color(255, 80, 80)
    draw.draw_line(kx, oy, kx, ky)
    draw.fill_circle(kx, ky, 4)

    draw.set_color(255, 220, 0)
    draw.draw_text(ox + 8, oy - h + 14, "Vmax = {:.2g}".format(vmax))
    draw.set_color(255, 120, 120)
    draw.draw_text(kx + 5, ky + 15, "Km = {:.2g}".format(km))
    draw.set_color(200, 200, 200)
    draw.draw_text(ox + 180, oy + 18, "[S] (0 a 5*Km)")
    draw.show_draw()

while True:
    print("\n=== DASHBOARD GRAFICO PRO ===")
    print("1: Simulador Orbital (Dark Mode)")
    print("2: Curva Michaelis-Menten")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        dashboard_orbita()
    elif op == "2":
        dashboard_michaelis()
    elif op == "0":
        break
