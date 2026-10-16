from funciones import CASOS_DE_PRUEBA

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x1 = f(x1)
        f_x0 = f(x0)
        
        if f_x1 - f_x0 == 0:
            return None, i, None 
            
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x2 - x1)
        
        if error < tol or abs(f(x2)) < tol:
            return x2, i + 1, error
            
        x0 = x1
        x1 = x2
        
    return x1, max_iter, error

print("=== MÉTODO DE LA SECANTE ===")
for nombre, caso in CASOS_DE_PRUEBA.items():
    print(f"\n{caso['categoria']} -> {caso['expresion']}")
    
    raiz, iteraciones, error = secante(caso["f"], caso["x0"], caso["x1"])
    
    if raiz is not None:
        print(f"Raíz: {raiz:.6f} | Iteraciones: {iteraciones} | Error: {error:.2e}")
    else:
        print("Resultado: Falló (división por cero).")