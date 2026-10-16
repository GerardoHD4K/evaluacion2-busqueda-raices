import numpy as np
from funciones import CASOS_DE_PRUEBA

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    x0, x1 = float(x0), float(x1)
    historial_error = []
    for i in range(1, max_iter + 1):
        f_x1 = f(x1)
        f_x0 = f(x0)

        if np.abs(f_x1 - f_x0) < 1e-12:
            return None, i, historial_error, False, "División por cero"

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = np.abs(x2 - x1)
        historial_error.append(error)

        if error < tol or np.abs(f(x2)) < tol:
            return x2, i, historial_error, True, "Converge"

        x0 = x1
        x1 = x2

    return x1, max_iter, historial_error, False, "Tope de iteraciones alcanzado"

if __name__ == "__main__":
    print("=== MÉTODO DE LA SECANTE ===")
    for nombre, datos in CASOS_DE_PRUEBA.items():
        raiz, iters, errores, conv, estado = secante(datos["f"], datos["x0"], datos["x1"])
        if raiz is not None:
            print(f"{nombre:<15} Raiz: {raiz:.6f} Iter: {iters:<3} Error: {errores[-1]:.6f} {estado}")
        else:
            print(f"{nombre:<15} Raiz: {'---':<8} Iter: {iters:<3} Error: {'---':<8} {estado}")