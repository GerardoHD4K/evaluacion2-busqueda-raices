import numpy as np
from funciones import CASOS_DE_PRUEBA

def falsa_posicion(f, intervalo, tol=1e-6, max_iter=100):
    if intervalo is None:
        return None, 0, [], False, "No aplica"
    a, b = float(intervalo[0]), float(intervalo[1])
    if f(a) * f(b) >= 0:
        return None, 0, [], False, "Falla Bolzano"

    c = a
    historial_error = []
    for i in range(1, max_iter + 1):
        c_old = c
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        error = np.abs(c - c_old)
        historial_error.append(error)

        if error < tol or np.abs(f(c)) < tol:
            return c, i, historial_error, True, "Converge"

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, max_iter, historial_error, False, "Tope de iteraciones alcanzado"

if __name__ == "__main__":
    print("=== MÉTODO DE FALSA POSICIÓN ===")
    for nombre, datos in CASOS_DE_PRUEBA.items():
        raiz, iters, errores, conv, estado = falsa_posicion(datos["f"], datos["intervalo"])
        if raiz is not None:
            print(f"{nombre:<15} Raiz: {raiz:.6f} Iter: {iters:<3} Error: {errores[-1]:.6f} {estado}")
        else:
            print(f"{nombre:<15} Raiz: {'---':<8} Iter: {iters:<3} Error: {'---':<8} {estado}")