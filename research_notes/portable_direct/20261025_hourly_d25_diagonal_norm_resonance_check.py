"""Author checker: diagonal semilinear top-digit gauge resonance.
Exact Z/p^r[T]/(T^2-2) arithmetic; not native CM or independent review.
"""
Z = (0, 0)
ONE = (1, 0)

def add(a, b, m):
    return ((a[0] + b[0]) % m, (a[1] + b[1]) % m)

def neg(a, m):
    return (-a[0] % m, -a[1] % m)

def mul(a, b, m):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % m,
            (a[0]*b[1] + a[1]*b[0]) % m)

def sigma(a, m):
    return (a[0] % m, -a[1] % m)

def scale(a, k, m):
    return (a[0]*k % m, a[1]*k % m)

def mmul(A, B, m):
    return tuple(tuple(add(mul(A[i][0], B[0][j], m),
                           mul(A[i][1], B[1][j], m), m)
                       for j in range(2)) for i in range(2))

def madd(A, B, m):
    return tuple(tuple(add(A[i][j], B[i][j], m)
                       for j in range(2)) for i in range(2))

def mneg(A, m):
    return tuple(tuple(neg(A[i][j], m) for j in range(2)) for i in range(2))

def msigma(A, m):
    return tuple(tuple(sigma(A[i][j], m) for j in range(2))
                 for i in range(2))

def top(A, q, m):
    return tuple(tuple(scale(A[i][j], q, m)
                       for j in range(2)) for i in range(2))

I = ((ONE, Z), (Z, ONE))
E12 = ((Z, ONE), (Z, Z))

def gauge_eliminates(p, r, a, x):
    mod, q = p**r, p**(r-1)
    C0 = ((a, Z), (Z, ONE))
    X = ((Z, x), (Z, Z))
    C = mmul(C0, madd(I, top(E12, q, mod), mod), mod)
    P = madd(I, top(X, q, mod), mod)
    Pinv = madd(I, mneg(top(X, q, mod), mod), mod)
    transported = mmul(mmul(Pinv, C, mod), msigma(P, mod), mod)
    assert transported == C0
    return C, P, mmul(C, msigma(C, mod), mod)

for p in (13, 19, 373):
    for r in (2, 3):
        # Norm(2+T)=2 and Norm(1)=1: E12 jet is removable.
        gauge_eliminates(p, r, (2, 1), (-4, -1))
        mod, q = p**r, p**(r-1)
        C = madd(I, top(E12, q, mod), mod)
        S = mmul(C, msigma(C, mod), mod)
        assert S[0][1] == (2*q, 0) and S != I

# Previously persisted ordinary-Hesse coefficient, not native Frobenius.
p, mod = 373, 373**2
a = (92060, 21788)
assert (a[0]**2 - 2*a[1]**2) % mod == 122102
C, P, S = gauge_eliminates(p, 2, a, (143, 280))
assert S[0][1] == (22380, 57442)
assert P[0][1] == (53339, 104440)
assert (122102 % p, S[0][1][0]//p, S[0][1][1]//p) == (131, 60, 154)
gauge_eliminates(p, 3, a, (143, 280))
print("PASS: six uniform comparisons, two p=373 Hesse lifts, exact square digits.")
