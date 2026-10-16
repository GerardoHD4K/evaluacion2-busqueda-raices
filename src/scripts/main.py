import os
import csv
import sys

# Evitar la creacion de __pycache__
sys.dont_write_bytecode = True

import numpy as np
import matplotlib.pyplot as plt

from funciones import CASOS_DE_PRUEBA
from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from secante import secante
from newton_raphson import newton_raphson
from newton_raphson_mejorado import newton_raphson_mejorado

# Directorios de salida
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

TOL = 1e-6
MAX_ITER = 100


def ejecutar_metodos(datos):
    return {
        "Biseccion": biseccion(datos["f"], datos["intervalo"], TOL, MAX_ITER),
        "Falsa Posicion": falsa_posicion(datos["f"], datos["intervalo"], TOL, MAX_ITER),
        "Punto Fijo": punto_fijo(datos["g"], datos["x0"], TOL, MAX_ITER),
        "Secante": secante(datos["f"], datos["x0"], datos["x1"], TOL, MAX_ITER),
        "Newton-Raphson": newton_raphson(datos["f"], datos["df"], datos["x0"], TOL, MAX_ITER),
        "NR Mejorado": newton_raphson_mejorado(datos["f"], datos["df"], datos["d2f"], datos["x0"], TOL, MAX_ITER),
    }


def main():
    resumen_filas = []
    resultados_globales = {}

    print("Iniciando")

    for nombre_caso, datos in CASOS_DE_PRUEBA.items():
        f = datos["f"]
        rango = datos["rango_grafico"]

        # 1. Exportar CSV con columnas
        x_vals = np.linspace(rango[0], rango[1], 200)
        y_vals = f(x_vals)
        datos_csv = np.column_stack((x_vals, y_vals))
        ruta_csv_func = os.path.join(DATA_DIR, f"{nombre_caso.lower()}_datos.csv")
        np.savetxt(
            ruta_csv_func,
            datos_csv,
            delimiter=",",
            header="x,f(x)",
            comments="",
            fmt="%.6f"
        )

        # Ejecutar los 6 metodos
        resultados = ejecutar_metodos(datos)
        resultados_globales[nombre_caso] = resultados

        # Raiz de referencia
        raiz_ref = resultados["NR Mejorado"][0]

        for metodo, (raiz, iters, hist_err, conv, estado) in resultados.items():
            err_final = hist_err[-1] if hist_err else None
            resumen_filas.append([
                nombre_caso,
                datos["expresion"],
                metodo,
                f"{raiz:.6f}" if raiz is not None else "No aplica",
                iters,
                f"{err_final:.6f}" if err_final is not None else "No aplica",
                estado
            ])

        # 2. Grafica: Funcion con raiz marcada
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f"f(x) = {datos['expresion']}", color="royalblue", linewidth=2)
        plt.axhline(0, color="black", linestyle="--", linewidth=1, label="Eje x (y=0)")

        if raiz_ref is not None:
            plt.scatter(
                [raiz_ref], [f(raiz_ref)],
                color="crimson", zorder=5, s=70,
                label=f"Raiz aprox {raiz_ref:.6f}"
            )
            if nombre_caso == "Poli_Doble":
                plt.annotate(
                    "Tangencia al eje x (raiz doble)",
                    xy=(raiz_ref, 0),
                    xytext=(raiz_ref - 0.7, 0.4),
                    arrowprops=dict(arrowstyle="->", color="crimson")
                )

        plt.title(f"Funcion: {datos['categoria']}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(ASSETS_DIR, f"funcion_{nombre_caso.lower()}.png"), dpi=150)
        plt.close()

        # 3. Grafica: Convergencia |error| vs iteracion
        plt.figure(figsize=(8, 5))
        for metodo, (raiz, iters, hist_err, conv, estado) in resultados.items():
            if len(hist_err) > 0:
                iteraciones_eje = np.arange(1, len(hist_err) + 1)
                errores_seguros = np.maximum(np.array(hist_err), 1e-16)
                plt.plot(iteraciones_eje, errores_seguros, marker="o", markersize=4, label=f"{metodo} ({iters} it.)")

        plt.yscale("log")
        plt.axhline(TOL, color="gray", linestyle=":", label=f"Tolerancia ({TOL})")
        plt.title(f"Convergencia |error| vs Iteracion - {datos['categoria']}")
        plt.xlabel("Iteracion")
        plt.ylabel("|Error| (escala logaritmica)")
        plt.grid(True, which="both", alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(ASSETS_DIR, f"convergencia_{nombre_caso.lower()}.png"), dpi=150)
        plt.close()

    # 4. Guardar CSV resumen de convergencia
    ruta_resumen = os.path.join(DATA_DIR, "resumen_convergencia.csv")
    with open(ruta_resumen, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Caso", "Funcion", "Metodo", "Raiz", "Iteraciones", "Error_Final", "Estado"])
        writer.writerows(resumen_filas)

    # 5. Grafica: Resumen de iteraciones por metodo y funcion
    nombres_casos = list(CASOS_DE_PRUEBA.keys())
    metodos_nombres = ["Biseccion", "Falsa Posicion", "Punto Fijo", "Secante", "Newton-Raphson", "NR Mejorado"]
    x_pos = np.arange(len(nombres_casos))
    ancho = 0.13

    plt.figure(figsize=(12, 6))
    for idx, metodo in enumerate(metodos_nombres):
        iters_metodo = [resultados_globales[c][metodo][1] for c in nombres_casos]
        desplazamiento = (idx - len(metodos_nombres) / 2) * ancho + ancho / 2
        plt.bar(x_pos + desplazamiento, iters_metodo, width=ancho, label=metodo)

    plt.xticks(x_pos, nombres_casos)
    plt.ylabel("Numero de Iteraciones")
    plt.title("Resumen Comparativo de Iteraciones por Metodo y Funcion")
    plt.grid(axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "resumen_iteraciones.png"), dpi=150)
    plt.close()

    print("Procesamiento completado con exito.")
    print(f"Datasets exportados en: {DATA_DIR}")
    print(f"Graficas PNG guardadas en: {ASSETS_DIR}")


if __name__ == "__main__":
    main()