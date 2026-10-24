"""Exact author checker for the SOURCE-POLYNOMIAL Hesse reflection pairing.
No crystalline Frobenius, Gauss-Manin H0/B0 matrix, native CM benchmark, or theorem admission.
All computations use integer residues in R=(Z/p^2)[T]/(T^2-2).
"""
from math import comb

PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)


def mul(a, b, modulus):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % modulus,
            (a[0] * b[1] + a[1] * b[0]) % modulus)


def evaluate(coefficients, x, modulus):
    value = (0, 0)
    for coefficient in reversed(coefficients):
        value = mul(value, x, modulus)
        value = ((value[0] + coefficient) % modulus, value[1])
    return value


def derivative(coefficients, modulus):
    return [(k * coefficients[k]) % modulus
            for k in range(1, len(coefficients))]


def check(p):
    assert p >= 13 and p % 24 in (13, 19)
    n = (p - 1) // 3
    q = p * p
    inv = lambda a: pow(a, -1, q)
    c = [1]
    for k in range(n):
        c.append(c[-1] * (3*k + 1) * (3*k + 2)
                 * inv(9*(k+1)**2) % q)

    # B(X)=A(1-X) from binomial expansion; independent of A(u) pair conjugation.
    B = [(-1)**j * sum(c[k] * comb(k, j)
           for k in range(j, n+1)) % q for j in range(n+1)]
    u = (2*inv(4) % q, -inv(4) % q)
    x_half = (inv(2), 0)
    A_u = evaluate(c, u, q)
    Ap_u = evaluate(derivative(c, q), u, q)
    B_u = evaluate(B, u, q)
    Bp_u = evaluate(derivative(B, q), u, q)
    left = mul(A_u, Bp_u, q)
    right = mul(Ap_u, B_u, q)
    wronskian = ((left[0]-right[0]) % q,
                 (left[1]-right[1]) % q)
    weighted = mul(wronskian, (inv(8), 0), q)

    # Source forcing F(X)=X^n B(X)-(1-X)^n A(X).
    F = [0] * (2*n + 1)
    for j, bj in enumerate(B):
        F[n+j] = (F[n+j] + bj) % q
    for j in range(n+1):
        signbinomial = (-1)**j * comb(n, j)
        for k, ck in enumerate(c):
            F[j+k] = (F[j+k] - signbinomial*ck) % q
    # All j+1 <= 2*n+1 < p, hence inverses are units.
    integral_coefficients = [0] + [
        coefficient * inv(j+1) % q for j, coefficient in enumerate(F)
    ]
    at_u = evaluate(integral_coefficients, u, q)
    at_half = evaluate(integral_coefficients, x_half, q)
    integral = ((at_u[0]-at_half[0]) % q,
                (at_u[1]-at_half[1]) % q)
    Cp = ((p+1) * c[n] * inv(9)) % q
    A_half = evaluate(c, x_half, q)[0]
    Ap_half = evaluate(derivative(c, q), x_half, q)[0]

    # Weighted Green identity independently reconstructs Wronskian.
    via_green = ((p*Cp*integral[0]
                  - A_half*Ap_half*inv(2)) % q,
                 (p*Cp*integral[1]) % q)
    assert weighted == via_green, (p, weighted, via_green)
    assert integral[1] == 0 and weighted[1] == 0

    a, b = A_u
    e, d = Ap_u
    assert a % p == 0 and b % p == 0 and e % p == 0
    assert Ap_half % p == 0 and weighted[0] % p == 0
    v, w = b // p % p, e // p % p
    normalized = weighted[0] // p % p
    assert normalized == v * (d % p) * pow(2, -1, p) % p

    if p == 373:
        assert A_u == (112646, 57442)
        assert Ap_u == (0, 130607)
        assert (v, w, d % p) == (154, 0, 57)
        assert (weighted, normalized) == ((106678, 0), 286)
        assert (Cp % p, A_half, Ap_half, integral) == (
            40, 9736, 129058, (35047, 0))
    return (p, v, w, d % p, normalized)


if __name__ == "__main__":
    for row in (check(p) for p in PRIMES):
        print("p=%d v=%d w=%d d=%d pairing=%d" % row)
    print("8/8 exact source-pair/Green checks passed; author-only.")
