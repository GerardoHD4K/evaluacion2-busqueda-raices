# Evaluacion 2: Busqueda de Raices

Este proyecto contiene la implementacion en Python de seis metodos numericos para encontrar raices de funciones no lineales y comparar su velocidad de convergencia.

## Estructura de carpetas del proyecto

- evaluacion2-busqueda-raices/
  - README.md: Instrucciones completas de instalacion, entorno y ejecucion.
  - requirements.txt: Lista de dependencias del proyecto (numpy y matplotlib).
  - informe.md: Respuestas a las preguntas de convergencia y conclusiones tecnicas.
  - src/
    - data/: Archivos CSV generados con las coordenadas (x, f(x)) y el resumen de convergencia.
    - assets/: Graficos generados en formato PNG (funciones, convergencia y resumen de iteraciones).
    - scripts/: Codigos fuente en Python con la logica de cada metodo.
      - funciones.py: Contiene las 6 funciones de prueba, sus derivadas analiticas, despejes g(x) y parametros iniciales.
      - biseccion.py: Metodo cerrado que divide el intervalo a la mitad aplicando el Teorema de Bolzano.
      - falsa_posicion.py: Metodo cerrado que aproxima la raiz mediante interpolacion lineal (Regula Falsi).
      - punto_fijo.py: Metodo abierto que itera la ecuacion despejada x = g(x).
      - secante.py: Metodo abierto que aproxima la derivada mediante una recta secante con dos puntos (x0, x1).
      - newton_raphson.py: Metodo abierto que utiliza la primera derivada f'(x) para alcanzar convergencia cuadratica.
      - newton_raphson_mejorado.py: Metodo abierto que incorpora la segunda derivada f''(x) para raices multiples o tangencias.
      - main.py: Script orquestador que ejecuta los 6 metodos sobre todas las funciones, exporta los CSV y genera los 13 graficos.

## Configuracion del Entorno Virtual (venv)

bash
git clone https://github.com/GerardoHD4K/evaluacion2-busqueda-raices.git
cd evaluacion2-busqueda-raices