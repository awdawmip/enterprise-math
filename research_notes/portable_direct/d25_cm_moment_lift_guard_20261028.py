"""Original-216 CM Legendre moment lift: integer p-adic checks, no native claim."""
from math import comb


def add(a, b, q):
    c = [0] * max(len(a), len(b))
    for j, x in enumerate(a): c[j] = (c[j] + x) % q
    for j, x in enumerate(b): c[j] = (c[j] + x) % q
    return c


def mul(a, b, q):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i + j] = (c[i + j] + x * y) % q
    return c


def sc(a, k, q): return [k * x % q for x in a]
def sub(a, b, q): return add(a, sc(b, -1, q), q)
def um(a, q): return sub(a, [0] + a, q)
def ev(a, x, q):
    y = 0
    for c in reversed(a): y = (y * x + c) % q
    return y


def divD(a, q):
    rem = a[:]
    b = [0] * (len(a) - 1)
    for j in range(len(a) - 1, 0, -1):
        b[j - 1] = rem[j] * pow(2, -1, q) % q
        rem[j - 1] = (rem[j - 1] + b[j - 1]) % q
    assert rem[0] == 0
    return b


def integ(a, q):
    return sum(x * pow(2 * j + 1, -1, q) for j, x in enumerate(a)) % q


def check(p):
    assert p % 6 == 1 and p > 3 and all(p % j for j in range(2, int(p**.5) + 1))
    m = (p - 1) // 6; q = p * p
    G = [(-1)**(m-j) * comb(2*m, m-j) * comb(2*m+2*j, 2*m)
         * pow(4, -m, q) % q for j in range(m+1)]
    GP = [j * G[j] % q for j in range(1, len(G))]
    x = pow(2, -1, q)
    a = ev(G, x, q); d = ev(GP, x, q); c = G[0]
    assert c % p
    Ga = G[:]; Ga[0] = (Ga[0] - a) % q
    R = divD(Ga, q)
    Hn = sc(um(GP, q), 2, q); Hn[0] = (Hn[0] - d) % q
    C = sub(sc(divD(Hn, q), 6, q), R, q)
    num = add(sc(mul(G, G, q), -1, q), sc(um(mul(G, GP, q), q), 12, q), q)
    num[0] = (num[0] + a*a - 6*a*d) % q
    Q = divD(num, q)
    K = integ(sc(um(mul(R, GP, q), q), 2, q), q)
    I = integ(Q, q)
    lam = (integ(C, q) - 6 * pow(c, -1, q)) % q
    assert K == (1 - a * pow(c, -1, q)) % q
    assert I == (6 + a * lam) % q
    base = add(sc(mul(G, R, q), -1, q), sc(um(mul(R, GP, q), q), 12, q), q)
    assert not any(sub(Q, add(base, sc(C, a, q), q), q))
    if p % 24 in (13, 19):
        assert a % p == 0 and d % p != 0 and K % p == 1 and I % p == 6
    return (p, a, c % p, d % p, K, I, lam % p,
            -(a//p) * pow(d, -1, p) % p if a % p == 0 and d % p else None)


def original_weighted_216(p):
    """Independent original term ratio, full n=0..p-1, mod p^3."""
    q = p**3
    t = 1
    result = 0
    for n in range(p):
        result = (result + (6*n+1)*t) % q
        if n + 1 < p:
            t = (t * (2*n+1) * (3*n+1) * (3*n+2)
                 * pow(36*(n+1)**3, -1, q)) % q
    return result


def main():
    primes = [7,13,19,31,37,43,61,67,73,79,97,103,109,127,139,
              151,157,163,181,193,199,211,229,277,283,307,331,349,373]
    for p in primes: check(p)
    assert check(13) == (13,26,2,12,157,6,0,2)
    assert check(19) == (19,76,8,17,172,348,14,2)
    assert check(373) == (373,17158,38,158,94743,122350,72,283)
    assert original_weighted_216(373) == 373
    assert (check(373)[5] * pow(6, -1, 373**2)) % (373**2) == 66768
    print('PASS_D25_CM_EXACT_MOMENT_LIFT_29_PRIMES')
    for p in (13,19,373): print(check(p))

if __name__ == '__main__': main()
