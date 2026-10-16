import numpy as np
import numpy as np
from funciones import CASOS_DE_PRUEBA

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x_actual = float(x0)
    historial_error = []
    for i in range(1, max_iter + 1):
        x_siguiente = g(x_actual)
        error = np.abs(x_siguiente - x_actual)
        historial_error.append(error)

        if error < tol:
            return x_siguiente, i, historial_error, True, "Converge"

        x_actual = x_siguiente

    return x_actual, max_iter, historial_error, False, "Tope de iteraciones alcanzado"

if __name__ == "__main__":
    print("=== MÉTODO DE PUNTO FIJO ===")
    for nombre, datos in CASOS_DE_PRUEBA.items():
        raiz, iters, errores, conv, estado = punto_fijo(datos["g"], datos["x0"])
        print(f"{nombre:<15} Raiz: {raiz:.6f} Iter: {iters:<3} Error: {errores[-1]:.6f} {estado}")