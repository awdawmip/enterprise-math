def A_recurrence_prefix(N: int):
    vals = [1]
    a = 1
    for n in range(N-1):
        num = a * 6 * (2*n+1) * (3*n+1) * (3*n+2)
        den = (n+1)**3
        assert num % den == 0
        a = num // den
        vals.append(a)
    return vals


def R_recurrence(p: int, m: int) -> int:
    mod = p**3
    base = 108*m
    inv = pow(base, -1, mod)
    vals = A_recurrence_prefix(p)
    s = 0
    power = 1
    for n, a in enumerate(vals):
        s = (s + (6*n + 1) * (a % mod) * power) % mod
        power = (power * inv) % mod
    return s
