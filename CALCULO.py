import math

def eval_fx(expr, x_val):
    env = {
        "x": x_val, "math": math,
        "sin": math.sin, "cos": math.cos, "tan": math.tan,
        "exp": math.exp, "ln": math.log, "log": math.log10,
        "sqrt": math.sqrt, "pi": math.pi, "e": math.e
    }
    return eval(expr, env)

def menu_derivada_taylor():
    print("\n--- DERIVADAS, TANGENTE Y TAYLOR ---")
    print("Usa x, sin(x), cos(x), exp(x), ln(x), x**2")
    expr = input("f(x) = ")
    x0 = float(input("Punto x0: "))
    h = 1e-4
    
    f0 = eval_fx(expr, x0)
    f1 = (eval_fx(expr, x0 + h) - eval_fx(expr, x0 - h)) / (2.0 * h)
    f2 = (eval_fx(expr, x0 + h) - 2.0*f0 + eval_fx(expr, x0 - h)) / (h ** 2)
    f3 = (eval_fx(expr, x0 + 2*h) - 2*eval_fx(expr, x0 + h) + 2*eval_fx(expr, x0 - h) - eval_fx(expr, x0 - 2*h)) / (2.0 * (h ** 3))
    
    b_tan = f0 - f1 * x0
    print("\n--- RESULTADOS EN x0 = {} ---".format(x0))
    print("f(x0)   = {:.6g}".format(f0))
    print("f'(x0)  = {:.6g}".format(f1))
    print("f''(x0) = {:.6g}".format(f2))
    print("f'''(x0)= {:.6g}".format(f3))
    print("Recta Tangente: y = {:.4g}*x + ({:.4g})".format(f1, b_tan))
    print("-- Coeficientes Taylor P3(x) --")
    print("c0={:.4g} | c1={:.4g} | c2={:.4g} | c3={:.4g}".format(f0, f1, f2/2.0, f3/6.0))

def menu_simpson():
    print("\n--- INTEGRAL DEFINIDA (SIMPSON 1/3) ---")
    expr = input("f(x) = ")
    a = float(input("Limite inferior a: "))
    b = float(input("Limite superior b: "))
    n = int(input("Subintervalos pares n (ej 10 o 100): "))
    if n % 2 != 0:
        n += 1
        
    h = (b - a) / n
    s_imp = 0.0
    s_par = 0.0
    for i in range(1, n):
        xi = a + i * h
        fx = eval_fx(expr, xi)
        if i % 2 == 1:
            s_imp += fx
        else:
            s_par += fx
            
    fa = eval_fx(expr, a)
    fb = eval_fx(expr, b)
    integ = (h / 3.0) * (fa + 4.0*s_imp + 2.0*s_par + fb)
    trap = (h / 2.0) * (fa + 2.0*(s_imp + s_par) + fb)
    
    print("\n--- RESULTADOS (h = {:.4g}) ---".format(h))
    print("Integral Simpson = {:.7g}".format(integ))
    print("Integral Trapecio= {:.7g}".format(trap))
    print("Valor Medio f_med= {:.6g}".format(integ / (b - a)))

def menu_edo_rk4():
    print("\n--- EDO dy/dx = f(x,y) (RUNGE-KUTTA 4) ---")
    expr = input("dy/dx = f(x,y) = ")
    x = float(input("x0 inicial: "))
    y = float(input("y0 inicial: "))
    xf = float(input("x final deseado: "))
    pasos = int(input("Cantidad de pasos (ej 5 o 10): "))
    
    h = (xf - x) / pasos
    print("\n--- TABLA PASO A PASO (h={:.3g}) ---".format(h))
    for i in range(1, pasos + 1):
        env = {"x": x, "y": y, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "ln": math.log}
        k1 = h * eval(expr, env)
        env["x"] = x + 0.5*h; env["y"] = y + 0.5*k1
        k2 = h * eval(expr, env)
        env["x"] = x + 0.5*h; env["y"] = y + 0.5*k2
        k3 = h * eval(expr, env)
        env["x"] = x + h; env["y"] = y + k3
        k4 = h * eval(expr, env)
        
        y += (k1 + 2.0*k2 + 2.0*k3 + k4) / 6.0
        x += h
        print("P{}: x={:.4g} -> y={:.6g}".format(i, x, y))

while True:
    print("\n=== CALCULO DIFERENCIAL E INTEGRAL ===")
    print("1: Derivadas, Tangente y Taylor")
    print("2: Integral Definida (Simpson/Trapecio)")
    print("3: EDO Runge-Kutta 4 (dy/dx = f(x,y))")
    print("0: Salir")
    op = input("Seleccion: ")
    if op == "1":
        menu_derivada_taylor()
    elif op == "2":
        menu_simpson()
    elif op == "3":
        menu_edo_rk4()
    elif op == "0":
        break
