import numpy as np
from funciones import CASOS_DE_PRUEBA # Cambia 'funciones' por el nombre de tu archivo

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None, 0, [] 

    c = a
    historial_error = []
    
    for i in range(max_iter):
        c_old = c
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        error = abs(c - c_old)
        historial_error.append(error)
        
        if error < tol or abs(f(c)) < tol:
            return c, i + 1, historial_error
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return c, max_iter, historial_error

print("=== MÉTODO DE FALSA POSICIÓN ===")
for nombre, caso in CASOS_DE_PRUEBA.items():
    print(f"\n{caso['categoria']} -> {caso['expresion']}")
    
    if caso["intervalo"] is None:
        print("Resultado: No aplica (no tiene intervalo definido).")
        continue
        
    a, b = caso["intervalo"]
    raiz, iteraciones, errores = falsa_posicion(caso["f"], a, b)
    
    if raiz is not None and errores:
        print(f"Raíz: {raiz:.6f} | Iteraciones: {iteraciones} | Error final: {errores[-1]:.2e}")
    else:
        print("Resultado: Falló (no hay cambio de signo en el intervalo).")