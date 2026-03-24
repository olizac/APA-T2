"""
Name: Oliwia Zacharska

Unit tests:

>>> [n for n in range(2, 50) if esPrimo(n)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""


def _validar(n):
    if not isinstance(n, int) or n <= 1:
        raise TypeError("n must be a natural number greater than 1")


def esPrimo(n):
    """
    Determine if a n is prime.
    """
    _validar(n)

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def primos(n):
    """
    Return all primos less than n.
    """
    _validar(n)
    return tuple(i for i in range(2, n) if esPrimo(i))


def descompon(n):
    """
    Return the prime factorization of a n.
    """
    _validar(n)

    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return tuple(factors)


def mcd_two(a, b):
    """
    mcd of two ns using prime factorization.
    """
    _validar(a)
    _validar(b)

    factors_a = list(descompon(a))
    factors_b = list(descompon(b))

    common = []

    for f in factors_a:
        if f in factors_b:
            common.append(f)
            factors_b.remove(f)

    result = 1
    for f in common:
        result *= f

    return result


def mcm_two(a, b):
    """
    mcm of two ns using prime factorization.
    """
    _validar(a)
    _validar(b)

    factors_a = list(descompon(a))
    factors_b = list(descompon(b))

    result_factors = []

    all_factors = set(factors_a + factors_b)

    for f in all_factors:
        count_a = factors_a.count(f)
        count_b = factors_b.count(f)
        result_factors.extend([f] * max(count_a, count_b))

    result = 1
    for f in result_factors:
        result *= f

    return result


def mcd(*ns):
    """
    mcd of multiple ns.
    """
    if len(ns) < 2:
        raise TypeError

    for n in ns:
        _validar(n)

    result = ns[0]

    for n in ns[1:]:
        result = mcd_two(result, n)

    return result


def mcm(*ns):
    """
    mcm of multiple ns.
    """
    if len(ns) < 2:
        raise TypeError

    for n in ns:
        _validar(n)

    result = ns[0]

    for n in ns[1:]:
        result = mcm_two(result, n)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)