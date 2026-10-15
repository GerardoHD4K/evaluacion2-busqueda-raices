def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x1 = f(x1)
        f_x0 = f(x0)
        
        if f_x1 - f_x0 == 0:
            return None, i, None # Evitar división por cero
            
        # Fórmula de la secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        error = abs(x2 - x1)
        
        if error < tol or abs(f(x2)) < tol:
            return x2, i + 1, error
            
        # Actualización de valores
        x0 = x1
        x1 = x2
        
    return x1, max_iter, error

