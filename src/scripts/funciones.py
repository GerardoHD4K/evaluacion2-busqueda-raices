import numpy as np

#Polinomica Raiz Simple f(x)=x^3-x-2
def f_poli_simple(x):
    return x**3 - x - 2.0
#Primera derivada
def df_poli_simple(x):
    return 3.0 * x**2 - 1.0
#Segunda derivada
def d2f_poli_simple(x):
    return 6.0 * x
#Despeje para punto fijo
def g_poli_simple(x):
    return np.cbrt(x + 2.0)

#Polinomica Raiz Doble f(x)=(x-2)^2
def f_poli_doble(x):
    return (x - 2.0)**2
#Primera derivada
def df_poli_doble(x):
    return 2.0 * (x - 2.0)
#Segunda derivada
def d2f_poli_doble(x):
    if np.isscalar(x):
        return 2.0
    return np.full_like(x, 2.0, dtype=float)
#Despeje para punto fijo
def g_poli_doble(x):
    return (x**2 + 4.0) / 4.0

#Logaritmica f(x)=ln(x)+x-4
def f_logaritmica(x):
    return np.log(x) + x - 4.0
#Primera derivada
def df_logaritmica(x):
    return (1.0 / x) + 1.0
#Segunda derivada
def d2f_logaritmica(x):
    return -1.0 / (x**2)
def g_logaritmica(x):
    return 4.0 - np.log(x)

#Exponencial f(x)=e^(-x)-x
def f_exponencial(x):
    return np.exp(-x) - x
#Primera derivada
def df_exponencial(x):
    return -np.exp(-x) - 1.0
#Segunda derivada
def d2f_exponencial(x):
    return np.exp(-x)
#Despeje para punto fijo
def g_exponencial(x):
    return np.exp(-x)

#Trigonometrica f(x)=cos(x)-x
def f_trigonometrica(x):
    return np.cos(x) - x
#Primera derivada 
def df_trigonometrica(x):
    return -np.sin(x) - 1.0
#Segunda derivada
def d2f_trigonometrica(x):
    return -np.cos(x)
#Despeje para punto fijo
def g_trigonometrica(x):
    return np.cos(x)

#Mixta f(x)=sqrt(x)-cos(x)
def f_mixta(x):
    return np.sqrt(x) - np.cos(x)
#Primera derivada
def df_mixta(x):
    return (1.0 / (2.0 * np.sqrt(x))) + np.sin(x)
#Segunda derivada
def d2f_mixta(x):
    return (-1.0 / (4.0 * (x**1.5))) + np.cos(x)
#Despeje punto fijo
def g_mixta(x):
    return np.cos(x)**2

# Caso de prueba y Parametros
CASOS_DE_PRUEBA = {
    "Poli_Simple": {
        "categoria": "Polinómica (raíz simple)",
        "expresion":"f(x) = x^3 - x - 2",
        "f": f_poli_simple,
        "df": df_poli_simple,
        "d2f": d2f_poli_simple,
        "g": g_poli_simple,
        "intervalo": [1.0, 2.0],
        "x0": 1.5,
        "x1": 2.0,
        "rango_grafico": [0.5, 2.3]
    },
    "Poli_Doble": {
        "categoria": "Polinómica (raíz doble)",
        "expresion": "f(x) = (x - 2)^2",
        "f": f_poli_doble,
        "df": df_poli_doble,
        "d2f": d2f_poli_doble,
        "g": g_poli_doble,
        "intervalo": None,
        "x0": 1.2,
        "x1": 1.5,
        "rango_grafico": [0.8, 3.2]
    },
    "Logaritmica": {
        "categoria": "Logarítmica",
        "expresion": "f(x) = ln(x) + x - 4",
        "f": f_logaritmica,
        "df": df_logaritmica,
        "d2f": d2f_logaritmica,
        "g": g_logaritmica,
        "intervalo": [2.0, 3.0],
        "x0": 2.5,
        "x1": 3.0,
        "rango_grafico": [1.8, 3.2]
    },
    "Exponencial": {
        "categoria": "Exponencial",
        "expresion": "f(x) = e^(-x) - x",
        "f": f_exponencial,
        "df": df_exponencial,
        "d2f": d2f_exponencial,
        "g": g_exponencial,
        "intervalo": [0.0, 1.0],
        "x0": 0.5,
        "x1": 1.0,
        "rango_grafico": [-0.2, 1.2]
    },
    "Trigonometrica": {
        "categoria": "Trigonométrica",
        "expresion": "f(x) = cos(x) - x",
        "f": f_trigonometrica,
        "df": df_trigonometrica,
        "d2f": d2f_trigonometrica,
        "g": g_trigonometrica,
        "intervalo": [0.0, 1.0],
        "x0": 0.5,
        "x1": 1.0,
        "rango_grafico": [-0.2, 1.2]
    },
    "Mixta": {
        "categoria": "Mixta",
        "expresion": "f(x)=sqrt(x)-cos(x)",
        "f": f_mixta,
        "df": df_mixta,
        "d2f": d2f_mixta,
        "g": g_mixta,
        "intervalo": [0.1, 1.0],
        "x0": 0.5,
        "x1": 1.0,
        "rango_grafico": [0.05, 1.2]
    },
}
