from funciones import CASOS_DE_PRUEBA

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None, 0, None 

    c = a
    for i in range(max_iter):
        c_old = c
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        error = abs(c - c_old)
        
        if error < tol or abs(f(c)) < tol:
            return c, i + 1, error
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return c, max_iter, error

print("=== MÉTODO DE FALSA POSICIÓN ===")
for nombre, caso in CASOS_DE_PRUEBA.items():
    print(f"\n{caso['categoria']} -> {caso['expresion']}")
    
    if caso["intervalo"] is None:
        print("Resultado: No aplica (no tiene intervalo definido).")
        continue
        
    a, b = caso["intervalo"]
    raiz, iteraciones, error = falsa_posicion(caso["f"], a, b)
    
    if raiz is not None:
        print(f"Raíz: {raiz:.6f} | Iteraciones: {iteraciones} | Error: {error:.2e}")
    else:
        print("Resultado: Falló (no hay cambio de signo en el intervalo).")