import numpy as np
from funciones import CASOS_DE_PRUEBA

def newtom_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x_act = float(x0)
    historial_error = []

    for i in range(1, max_iter + 1):
        fx = f(x_act)
        dfx = df(x_act)

        #Evitart division por cero si la pendiente es nula
        if np.abs(dfx) < 1e-12:
            return x_act, i, historial_error, False, "Falla"

        #Newton raphson
        x_sig = x_act - (fx / dfx)
        error = np.abs(x_sig - x_act)
        historial_error.append(error)

        #Criterio de parada
        if np.abs(f(x_sig)) < tol or error < tol:
            return x_sig, i, historial_error, True, "Converge"
        x_act = x_sig
    return x_act, max_iter, historial_error, False, "Tope de iteraciones alcanzado"

if __name__ == "__main__":
    print("Prueba Metodo Newton Raphson")
    for nombre, datos in CASOS_DE_PRUEBA.items():
        raiz, iters, errores, conv, estado = newtom_raphson(datos["f"], datos["df"], datos["x0"] )

        err_final = errores[-1] if errores else 0.0
        print(f"{nombre:<15} Raiz:{raiz:.6} Iter:{iters:<3} Error:{err_final:.6f} {estado}")