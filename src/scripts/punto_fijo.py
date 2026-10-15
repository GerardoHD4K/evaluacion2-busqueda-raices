def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x_actual = x0
    
    for i in range(max_iter):
        x_siguiente = g(x_actual)
        error = abs(x_siguiente - x_actual)
        
        if error < tol:
            return x_siguiente, i + 1, error
            
        x_actual = x_siguiente
        
    return x_actual, max_iter, error

