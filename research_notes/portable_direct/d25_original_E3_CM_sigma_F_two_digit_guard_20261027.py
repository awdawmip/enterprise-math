#!/usr/bin/env python3
"""D25 original E3 signed CM + sigma-F two-digit algebraic discrimination.

Exact external-model arithmetic in (Z/373^2)[T]/(T^2-2).
Checks TWO constructed Frobenius-compatible operators with identical determinant,
same two-step square and same signed original E3 CM covariance but different
mod-p lower-left / image-line ports. They are NOT native H0/B0 measurements.
"""
P = 373
MOD = P * P

def add(a, b):
    return ((a[0] + b[0]) % MOD, (a[1] + b[1]) % MOD)

def neg(a):
    return ((-a[0]) % MOD, (-a[1]) % MOD)

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % MOD,
            (a[0] * b[1] + a[1] * b[0]) % MOD)

def scale(a, k):
    return (a[0] * k % MOD, a[1] * k % MOD)

def sigma(a):
    return (a[0], -a[1] % MOD)

def matmul(a, b):
    return [[add(mul(a[i][0], b[0][j]),
                 mul(a[i][1], b[1][j])) for j in range(2)] for i in range(2)]

def matsigma(a):
    return [[sigma(x) for x in row] for row in a]

def det(a):
    return sub(mul(a[0][0], a[1][1]), mul(a[0][1], a[1][0]))

def check():
    zero, one, p = (0, 0), (1, 0), (P, 0)
    identity_p = [[p, zero], [zero, p]]
    u = 89697
    assert (u * u + 3) % MOD == 0

    lam = scale((4, -1), pow(72, -1, MOD))
    lam_bar = sigma(lam)
    n = mul(lam, lam_bar)
    assert n == (7 * pow(2592, -1, MOD) % MOD, 0)

    theta_11 = scale((0, 1), u)
    theta_12 = scale((1, -2), u * pow(18, -1, MOD))
    theta = [[theta_11, theta_12], [zero, neg(theta_11)]]
    assert matmul(theta, theta) == [[((-6) % MOD, 0), zero],
                                     [zero, ((-6) % MOD, 0)]]

    # Algebraically constructed two possibilities (not original native data).
    a0 = [[lam, sub(p, n)], [one, neg(lam_bar)]]
    a1 = [[scale(lam, P), sub(one, scale(n, P))],
          [p, neg(scale(lam_bar, P))]]
    for a in (a0, a1):
        assert matmul(theta, a) == matmul(a, matsigma(theta))
        assert matmul(a, matsigma(a)) == identity_p
        assert det(a) == (MOD - P, 0)
        assert any(x[k] % P for row in a for x in row for k in (0, 1))
        assert all(x % P == 0 for x in det(a))

    assert a0[1][0] == one
    assert a1[1][0] == p
    assert a0[1][0] != a1[1][0]
    assert a1[0][1][0] % P == 1

    # The source's signed second column is essential.
    broken = [[lam, sub(p, n)], [one, lam_bar]]
    assert matmul(theta, broken) != matmul(broken, matsigma(theta))

    print("p", P, "mod", MOD, "u", u)
    print("lambda", lam, "sigma(lambda)", lam_bar, "Norm(lambda)", n)
    print("A0", a0)
    print("A1", a1)
    print("same determinant", det(a0), "same square", identity_p)
    print("PASS: exact constructed counterexample to scalar/square-only original-CM operator identification")
    print("AUTHOR_SIDE_UNREVIEWED; NATIVE_H0B0_NOT_EXECUTED; LIFT_OPEN")

if __name__ == "__main__":
    check()
