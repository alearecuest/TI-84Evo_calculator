# TI-84 Evo - Scientific & Engineering Python Suite

Coleccion de 25 scripts interactivos en **CircuitPython / MicroPython** disenados para la calculadora **Texas Instruments TI-84 Evo**. Automatiza el despeje de variables, pasos intermedios, visualizacion grafica y verificacion de resultados para examenes y laboratorios universitarios.

## Modulos Incluidos

| Script | Area / Materia | Herramientas y Calculos |
| :--- | :--- | :--- |
| **`ASTRO.py`** | Astronomia y Mecanica Orbital | Velocidad orbital/escape, periodo de Kepler ($T$), radio de Schwarzschild, optica instrumental ($f/\#$, aumento, Dawes, Rayleigh, pupila) y paralaje/magnitudes. |
| **`ASTRO2.py`** | Astrofisica y Cosmologia | Cuerpo negro estelar (Wien, Stefan-Boltzmann, $L/L_\odot$), Redshift relativista ($z$), Ley de Hubble y transformacion Ecuatorial a Horizontal + Masa de Aire ($X$). |
| **`INSTRUM.py`** | Instrumentacion y Sensores | Escala de placa CCD/CMOS (arcsec/px), campo de vision ($FOV$), limite de Nyquist, relacion senal-ruido ($SNR$), error fotometrico, filtros $RC$ y decibeles ($dB$). |
| **`BIOTECH.py`** | Biotecnologia y Quimica Analitica | Buffers (Henderson-Hasselbalch), cinetica enzimatica de Michaelis-Menten + Lineweaver-Burk, Ley de Beer-Lambert, diluciones y crecimiento celular ($\mu, t_d$). |
| **`BIOQUIM.py`** | Bioquimica y Biologia Molecular | Energia libre de Gibbs ($\Delta G'$ real y $K'_{eq}$), potencial de Nernst, pureza y concentracion de ADN/ARN ($A_{260}/A_{280}$) y $T_m$ / $\%GC$ de primers PCR. |
| **`ENZIMAS.py`** | Enzimologia Avanzada e Inhibicion | Numero de recambio ($k_{cat}$), eficiencia catalitica ($k_{cat}/K_m$), diagnostico de inhibicion (competitiva, acompetitiva, no competitiva y mixta con calculo de $K_i$ y $K_i'$) y ecuacion de Hill ($n_H$). |
| **`TERMO.py`** | Termodinamica y Electroforesis | Ecuacion de Van 't Hoff ($\Delta H^\circ, \Delta S^\circ$ y $K_{eq}$ a distintas temperaturas), punto isoelectrico ($pI$) y migracion electroforetica, fuerza ionica ($I$) y coeficiente de actividad de Debye-Huckel ($\gamma$). |
| **`CINETICA.py`** | Cinetica Quimica y Radiactiva | Leyes integradas de orden 0, 1 y 2 ($[A]_t, t_{1/2}, v$), determinacion de orden por velocidades iniciales y reacciones secuenciales / decaimiento en cadena $A \rightarrow B \rightarrow C$ (ecuacion de Bateman y $t_{\max}$). |
| **`BIOLOGIA.py`** | Biologia, Genetica y Ecologia | Equilibrio de Hardy-Weinberg ($p, q, p^2, 2pq, q^2$), test de $\chi^2$ para cruzas geneticas, conteo en camara de Neubauer e indices de Shannon ($H'$) y Simpson. |
| **`BIOSTAT.py`** | Bioestadistica y Diagnostico | Sensibilidad, especificidad, $VPP$ y $VPN$ clinico, test $t$ de Student para dos muestras independientes ($S_p, SE, |t|$) e intervalos de confianza (95% y 99%). |
| **`STATPRO.py`** | Bioestadistica Avanzada y ANOVA | Deteccion de outliers (Test Q de Dixon y Test de Grubbs), tabla ANOVA de 1 via completa ($SS_B, SS_W, MS, F$) y distribuciones discretas (Binomial y Poisson exactas y acumuladas). |
| **`ORGANICA.py`** | Quimica Organica | Indice de Deficiencia de Hidrogeno (IDH) y composicion centesimal, formula empirica desde analisis elemental, polarimetria ($[\alpha]_D$, $\%ee$) y cinetica de Arrhenius. |
| **`ORGPRO.py`** | Quimica Organica Avanzada | Hibridacion VSEPR y geometria molecular (tetraedrica, trigonal, lineal), balance energetico de reacciones ($\Delta H$) y guia de pKa. |
| **`ANALITICA.py`** | Quimica Analitica (UdelaR) | Estadistica de replicas y comparacion de metodos (t-Student pareada/independiente), calculos volumetricos y estandarizacion analitica. |
| **`CROMAEQ.py`** | Cromatografia, Kps y Gravimetria | Parametros cromatograficos ($k', N, H, \alpha, R_s$), solubilidad molar a partir de $K_{ps}$ con efecto de ion comun y factor gravimetrico ($FG$). |
| **`ESTEREO.py`** | Estereoquimica Organica | Calculo de IDH avanzado, maximo de estereoisomeros teoricos ($2^n$) y calculo de exceso enantiomerico ($\%ee$). |
| **`ESPECTRO.py`** | Espectroscopia y Soluciones | Ley de Beer-Lambert universal (Absorbancia, Epsilon, Transmitancia) y planificador de diluciones seriadas para curvas de calibrado. |
| **`FISQUIM.py`** | Fisicoquimica y Termodinamica | Gases reales de Van der Waals vs gas ideal, factor de compresibilidad $Z$, propiedades coligativas (presion osmotica, crioscopia, ebulloscopia) y Clausius-Clapeyron. |
| **`RADIOMG.py`** | Fisica Radiologica e Imagenologia | Decaimiento radiactivo y actividad, blindaje ($HVL, TVL, \mu$), ley de inversa del cuadrado, RMN (frecuencia de Larmor y senal Spin-Echo $T_1/T_2$) y Ultrasonido/Doppler. |
| **`OPTMEC.py`** | Biofisica, Optica y Mecanica | Ecuacion de Goldman-Hodgkin-Katz ($V_m$), lentes delgadas, Ley de Snell, angulo critico y de Brewster, choques 1D y Relatividad Especial (factor de Lorentz $\gamma$). |
| **`MATEMAT.py`** | Matematica y Algebra Vectorial | Vectores en $\mathbb{R}^3$ (modulos, producto escalar, angulo y producto cruz), regresion lineal por minimos cuadrados ($m, b, r, R^2$) con interpolacion y cuadraticas complejas. |
| **`ALGEBRA.py`** | Algebra Lineal y Sistemas 3x3 | Resolucion de sistemas $3\times 3$ por Regla de Cramer mostrando todos los determinantes, autovalores/autovectores, polinomio caracteristico e inversa $2\times 2$ y distancia punto-plano. |
| **`CALCULO.py`** | Calculo Diferencial, Integral y EDO | Derivadas de orden 1, 2 y 3 ($f', f'', f'''$), recta tangente, polinomio de Taylor, integracion numerica por Simpson 1/3 y Trapecios, y solver de EDOs por Runge-Kutta 4 (RK4). |
| **`LABMATH.py`** | Laboratorio y Metodos Numericos | Propagacion automatica de errores experimentales ($\pm \Delta x$) y resolucion iterativa de la ecuacion trascendente de Kepler ($M = E - e \sin E$) por Newton-Raphson. |
| **`CONST.py`** | Constantes y Conversor Universal | Tabla de constantes fisicas y astronomicas fundamentales, conversor de fotones ($\text{nm} \leftrightarrow \text{eV} \leftrightarrow \text{Hz} \leftrightarrow \text{J}$), presion ($\text{atm}, \text{Pa}, \text{mmHg}, \text{bar}$) y actividad ($\text{Ci} \leftrightarrow \text{Bq}$). |
| **`DASH.py`** | Dashboard Grafico (ti_draw) | Interfaz grafica en modo oscuro (320x240 px) para simulacion de elipses orbitales de Kepler con telemetria en pantalla y graficador de curvas de saturacion de Michaelis-Menten. |

## Instalacion y Uso en la TI-84 Evo

1. Conectar la calculadora a la PC mediante cable USB-C (asegurandose de estar en la pantalla principal de la calculadora y no dentro de la app de Python).
2. Ingresar a **[TI Connect Evo](https://connectevo.ti.com/)** desde un navegador basado en Chromium.
3. Hacer clic en **Enviar Archivos** -> **Enviar a la calculadora** y seleccionar los archivos `.py`.
4. En la calculadora, presionar **`[prgm]`** -> **Python App** (o el boton de inicio **`[on]`** -> **Python**).
5. Seleccionar el script deseado en el *File Manager* y presionar **`[Y=]` (`f1` / `RUN`)** para ejecutarlo.
6. Para regresar al listado de programas desde la consola, presionar **`[zoom]` (`f3` / `FILES`)**. Para salir de Python, presionar **`[2nd]` + `[mode]` (`quit`)**.
