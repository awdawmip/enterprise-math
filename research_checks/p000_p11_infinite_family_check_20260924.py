from fractions import Fraction as F
from math import gcd, isqrt

A2 = F(-2)
A4 = F(2)


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    if P == Q:
        m = (3 * x1 * x1 + 2 * A2 * x1 + A4) / (2 * y1)
    else:
        m = (y2 - y1) / (x2 - x1)
    x3 = m * m - A2 - x1 - x2
    return x3, -y1 + m * (x1 - x3)


def mul(n, P):
    R = None
    Q = P
    while n:
        if n & 1:
            R = add(R, Q)
        Q = add(Q, Q)
        n //= 2
    return R


def count_mod_p(p):
    n = 1
    for x in range(p):
        rhs = (x**3 - 2 * x * x + 2 * x) % p
        n += sum(1 for y in range(p) if y * y % p == rhs)
    return n


def sq(n):
    z = isqrt(n)
    return z if z * z == n else None


def recovered_root_gcd(k, A, B, C, P, Q, D, U, V):
    d = int(k * D)
    mu = int(k * U)
    nu = int(k * V)
    p = k * P
    q = k * Q
    b0 = k * C
    roots = []
    for z in (p, b0, q):
        roots += [abs((d + z) // 2), abs((d - z) // 2)]
    roots += [abs(mu) // 2, abs(nu) // 2]
    g = 0
    for z in roots:
        g = gcd(g, z)
    return g


assert count_mod_p(3) == 6
assert count_mod_p(5) == 8

R = (F(1), F(1))
assert mul(3, R) == (F(49, 9), F(-287, 27))
assert mul(4, R) == (F(961, 400), F(21359, 8000))

strict = []
for n in range(1, 41):
    x, y = mul(n, R)
    a = sq(x.numerator)
    b = sq(x.denominator)
    assert a is not None and b is not None
    assert gcd(a, b) == 1 and a % 2 == 1

    # Equivalent exact rational test for 2 < x < 2 + sqrt(2).
    if not (x > 2 and (x - 2) * (x - 2) < 2):
        continue

    r = a * a - b * b
    s = b * b
    assert r > s > 0 and gcd(r, s) == 1 and (r - s) % 2 == 1
    even = r if r % 2 == 0 else s
    assert even % 4 == 0

    A = r * r - s * s
    B = 2 * r * s
    C = r * r + s * s
    h = sq(C)
    assert h is not None
    assert r + s == a * a

    P = A + B
    Q = B - A
    assert Q > 0
    assert P == a**4 - 2 * b**4
    assert Q == -a**4 + 4 * a * a * b * b - 2 * b**4

    X = (a**4 + 2 * b**4) ** 2
    W = 8 * a**3 * b**3 * h * (a**4 + 2 * b**4)
    assert W * W == X * (X - P * P) * (X - Q * Q)

    S = P + Q
    T = F(S) * (X - P * Q) / (X + P * Q)
    Yq = F(4 * S * P * Q) * W / (X + P * Q) ** 2
    D = Yq / (2 * T)
    U = (T + F(P * P - Q * Q, T)) / 2
    V = (T - F(P * P - Q * Q, T)) / 2

    assert D > 0 and U > 0 and V > 0 and D < Q
    assert U * U + D * D == P * P
    assert V * V + D * D == Q * Q

    strict.append((n, a, b, r, s, h, A, B, C, P, Q, D, U, V))

assert [z[0] for z in strict] == [4, 13, 23, 31, 40]

z = strict[0]
_, a, b, r, s, h, A, B, C, P, Q, D, U, V = z

den = 1
for f in (D, U, V):
    den = den * f.denominator // gcd(den, f.denominator)
assert den == 767326053623109361

k = 2 * den
d = int(k * D)
mu = int(k * U)
nu = int(k * V)
x0 = k * B
y0 = k * A
b0 = k * C

assert x0 * x0 + y0 * y0 == b0 * b0
assert d * d + mu * mu == (x0 + y0) ** 2
assert d * d + nu * nu == (x0 - y0) ** 2
assert d % 2 == k % 2 and mu % 2 == 0 and nu % 2 == 0
assert recovered_root_gcd(k, A, B, C, P, Q, D, U, V) == 1

assert (x0, y0, b0) == (
    688751865732102962433600,
    237442908685242206886562,
    728531583004032197926562,
)
assert (d, mu, nu) == (
    377120747320472741536080,
    845941311261274825126562,
    247910702978256584099362,
)

print(
    "PASS P000 P11 infinite-family replay:",
    "F3=6",
    "F5=8",
    "strict_n<=40=",
    [z[0] for z in strict],
    "n4_root_gcd=1",
)
