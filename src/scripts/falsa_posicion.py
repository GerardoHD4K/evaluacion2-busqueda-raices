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

caso = CASOS_DE_PRUEBA["Poli_Simple"]
a, b = caso["intervalo"]
raiz, iteraciones, error = falsa_posicion(caso["f"], a, b)
print(f"Falsa Posición ({caso['categoria']}):")
print(f"Raíz: {raiz:.6f} | Iteraciones: {iteraciones} | Error: {error:.2e}\n")