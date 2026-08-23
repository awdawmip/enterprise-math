from math import gcd, isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def norms(a, b):
    return a * a + b * b, a * a - a * b + b * b


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    x = pow(a, (p - 1) // 2, p)
    return 1 if x == 1 else -1


def perfect_square(n):
    if n < 0:
        return None
    r = isqrt(n)
    return r if r * r == n else None


def pointed(a, b):
    assert gcd(a, b) == 1
    N, C = norms(a, b)
    H = N * C
    assert gcd(b, H) == 1
    r = (-a * pow(b, -1, H)) % H
    return N, C, H, r


def check_identities(B=80):
    for a in range(1, B + 1):
        for b in range(1, B + 1):
            N, C = norms(a, b)
            u, v = a + b, a - b
            assert 2 * N == u * u + v * v
            assert 4 * C == u * u + 3 * v * v
            assert u * u == 3 * N - 2 * C
            assert v * v == 2 * C - N
            assert gcd(N, C) == gcd(a, b) ** 2
            if gcd(a, b) == 1:
                N, C, H, r = pointed(a, b)
                assert ((r * r + 1) * (r * r + r + 1)) % H == 0
                assert gcd(H, r * r + 1) == N
                assert gcd(H, r * r + r + 1) == C
                rinv = pow(r, -1, H)
                e = (-(r + rinv)) % H
                assert (e * e - e) % H == 0
                assert gcd(e, H) == N
                assert gcd((e - 1) % H, H) == C
                U, V = 3 * N - 2 * C, 2 * C - N
                su, sv = perfect_square(U), perfect_square(V)
                assert su is not None and sv is not None
                aa = (su + sv) // 2
                bb = (su - sv) // 2
                assert sorted((aa, bb)) == sorted((a, b))
    return True


def dual_cells(B=120):
    for a in range(1, B + 1):
        for b in range(1, B + 1):
            if gcd(a, b) != 1:
                continue
            p, q = norms(a, b)
            if p > 3 and q > 3 and is_prime(p) and is_prime(q):
                yield a, b, p, q


def check_dual(B=120):
    for a, b, p, q in dual_cells(B):
        assert q < p < 2 * q
        assert (p % 8, q % 12) in ((1, 1), (5, 7))
        chi = 1 if q % 12 == 1 else -1
        assert legendre(p, q) == chi
        assert legendre(q, p) == chi
        assert legendre(2, p) == chi
        assert legendre(-1, q) == chi

        _, _, H, r = pointed(a, b)
        roots = {pow(r, exponent, H) for exponent in (1, 5, 7, 11)}
        assert len(roots) == 4
        for x in roots:
            assert (x * x + 1) % p == 0
            assert (x * x + x + 1) % q == 0
            assert gcd(H, pow(x, 6, H) + 1) == p
            assert gcd(H, pow(x, 6, H) - 1) == q

        rswap = (-b * pow(a, -1, H)) % H
        assert rswap == pow(r, 11, H) == pow(r, -1, H)
    return True


def primes_upto(n):
    return [p for p in range(2, n + 1) if is_prime(p)]


def corridor_roots(k, p):
    roots = set()
    for t in range(p):
        F = 2 * t * t + 2 * k * t + k * k
        G = t * t + k * t + k * k
        if F % p == 0 or G % p == 0:
            roots.add(t)
    return roots


def check_corridors(K=60, P=97):
    for k in range(1, K + 1, 2):
        for p in primes_upto(P):
            nu = len(corridor_roots(k, p))
            if p == 2:
                assert nu == 0
            elif p == 3:
                assert nu == 1
            elif k % p == 0:
                assert nu == 1
            else:
                expected = 2 + legendre(-1, p) + legendre(-3, p)
                assert nu == expected
                assert nu < p
    return True


def check_matching(B=150):
    pts = {(a, b) for a, b, _, _ in dual_cells(B)}
    for a, b in pts:
        degree = 0
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)):
            if (a + da, b + db) in pts:
                degree += 1
        assert degree <= 1
    return True


def main():
    assert check_identities()
    assert check_dual()
    assert check_corridors()
    assert check_matching()
    print('prime-fusion theorem package checker: PASS')


if __name__ == '__main__':
    main()
