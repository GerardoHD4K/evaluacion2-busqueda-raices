import numpy as np
from funciones import CASOS_DE_PRUEBA

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x_actual = x0
    historial_error = []
    
    for i in range(max_iter):
        x_siguiente = g(x_actual)
        error = abs(x_siguiente - x_actual)
        historial_error.append(error)
        
        if error < tol:
            return x_siguiente, i + 1, historial_error
            
        x_actual = x_siguiente
        
    return x_actual, max_iter, historial_error

print("=== MÉTODO DE PUNTO FIJO ===")
for nombre, caso in CASOS_DE_PRUEBA.items():
    print(f"\n{caso['categoria']} -> {caso['expresion']}")
    
    raiz, iteraciones, errores = punto_fijo(caso["g"], caso["x0"])
    if errores:
        print(f"Raíz: {raiz:.6f} | Iteraciones: {iteraciones} | Error final: {errores[-1]:.2e}")