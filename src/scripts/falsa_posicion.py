def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None, 0, None # Falla si no hay cambio de signo

    c = a
    for i in range(max_iter):
        c_old = c
        # Fórmula de falsa posición
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        
        error = abs(c - c_old)
        if error < tol or abs(f(c)) < tol:
            return c, i + 1, error
            
        # Actualización del intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return c, max_iter, error

