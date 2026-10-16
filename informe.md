# Informe de Laboratorio Evaluado 2: Busqueda de Raices y Analisis de Convergencia
# Gerardo Pinilla, Matias Araya
## 1. Ambiente Controlado y Resumen de Resultados Experimentales

Para garantizar la reproducibilidad de las pruebas, cada funcion definida en funciones.py fue evaluada bajo una tolerancia de 1e-6 y un tope maximo de 100 iteraciones, verificando previamente el cumplimiento del Teorema de Bolzano (f(a)*f(b) < 0) o la condicion de tangencia al eje x.

### 1.1. Parametros y Verificacion de Rango por Funcion

- Poli_Simple: f(x) = x^3 - x - 2
  - Intervalo [a, b]: [1.0, 2.0]
  - Estimaciones iniciales: x0 = 1.5, x1 = 2.0
  - Demostracion de raiz en el rango: Cambio de signo cumplido (Bolzano), f(1)*f(2) = (-2)*(4) = -8 < 0
  - Graficos de respaldo: src/assets/funcion_poli_simple.png y src/assets/convergencia_poli_simple.png

- Poli_Doble: f(x) = (x - 2)^2
  - Intervalo [a, b]: No aplica
  - Estimaciones iniciales: x0 = 1.2, x1 = 1.5
  - Demostracion de raiz en el rango: Sin cambio de signo (f(x) >= 0 en todo su dominio), tangencia al eje x demostrada en el punto (2, 0)
  - Graficos de respaldo: src/assets/funcion_poli_doble.png y src/assets/convergencia_poli_doble.png

- Logaritmica: f(x) = ln(x) + x - 4
  - Intervalo [a, b]: [2.0, 3.0]
  - Estimaciones iniciales: x0 = 2.5, x1 = 3.0
  - Demostracion de raiz en el rango: Cambio de signo cumplido (Bolzano), f(2)*f(3) = (-1.306853)*(0.098612) < 0
  - Graficos de respaldo: src/assets/funcion_logaritmica.png y src/assets/convergencia_logaritmica.png

- Exponencial: f(x) = e^(-x) - x
  - Intervalo [a, b]: [0.0, 1.0]
  - Estimaciones iniciales: x0 = 0.5, x1 = 1.0
  - Demostracion de raiz en el rango: Cambio de signo cumplido (Bolzano), f(0)*f(1) = (1.0)*(-0.632121) < 0
  - Graficos de respaldo: src/assets/funcion_exponencial.png y src/assets/convergencia_exponencial.png

- Trigonometrica: f(x) = cos(x) - x
  - Intervalo [a, b]: [0.0, 1.0]
  - Estimaciones iniciales: x0 = 0.5, x1 = 1.0
  - Demostracion de raiz en el rango: Cambio de signo cumplido (Bolzano), f(0)*f(1) = (1.0)*(-0.459698) < 0
  - Graficos de respaldo: src/assets/funcion_trigonometrica.png y src/assets/convergencia_trigonometrica.png

- Mixta: f(x) = sqrt(x) - cos(x)
  - Intervalo [a, b]: [0.1, 1.0]
  - Estimaciones iniciales: x0 = 0.5, x1 = 1.0
  - Demostracion de raiz en el rango: Cambio de signo cumplido (Bolzano), f(0.1)*f(1.0) = (-0.678766)*(0.459698) < 0
  - Graficos de respaldo: src/assets/funcion_mixta.png y src/assets/convergencia_mixta.png


### 1.2. Resultados de Convergencia Obtenidos (src/data/resumen_convergencia.csv)

### Caso 1: Poli_Simple -> f(x) = x^3 - x - 2
- Biseccion: Raiz = 1.521380 | Iteraciones = 20 | Error Final = 0.000001 | Estado = Converge
- Falsa Posicion: Raiz = 1.521379 | Iteraciones = 12 | Error Final = 0.000001 | Estado = Converge
- Punto Fijo: Raiz = 1.521380 | Iteraciones = 7 | Error Final = 0.000000 | Estado = Converge
- Secante: Raiz = 1.521380 | Iteraciones = 4 | Error Final = 0.000009 | Estado = Converge
- Newton-Raphson: Raiz = 1.521380 | Iteraciones = 2 | Error Final = 0.000359 | Estado = Converge
- NR Mejorado: Raiz = 1.521380 | Iteraciones = 2 | Error Final = 0.000356 | Estado = Converge

### Caso 2: Poli_Doble -> f(x) = (x - 2)^2
- Biseccion: Raiz = No aplica | Iteraciones = 0 | Error Final = No aplica | Estado = No aplica
- Falsa Posicion: Raiz = No aplica | Iteraciones = 0 | Error Final = No aplica | Estado = No aplica
- Punto Fijo: Raiz = 1.963027 | Iteraciones = 100 | Error Final = 0.000348 | Estado = Tope de iteraciones alcanzado
- Secante: Raiz = 1.999043 | Iteraciones = 13 | Error Final = 0.000591 | Estado = Converge
- Newton-Raphson: Raiz = 1.999219 | Iteraciones = 10 | Error Final = 0.000781 | Estado = Converge
- NR Mejorado: Raiz = 2.000000 | Iteraciones = 1 | Error Final = 0.800000 | Estado = Converge

### Caso 3: Logaritmica -> f(x) = ln(x) + x - 4
- Biseccion: Raiz = 2.926271 | Iteraciones = 19 | Error Final = 0.000002 | Estado = Converge
- Falsa Posicion: Raiz = 2.926271 | Iteraciones = 4 | Error Final = 0.000008 | Estado = Converge
- Punto Fijo: Raiz = 2.926271 | Iteraciones = 14 | Error Final = 0.000001 | Estado = Converge
- Secante: Raiz = 2.926271 | Iteraciones = 3 | Error Final = 0.000005 | Estado = Converge
- Newton-Raphson: Raiz = 2.926271 | Iteraciones = 3 | Error Final = 0.000004 | Estado = Converge
- NR Mejorado: Raiz = 2.926271 | Iteraciones = 3 | Error Final = 0.000006 | Estado = Converge

### Caso 4: Exponencial -> f(x) = e^(-x) - x
- Biseccion: Raiz = 0.567143 | Iteraciones = 20 | Error Final = 0.000001 | Estado = Converge
- Falsa Posicion: Raiz = 0.567143 | Iteraciones = 7 | Error Final = 0.000001 | Estado = Converge
- Punto Fijo: Raiz = 0.567143 | Iteraciones = 22 | Error Final = 0.000001 | Estado = Converge
- Secante: Raiz = 0.567144 | Iteraciones = 3 | Error Final = 0.000363 | Estado = Converge
- Newton-Raphson: Raiz = 0.567143 | Iteraciones = 2 | Error Final = 0.000832 | Estado = Converge
- NR Mejorado: Raiz = 0.567143 | Iteraciones = 2 | Error Final = 0.000870 | Estado = Converge

### Caso 5: Trigonometrica -> f(x) = cos(x) - x
- Biseccion: Raiz = 0.739085 | Iteraciones = 20 | Error Final = 0.000001 | Estado = Converge
- Falsa Posicion: Raiz = 0.739085 | Iteraciones = 5 | Error Final = 0.000007 | Estado = Converge
- Punto Fijo: Raiz = 0.739085 | Iteraciones = 34 | Error Final = 0.000001 | Estado = Converge
- Secante: Raiz = 0.739085 | Iteraciones = 4 | Error Final = 0.000002 | Estado = Converge
- Newton-Raphson: Raiz = 0.739085 | Iteraciones = 3 | Error Final = 0.000057 | Estado = Converge
- NR Mejorado: Raiz = 0.739085 | Iteraciones = 3 | Error Final = 0.000069 | Estado = Converge

### Caso 6: Mixta -> f(x) = sqrt(x) - cos(x)
- Biseccion: Raiz = 0.641714 | Iteraciones = 20 | Error Final = 0.000001 | Estado = Converge
- Falsa Posicion: Raiz = 0.641714 | Iteraciones = 4 | Error Final = 0.000011 | Estado = Converge
- Punto Fijo: Raiz = 0.639911 | Iteraciones = 100 | Error Final = 0.003683 | Estado = Tope de iteraciones alcanzado
- Secante: Raiz = 0.641715 | Iteraciones = 3 | Error Final = 0.000304 | Estado = Converge
- Newton-Raphson: Raiz = 0.641715 | Iteraciones = 2 | Error Final = 0.001961 | Estado = Converge
- NR Mejorado: Raiz = 0.641714 | Iteraciones = 2 | Error Final = 0.000944 | Estado = Converge


## 2. Preguntas de Convergencia (Seccion 6)

### 1. ¿Que metodo convergio en menos iteraciones en cada funcion? ¿Por que?
- En Poli_Simple (x^3 - x - 2): Empataron Newton-Raphson y NR Mejorado con 2 iteraciones (raiz 1.521380), seguidos por Secante con 4 iteraciones.
- En Poli_Doble ((x - 2)^2): Gano NR Mejorado con 1 sola iteracion (llegando directo a la raiz exacta 2.000000), superando ampliamente a Newton-Raphson (10 iteraciones) y Secante (13 iteraciones).
- En Logaritmica (ln(x) + x - 4): Empataron Secante, Newton-Raphson y NR Mejorado con 3 iteraciones (raiz 2.926271), seguidos de cerca por Falsa Posicion con 4 iteraciones.
- En Exponencial (e^(-x) - x): Empataron Newton-Raphson y NR Mejorado con 2 iteraciones (raiz 0.567143), seguidos por Secante con 3 iteraciones.
- En Trigonometrica (cos(x) - x): Empataron Newton-Raphson y NR Mejorado con 3 iteraciones (raiz 0.739085), seguidos por Secante con 4 iteraciones.
- En Mixta (sqrt(x) - cos(x)): Empataron Newton-Raphson y NR Mejorado con 2 iteraciones (raiz 0.641714), seguidos por Secante con 3 iteraciones.

Por que: Porque los metodos de la familia de Newton utilizan la informacion exacta de la pendiente local f'(x) mediante la serie de Taylor, proyectando la recta tangente directo hacia el cruce con el eje x y alcanzando convergencia cuadratica (orden p = 2). En la raiz doble, NR Mejorado incorpora ademas la curvatura mediante la segunda derivada f''(x), compensando que f'(2) = 0 y evitando que el paso se reduzca a la mitad como le ocurre al Newton-Raphson estandar.

### 2. ¿Que orden de convergencia tiene cada metodo y como se refleja en el grafico |error| vs iteracion?
- Orden Lineal (p = 1): Corresponde a Biseccion, Falsa Posicion y Punto Fijo. En los graficos convergencia_*.png (con el eje vertical en escala logaritmica), la convergencia lineal se visualiza como una linea recta descendente con pendiente constante. En Biseccion el error cae a la mitad por iteracion (0.5^n), formando una diagonal suave que tarda entre 19 y 20 iteraciones en cruzar el umbral de 1e-6.
- Orden Superlineal (p = 1.618): Corresponde al metodo de la Secante. En la grafica logaritmica se aprecia como una curva concava hacia abajo cuya pendiente se vuelve mas pronunciada en cada paso, convergiendo en apenas 3 a 4 iteraciones en raices simples.
- Orden Cuadratico (p = 2): Corresponde a Newton-Raphson y NR Mejorado (en raices simples, y NR Mejorado tambien en raices multiples). Dado que el error nuevo es proporcional al cuadrado del error anterior, en escala logaritmica se observa como una caida abrupta casi vertical, duplicando aproximadamente el numero de decimales correctos en cada paso y alcanzando la tolerancia en 1 a 3 iteraciones.

### 3. ¿Que metodos requieren un intervalo con cambio de signo y cuales no?
- Si requieren un intervalo [a, b] con cambio de signo f(a)*f(b) < 0: Biseccion y Falsa Posicion. Son metodos cerrados que dependen del Teorema de Bolzano para garantizar que al menos una raiz quede atrapada dentro del intervalo en cada sub-division.
- No requieren intervalo con cambio de signo: Punto Fijo (parte de una estimacion inicial x0 y evalua x_sig = g(x_act)), Secante (parte de dos estimaciones iniciales x0 y x1 sin exigir que encierren la raiz), Newton-Raphson (parte de un unico punto inicial x0) y NR Mejorado (parte de un unico punto inicial x0). Todos estos son metodos abiertos.

### 4. En la funcion que toca el eje x (raiz doble): ¿que metodos fallan o no aplican y cual se comporta mejor? ¿Por que?
En el caso Poli_Doble f(x) = (x - 2)^2:
- No aplican: Biseccion y Falsa Posicion (Iteraciones = 0, Estado = No aplica). Como la parabola solo toca tangencialmente el eje x en x = 2 y rebota hacia arriba manteniendo (x - 2)^2 >= 0 en todo su dominio, no existe ningun par [a, b] donde f(a)*f(b) < 0.
- Fallan por estancamiento (tope de iteraciones): Punto Fijo con g(x) = (x^2 + 4)/4 alcanza el tope de 100 iteraciones quedandose en 1.963027 (Error Final = 0.000348). Esto ocurre porque la derivada del despeje evaluada en la raiz es |g'(2)| = 1, violando la condicion de contraccion estricta (|g'(x)| < 1) y provocando una convergencia sublineal extremadamente lenta.
- Convergen pero se degradan de orden: Newton-Raphson sube de su promedio de 2 iteraciones a 10 iteraciones (1.999219), y Secante sube a 13 iteraciones (1.999043). Ambos pierden su orden cuadratico/superlineal y pasan a comportarse de forma lineal porque al acercarse a x = 2, tanto f(x) como f'(x) = 2(x - 2) tienden a 0. Para una raiz de multiplicidad m = 2, el error en Newton se reduce solo a la mitad en cada paso, avanzando igual de lento que una biseccion.
- El que mejor se comporta: NR Mejorado, que converge a 2.000000 en 1 iteracion. Al incluir la segunda derivada f''(x) en su formula x_sig = x_act - (f(x)*f'(x)) / ([f'(x)]^2 - f(x)*f''(x)), cancela algebraicamente la multiplicidad de la raiz y llega al valor exacto en un solo paso desde cualquier x0 distinto de 2.

### 5. ¿Como influyen el intervalo inicial y la estimacion inicial en la cantidad de iteraciones y en si el metodo converge?
Para comprobarlo numericamente sobre Poli_Simple f(x) = x^3 - x - 2 (raiz en 1.521380), se variaron los parametros de entrada:
- Efecto de mover el intervalo [a, b] en Biseccion:
 Con el intervalo original [1.0, 2.0] (ancho 1.0) tardo 20 iteraciones. Al estrechar el intervalo a [1.4, 1.6] (ancho 0.2) bajo a 18 iteraciones. Al ampliar el intervalo a [0.0, 5.0] (ancho 5.0) subio a 23 iteraciones. En Biseccion siempre converge si se cumple Bolzano, y el numero de iteraciones responde a log2((b - a) / tol), por lo que multiplicar el ancho por 5 solo anade 3 iteraciones mas.
- Efecto de mover la estimacion inicial x0 en metodos abiertos (Newton-Raphson y Punto Fijo):
 Con la semilla original x0 = 1.5, Newton-Raphson tardo 2 iteraciones. Al alejar la semilla a x0 = 5.0, Newton-Raphson subio a 7 iteraciones. Al situar la semilla en x0 = 0.58 (muy cerca del punto critico donde la derivada f'(x) = 3x^2 - 1 vale 0, en x = 0.577350), la tangente es casi horizontal, disparando la primera iteracion lejos de la raiz y elevando el costo a 18 iteraciones. Si cae exactamente donde la derivada es 0, el metodo falla por division por cero.
 En Punto Fijo, para la funcion Mixta (sqrt(x) - cos(x)), el despeje g(x) = cos^2(x) tiene derivada |g'(0.641714)| cercana a 0.959 (muy proxima a 1). Al estar tan cerca de 1, las oscilaciones amortiguan muy lento y desde x0 = 0.5 llega al tope de 100 iteraciones (0.639911) sin alcanzar un error menor a 1e-6.

### 6. ¿Que metodo recomiendan segun el tipo de funcion, considerando el compromiso entre velocidad y robustez?
- Funciones polinomicas, exponenciales y trigonometricas con raiz simple y derivada sencilla: Se recomienda Newton-Raphson (2 a 3 iteraciones), ya que su costo analitico es bajo y ofrece velocidad cuadratica.
- Funciones con sospecha de raices multiples o tangencia al eje horizontal: Se recomienda NR Mejorado (promedio de 2.17 iteraciones y 1 iteracion en Poli_Doble), siendo el unico metodo que no sufre degradacion ni inaplicabilidad cuando f'(r) = 0.
- Funciones complejas o compuestas (como Logaritmica o Mixta) cuando no se desea derivar analiticamente: Se recomienda Secante (3 a 4 iteraciones en raices simples), logrando practicamente la misma velocidad que Newton-Raphson pero evaluando unicamente f(x).
- Situaciones donde la robustez y la seguridad de convergencia son prioritarias sobre la velocidad: Se recomienda Falsa Posicion (4 a 12 iteraciones) o Biseccion (19 a 20 iteraciones). Aunque son mas lentos, garantizan converger siempre que exista cambio de signo en [a, b], evitando el riesgo de estancamiento observado en Punto Fijo.


## 3. Conclusion Argumentada (Seccion 9)

### 1. ¿Que metodo elegirian para cada tipo de funcion y por que (velocidad vs robustez)?
A la luz de los datos obtenidos en resumen_convergencia.csv y reflejados en src/assets/resumen_iteraciones.png, existe una diferencia clara entre eficiencia computacional y garantia de convergencia. En las cinco funciones de raiz simple (Poli_Simple, Logaritmica, Exponencial, Trigonometrica y Mixta), Newton-Raphson y NR Mejorado lideraron en velocidad con entre 2 y 3 iteraciones, seguidos por Secante con 3 a 4 iteraciones. En contraste, Biseccion demando de forma fija entre 19 y 20 iteraciones, mientras que Falsa Posicion logro reducir ese esfuerzo cerrado a un rango de 4 a 12 iteraciones (promedio de 6.40). Por su parte, Punto Fijo demostro ser el metodo menos robusto del estudio, con un promedio de 46.17 iteraciones y fallando por tope de 100 pasos tanto en Poli_Doble (1.963027) como en Mixta (0.639911). En conclusion: se elige Newton-Raphson cuando se dispone de f'(x), Secante cuando solo se tiene acceso a f(x) y se busca rapidez, y Falsa Posicion o Biseccion cuando se requiere certidumbre matematica de no divergencia.

### 2. ¿Que ocurrio en la raiz doble y que dice eso sobre tener raiz frente a cambiar de signo?
El experimento con f(x) = (x - 2)^2 demostro con datos que tener una raiz (f(r) = 0) no equivale a cambiar de signo. El cambio de signo en un intervalo continuo (Teorema de Bolzano) es una condicion suficiente, pero no necesaria, para que exista un cero. Como la curva solo toca el eje x en x = 2 y rebota manteniendo su signo positivo (verificable en src/assets/funcion_poli_doble.png), Biseccion y Falsa Posicion no aplican. Al mismo tiempo, la tangencia implica que f'(2) = 0, lo que provoco que Punto Fijo se estancara en 100 iteraciones y que Newton-Raphson (10 iteraciones) y Secante (13 iteraciones) perdieran su aceleracion y cayeran a un regimen lineal lento. Unicamente NR Mejorado, al incorporar la segunda derivada f''(x), restauro el orden cuadratico y hallo la raiz exacta 2.000000 en 1 iteracion.

### 3. ¿Como cambio el numero de iteraciones al mover el intervalo o la estimacion inicial?
Los ensayos de sensibilidad confirmaron que en los metodos cerrados el impacto de ampliar el intervalo es logaritmico y controlado: pasar de [1.0, 2.0] a [0.0, 5.0] en Poli_Simple solo incremento a Biseccion de 20 a 23 iteraciones, y reducirlo a [1.4, 1.6] lo bajo a 18 iteraciones. En cambio, en los metodos abiertos la sensibilidad frente a la semilla x0 es critica y no lineal: en Newton-Raphson, alejar x0 de 1.5 a 5.0 aumento las iteraciones de 2 a 7, y acercar x0 a 0.58 (proximo al punto de derivada nula x = 0.577350) disparo el costo a 18 iteraciones, demostrando que una estimacion inicial cercana a un extremo local puede anular por completo la ventaja de velocidad de los metodos abiertos.