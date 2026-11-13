# 🧮 TI-84 Evo - Scientific & Engineering Python Suite

Colección de scripts interactivos en **CircuitPython / MicroPython** diseñados para la calculadora **Texas Instruments TI-84 Evo**. Automatiza el despeje de variables, pasos intermedios y verificación de resultados para exámenes y laboratorios universitarios.

## 📦 Módulos Incluidos

| Script | Área / Materia | Herramientas y Cálculos |
| :--- | :--- | :--- |
| **`ASTRO.py`** | Astronomía y Mecánica Orbital | Velocidad orbital/escape, período de Kepler ($T$), radio de Schwarzschild, óptica instrumental ($f/\#$, aumento, Dawes, Rayleigh, pupila) y paralaje/magnitudes. |
| **`ASTRO2.py`** | Astrofísica y Cosmología | Cuerpo negro estelar (Wien, Stefan-Boltzmann, $L/L_\odot$), Redshift relativista ($z$), Ley de Hubble y transformación Ecuatorial a Horizontal + Masa de Aire ($X$). |
| **`BIOTECH.py`** | Biotecnología y Química Analítica | Buffers (Henderson-Hasselbalch), cinética enzimática de Michaelis-Menten + Lineweaver-Burk, Ley de Beer-Lambert, diluciones y crecimiento celular ($\mu, t_d$). |
| **`BIOQUIM.py`** | Bioquímica y Biología Molecular | Energía libre de Gibbs ($\Delta G'$ real y $K'_{eq}$), potencial de Nernst, pureza y concentración de ADN/ARN ($A_{260}/A_{280}$) y $T_m$ / $\%GC$ de primers PCR. |
| **`BIOLOGIA.py`** | Biología, Genética y Ecología | Equilibrio de Hardy-Weinberg ($p, q, p^2, 2pq, q^2$), test de $\chi^2$ para cruzas genéticas, conteo en cámara de Neubauer e índices de Shannon ($H'$) y Simpson. |
| **`ORGANICA.py`** | Química Orgánica | Índice de Deficiencia de Hidrógeno (IDH) y composición centesimal, fórmula empírica desde análisis elemental, polarimetría ($[\alpha]_D$, $\%ee$) y cinética de Arrhenius. |
| **`RADIOMG.py`** | Física Radiológica e Imagenología | Decaimiento radiactivo y actividad, blindaje ($HVL, TVL, \mu$), ley de inversa del cuadrado, RMN (frecuencia de Larmor y señal Spin-Echo $T_1/T_2$) y Ultrasonido/Doppler. |
| **`OPTMEC.py`** | Biofísica, Óptica y Mecánica | Ecuación de Goldman-Hodgkin-Katz ($V_m$), lentes delgadas, Ley de Snell, ángulo crítico y de Brewster, choques 1D y Relatividad Especial (factor de Lorentz $\gamma$). |
| **`MATEMAT.py`** | Matemática y Álgebra Vectorial | Vectores en $\mathbb{R}^3$ (módulos, producto escalar, ángulo y producto cruz), regresión lineal por mínimos cuadrados ($m, b, r, R^2$) con interpolación y cuadráticas complejas. |
| **`LABMATH.py`** | Laboratorio y Métodos Numéricos | Propagación automática de errores experimentales ($\pm \Delta x$) y resolución iterativa de la ecuación trascendente de Kepler ($M = E - e \sin E$) por Newton-Raphson. |

## 🚀 Cómo cargar los scripts en la TI-84 Evo

1. Conectar la calculadora a la PC mediante cable USB-C.
2. Ingresar a **[TI Connect™ Evo](https://connectevo.ti.com/)** desde un navegador basado en Chromium.
3. Hacer clic en **Enviar Archivos** -> **Enviar a la calculadora** y seleccionar los archivos `.py`.
4. Elegir **Ubicación: Archivo** (Archive/Flash) para almacenarlos de forma permanente.
5. En la calculadora, presionar **`[apps]`** -> **Python**, seleccionar el script y presionar **`[y=]` (`Run`)**.
