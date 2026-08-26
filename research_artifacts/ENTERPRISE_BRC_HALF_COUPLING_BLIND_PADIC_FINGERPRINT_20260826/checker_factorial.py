from math import factorial


def A_factorial(n: int) -> int:
    return factorial(2*n) * factorial(3*n) // (factorial(n) ** 5)


def R_factorial(p: int, m: int) -> int:
    mod = p**3
    base = 108*m
    inv = pow(base, -1, mod)
    s = 0
    power = 1
    for n in range(p):
        a = A_factorial(n)
        s = (s + (6*n + 1) * (a % mod) * power) % mod
        power = (power * inv) % mod
    return s
