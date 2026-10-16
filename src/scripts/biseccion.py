import numpy as np
from funciones import CASOS_DE_PRUEBA

def biseccion (f, intervalo, tol=1e-6, max_inter=100):
    if intervalo is None:
        return None, 0, [], False, "No aplica"
    a = float(intervalo[0])
    b = float(intervalo[1])
    fa = f(a)
    fb = f(b)

#Aplicamos Teorema de Bolzano para cambio de signo en el intervalo
    if fa * fb >=0:
        return None, 0, [], False, "Falla Bolzano"

    historial_error = []
    x_ant = a

    for i in range(1, max_inter + 1):
        xr = (a + b) / 2.0
        fxr = f(xr)

        #Calculo del error
        if i ==1:
            error = np.abs(b-a) / 2.0
        else:
            error = np.abs(xr - x_ant)

        historial_error.append(error)

        #Criterio de parada
        if np.abs(fxr) < tol or error < tol:
            return xr, i, historial_error, True, "Converge"

        #Elegir el subintervalo
        if fa * fxr < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr
        x_ant  = xr
    return xr, max_inter, historial_error, False, "Tope de iteraciones alcanzado"

if __name__ == "__main__":
    print ("Prueba Metodo Biseccion")
    for nombre, datos in CASOS_DE_PRUEBA.items():
        raiz, iters, errores, conv, estado = biseccion(datos["f"], datos["intervalo"])

        if raiz is not None:
            err_final = errores[-1]
            print(f"{nombre:<15} Raiz: {raiz:.6f} Iter:{iters:<3} Error:{err_final:.6f} {estado}")
        else: 
            print(f"{nombre:<15} Raiz {'---':<8} Iter: {iters:<3} Error: {'---':<8} {estado}")

