#!/usr/bin/env python3
"""Exact F_p Laurent certificates for D25 GH-15/GH-16.

Arithmetic uses integers modulo p and four jet coefficients; there is no
floating point, modular zero division, or implicit cancellation of poles.
"""


def primes_below(bound):
    sieve = [True] * bound
    sieve[:2] = [False, False]
    for k in range(2, int(bound**0.5) + 1):
        if sieve[k]:
            for j in range(k * k, bound, k):
                sieve[j] = False
    return [p for p in range(7, bound) if sieve[p] and p % 4 == 3]


def mul(u, v, p):
    degree = len(u) - 1
    return [sum(u[i] * v[k - i] for i in range(k + 1)) % p
            for k in range(degree + 1)]


def factor(u, constant, p, direction):
    """Multiply by (constant+4e)^direction, splitting off e valuation."""
    degree = len(u) - 1
    a = constant % p
    if not a:
        c = (4 if direction == 1 else pow(4, -1, p))
        return [(c * x) % p for x in u], direction
    if direction == 1:
        f = [a, 4] + [0] * (degree - 1)
    else:
        inv = pow(a, -1, p)
        f = [inv * pow((-4 * inv) % p, i, p) % p
             for i in range(degree + 1)]
    return mul(u, f, p), 0


def cyclic_laurent(p, r, z, degree=4):
    """Laurent coefficients of unique GH-13 rational R_z(r+e).

    t_0=1, t_(j+1)=a_z(r+j+e)t_j, R=(sum f t_j)/(z-1).
    For all observed ranks, order is >= -2; retain exponents -2,-1,0,1.
    """
    if z % p in (0, 1):
        raise ValueError("Use a nonzero nonresonant z")
    value = 0
    unit = [1] + [0] * degree
    totals = {}
    for j in range(p):
        if value < -2:
            raise AssertionError((p, r, j, "unexpected pole order"))
        a = (8 * (r + j) + 1) % p
        for k in range(degree + 1):
            exponent = value + k
            if -2 <= exponent <= 1:
                totals[exponent] = (totals.get(exponent, 0) + a * unit[k]
                                    + (8 * unit[k - 1] if k else 0)) % p
        unit = [(c * (z % p)) % p for c in unit]
        for _ in range(3):
            unit, delta = factor(unit, 4 * (r + j) + 1, p, +1)
            value += delta
        for b in (2, 3, 4):
            unit, delta = factor(unit, 4 * (r + j) + b, p, -1)
            value += delta
    assert value == 0, (p, r, value)
    scale = pow((z - 1) % p, -1, p)
    return {k: totals.get(k, 0) * scale % p for k in (-2, -1, 0, 1)}


def ratio_and_log(p, r, z):
    inv = lambda a: pow(a % p, -1, p)
    args = [4 * r + b for b in (2, 3, 4)]
    ratio = z * pow(4 * r + 1, 3, p) * inv(args[0] * args[1] * args[2]) % p
    ell = (12 * inv(4 * r + 1) - 4 * sum(inv(x) for x in args)) % p
    ellprime = (-48 * inv(4 * r + 1)**2
                + 16 * sum(inv(x)**2 for x in args)) % p
    return ratio, ell, ellprime


def primary_observers(p, z):
    d = (p - 3) // 4
    C = 1
    T = L = J = 0
    coefficients = [1]
    logs = []
    for r in range(d):
        T = (T + (8 * r + 1) * C) % p
        ratio, ell, ellprime = ratio_and_log(p, r, z)
        logs.append(ell)
        L = (L + ell) % p
        J = (J + ellprime) % p
        C = C * ratio % p
        coefficients.append(C)
    T = (T + (8 * d + 1) * C) % p
    return {"d": d, "C_d": C, "T": T, "L": L, "J": J,
            "C": coefficients, "logs": logs}


def alpha_and_reflected(p):
    """Exact epsilon^-2 coefficient alpha at j0, and H_d(z)."""
    d = (p - 3) // 4
    j0 = 2 * d + 2
    alpha = 1
    zeros = 0
    for i in range(j0):
        alpha = alpha * pow((4 * i + 1) % p, 3, p) % p
        for b in (2, 3, 4):
            term = (4 * i + b) % p
            if term:
                alpha = alpha * pow(term, -1, p) % p
            else:
                alpha = alpha * pow(4, -1, p) % p
                zeros += 1
    assert zeros == 2 and alpha != 0
    h = 1
    hcoeffs = []
    for s in range(d + 1):
        hcoeffs.append((8 * s + 5) * h % p)
        if s < d:
            ratio = pow((4 * s + 3) % p, 3, p)
            den = (4 * s + 4) * (4 * s + 5) * (4 * s + 6)
            h = h * ratio * pow(den % p, -1, p) % p
    return alpha, hcoeffs


def eval_poly(coeffs, z, p):
    ans = 0
    for c in reversed(coeffs):
        ans = (ans * z + c) % p
    return ans


def check(p, z, all_ranks=False):
    data = primary_observers(p, z)
    d = data["d"]
    R0 = cyclic_laurent(p, 0, z)
    Rd = cyclic_laurent(p, d, z)
    Rplus = cyclic_laurent(p, d + 1, z)
    A0, B0 = R0[-2], R0[-1]
    assert Rplus[-2] == 0
    # GH-15 exact Laurent-regularized finite Gosper identity.
    counterterm = (B0 * data["L"]
                   + A0 * (data["J"] - data["L"]**2) * pow(2, -1, p)) % p
    rhs = (data["C_d"] * (Rd[0] + 8 * d + 1) - R0[0] + counterterm) % p
    assert rhs == data["T"], (p, z, "counterterm", rhs, data["T"])
    # at x=d: a_z(d+e)=2z/e - 12z + 56ze + ...
    assert A0 == (2 * z * data["C_d"] * Rplus[-1]) % p
    assert Rd[-2] == (2 * z * Rplus[-1]) % p
    assert Rd[-1] == (2 * z * Rplus[0] - 12 * z * Rplus[-1]) % p
    assert Rd[0] == (2 * z * Rplus[1] - 12 * z * Rplus[0]
                     + 56 * z * Rplus[-1] - (8 * d + 1)) % p
    # GH-16 alpha-z^(2d+2)-H polynomial factorization.
    alpha, hcoeffs = alpha_and_reflected(p)
    H = eval_poly(hcoeffs, z, p)
    a_from_H = (alpha * pow(z, 2 * d + 2, p) * H
                * pow(z - 1, -1, p)) % p
    assert a_from_H == A0, (p, z, "H-root", a_from_H, A0)
    # Any vanishing of A0 has precise interpretation as no pole at d+1.
    assert (A0 == 0) == (Rplus[-1] == 0)
    if all_ranks:
        accumulated = 0
        for r in range(d + 1):
            here = cyclic_laurent(p, r, z)
            assert data["C"][r] * here[-2] % p == A0
            assert (data["C"][r] * here[-1]
                    - (B0 - A0 * accumulated)) % p == 0
            if r < d:
                accumulated = (accumulated + data["logs"][r]) % p
    return {"p": p, "z": z, "d": d, "A0": A0, "B0": B0,
            "L": data["L"], "J": data["J"], "C_d": data["C_d"],
            "H0": R0[0], "Hd": Rd[0], "endpoint_residue": Rplus[-1],
            "T": data["T"], "counterterm": counterterm, "H": H}


def main():
    samples = primes_below(1000)
    assert len(samples) == 86
    rows = []
    for p in samples:
        for z in (2, 9):
            rows.append(check(p, z, all_ranks=p in (7, 11, 19, 23, 43, 67, 139)))
    assert all(row["A0"] == 0 and row["H"] == 0
               for row in rows if row["z"] == 9), "finite z=9 conjecture check"
    assert check(19, 2)["A0"] == 1, "genuine double pole counterexample"
    special = [row for row in rows if row["z"] == 9 and row["p"] in (19, 43, 67)]
    for item in special:
        print("CERT", item)
    print("PASS_GH15_ALL_PRIME_PARAMETRIC_LAURENT_COUNTERTERM_SAMPLES=", len(rows))
    print("PASS_GH16_REFLECTED_ALPHA_H_FACTOR_AND_FINITE_Z9_ROOT_SAMPLES=", len(samples))
    print("SCOPE: finite checks do not prove H_d(9)=0 for every prime")


if __name__ == "__main__":
    main()
