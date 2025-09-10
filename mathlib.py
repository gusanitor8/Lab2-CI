def square(n: int) -> int:
    """
    Retorna el cuadrado de un número.
    """
    return n * n


def factorial(n: int) -> int:
    """
    Retorna el factorial de un número entero positivo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def is_prime(n: int) -> bool:
    """
    Retorna True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a: int, b: int) -> int:
    """
    Retorna el máximo común divisor (MCD) entre dos números.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Retorna el mínimo común múltiplo (MCM) entre dos números.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)