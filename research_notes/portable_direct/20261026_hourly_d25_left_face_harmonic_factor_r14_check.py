"""Author-only exact mod-p^3 checks for labelled D25 left Hasse face."""
from math import isqrt

def invert(x, q):
    return pow(x % q, -1, q)

def mul(a, b, q):
    out = [0] * 4
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j < 4:
                out[i + j] = (out[i + j] + ai * bj) % q
    return out

def divide_by_linear(c, u, v, q):
    out = [0] * 4
    iv = invert(u, q)
    for j in range(4):
        out[j] = ((c[j] - (v * out[j - 1] if j else 0)) * iv) % q
    return out

def jets(m, p, q):
    f = [1, 0, 0, 0]
    alpha = p * invert(2, q)
    a = b = None
    for r in range(1, p):
        num = mul(f, [r - 1 - m, -1], q)
        num = mul(num, [r - 1 - 2 * m, -2], q)
        f = divide_by_linear(num, r * (r - alpha), -3 * r, q)
        if r == 2 * m:
            a = f[:]
        if r == p - 1:
            b = f[:]
    return a, b

def harmonic(n, q):
    h = [0]
    for k in range(1, n + 1):
        h.append((h[-1] + invert(k, q)) % q)
    return h

def neg_face_delta(m, p, q):
    left = 1 - 2 * m
    eta = 0
    for n in range(0, left, -1):
        w = pow(2, n, q) if n >= 0 else invert(pow(2, -n, q), q)
        eta = ((p - 2 * n) * eta - w) * invert(p - 2 * n + 1, q) % q
    w_left = invert(pow(2, -left, q), q)
    return (w_left - (p - 2 * left) * eta) % q

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def check(p):
    m = (p - 1) // 6
    q = p**3
    a, b = jets(m, p, q)
    h = harmonic(5 * m, q)
    A = (invert(m, q) + 2 * h[2 * m]
         - 6 * sum(invert(2 * u - 1, q) for u in range(m + 1, 3 * m + 1))) % q
    B = (h[m] - h[5 * m - 1] + 2 * h[2 * m] - 2 * h[4 * m - 1]) % q
    assert a[2] == A * a[1] % q
    assert b[3] == B * b[2] % q
    y12 = -2 * m * a[1] * b[2] % q
    y22 = -2 * m * a[2] * b[2] % q
    y13 = -2 * m * a[1] * b[3] % q
    assert y22 == A * y12 % q
    assert y13 == B * y12 % q
    delta = neg_face_delta(m, p, q)
    F_direct = (2 * p * delta * y12
                - p * p * invert(3, q) * delta * (y22 + y13)) % q
    F_factor = delta * y12 * (2 * p - p * p * invert(3, q) * (A + B)) % q
    assert F_direct == F_factor
    return (A + B) % p, (y22 + y13) % p, delta % (p * p), F_direct

def main():
    ps = [p for p in range(7, 998) if p % 6 == 1 and prime(p)]
    exceptional = []
    for p in ps:
        r = check(p)
        if r[0] == 0:
            exceptional.append(p)
        if p == 13:
            assert r == (0, 0, 47, 1872)
        if p == 733:
            assert r == (527, 416, 176653, 46744143)
    assert len(ps) == 80
    print(f"PASS {len(ps)} primes, {5 * len(ps)} exact modular identities")
    print("secondary A+B resonance p<=997:", exceptional)
    print("p13:", check(13))
    print("p733:", check(733))

if __name__ == '__main__':
    main()
