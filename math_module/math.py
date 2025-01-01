# math.py - Un module mathématique complet en Python pur

PI = 3.141592653589793
E = 2.718281828459045
inf = float('inf')
nan = float('nan')
tau = 2 * PI  # Tau est 2 * Pi

# Fonctions mathématiques de base
def ceil(x):
    """Retourne le plus petit entier supérieur ou égal à x."""
    if x == int(x):
        return int(x)
    return int(x) + 1 if x > 0 else int(x)

def floor(x):
    """Retourne le plus grand entier inférieur ou égal à x."""
    if x == int(x):
        return int(x)
    return int(x) if x > 0 else int(x) - 1

def factorial(n):
    """Retourne la factorielle de n (n!)."""
    if n < 0:
        raise ValueError("Factorielle non définie pour les nombres négatifs.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def exp(x):
    """Retourne e^x, calculé par la série de Taylor."""
    result = 1
    term = 1
    n = 1
    while abs(term) > 1e-10:  # Tolérance pour la précision
        term *= x / n
        result += term
        n += 1
    return result

def log(x, base=E):
    """Retourne le logarithme de x dans la base spécifiée (base par défaut est e)."""
    if x <= 0:
        raise ValueError("Le logarithme est défini uniquement pour x > 0.")
    return n_log(x) / n_log(base)

def n_log(x):
    """Retourne le logarithme naturel de x, calculé par la méthode de Newton."""
    if x <= 0:
        raise ValueError("Le logarithme naturel est défini uniquement pour x > 0.")
    n = 1.0
    while abs(n * exp(n) - x) > 1e-10:
        n = n - (exp(n) - x) / exp(n)
    return n

def sqrt(x):
    """Retourne la racine carrée de x."""
    if x < 0:
        raise ValueError("La racine carrée n'est pas définie pour les nombres négatifs.")
    return exp(log(x) / 2)

def pow(x, y):
    """Retourne x^y (x à la puissance y)."""
    return exp(y * log(x))

def sin(x):
    """Retourne le sinus de x, calculé par la série de Taylor."""
    result = 0
    term = x
    n = 1
    while abs(term) > 1e-10:
        result += term
        term *= -x * x / ((2 * n) * (2 * n + 1))
        n += 1
    return result

def cos(x):
    """Retourne le cosinus de x, calculé par la série de Taylor."""
    result = 1
    term = 1
    n = 1
    while abs(term) > 1e-10:
        term *= -x * x / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result

def tan(x):
    """Retourne la tangente de x."""
    return sin(x) / cos(x)

def radians(degrees):
    """Convertit des degrés en radians."""
    return degrees * PI / 180

def degrees(radians):
    """Convertit des radians en degrés."""
    return radians * 180 / PI

# Fonctions trigonométriques inverses
def asin(x):
    """Retourne l'arc sinus (inverse de sin) de x, calculé à partir de la série de Taylor."""
    if x < -1 or x > 1:
        raise ValueError("asin est défini uniquement pour x dans l'intervalle [-1, 1].")
    return atan(x / (sqrt(1 - x * x)))  # Utilisation de l'arc tangente pour calculer l'arc sinus

def acos(x):
    """Retourne l'arc cosinus (inverse de cos) de x, calculé à partir de la série de Taylor."""
    if x < -1 or x > 1:
        raise ValueError("acos est défini uniquement pour x dans l'intervalle [-1, 1].")
    return PI / 2 - asin(x)  # Utilisation de asin pour calculer l'arc cosinus

def atan(x):
    """Retourne l'arc tangente (inverse de tan) de x, calculé par la série de Taylor."""
    result = 0
    term = x
    n = 1
    while abs(term) > 1e-10:
        result += term
        term *= -x * x * (2 * n - 1) / (2 * n)
        n += 1
    return result

# Fonctions avancées
def gcd(x, y):
    """Retourne le plus grand commun diviseur (GCD) de x et y."""
    while y:
        x, y = y, x % y
    return x

def comb(n, k):
    """Retourne le nombre de combinaisons de n éléments pris k à la fois."""
    if k > n:
        raise ValueError("k ne peut pas être supérieur à n.")
    return factorial(n) // (factorial(k) * factorial(n - k))

def perm(n, k):
    """Retourne le nombre de permutations de n éléments pris k à la fois."""
    if k > n:
        raise ValueError("k ne peut pas être supérieur à n.")
    return factorial(n) // factorial(n - k)

def fsum(iterable):
    """Retourne la somme des éléments de l'itérable, en prenant en compte la précision."""
    total = 0.0
    for value in iterable:
        total += value
    return total

# Exemple d'utilisation
if __name__ == "__main__":
    print("PI =", PI)
    print("e =", E)
    print("inf =", inf)
    print("nan =", nan)
    print("tau =", tau)
    print("sin(0) =", sin(0))
    print("cos(PI / 2) =", cos(PI / 2))
    print("sqrt(16) =", sqrt(16))
    print("exp(1) =", exp(1))
    print("log(10) =", log(10))
    print("factorial(5) =", factorial(5))
    print("pow(2, 3) =", pow(2, 3))
    print("gcd(60, 48) =", gcd(60, 48))
    print("comb(5, 3) =", comb(5, 3))
    print("perm(5, 3) =", perm(5, 3))
    print("fsum([1.0, 2.0, 3.0]) =", fsum([1.0, 2.0, 3.0]))
    print("asin(0.5) =", asin(0.5))
    print("acos(0.5) =", acos(0.5))
    print("atan(1) =", atan(1))
