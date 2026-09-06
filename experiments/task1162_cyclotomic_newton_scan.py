#!/usr/bin/env python3
"""Exact finite scan for fully cyclotomic positive quadratic Fekete polynomials.

TASK #1162 research experiment.  This is a finite computation certificate, not a
proof of a global classification.

For a positive fundamental discriminant D let
    P_D(x) = F_D(x)/x = sum_{a=1}^{D-1} chi_D(a) x^(a-1).
P_D is monic with constant term 1.  If P_D is a product of cyclotomic
polynomials then all its roots have modulus 1, hence every Newton power sum
S_k satisfies |S_k| <= deg(P_D)=D-2.

The scan computes S_k exactly from the first character coefficients and rejects
D at the first violation.  The six survivors known in the scanned range are
then verified by exact (1-x^d)-product identities.
"""

from __future__ import annotations

import argparse


KNOWN_C = {
    5: {1: 1, 2: 1, 5: -1},
    8: {2: 1, 4: 1, 8: -1},
    12: {4: 1, 6: 1, 12: -1},
    24: {4: -1, 6: 1, 8: 1, 12: 1, 24: -1},
    28: {2: -1, 4: 2, 6: -1, 12: 1, 14: 1, 28: -1},
    60: {6: -1, 10: -1, 12: 2, 20: 1, 30: 1, 60: -1},
}


def jacobi_symbol(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError("Jacobi denominator must be positive odd")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def kronecker_positive_denominator(a: int, n: int) -> int:
    """Kronecker (a/n) for n>=1, enough for this positive-conductor scan."""
    if n <= 0:
        raise ValueError("denominator must be positive")
    if n == 1:
        return 1
    twos = 0
    while n % 2 == 0:
        twos += 1
        n //= 2
    result = 1
    if twos:
        if a % 2 == 0:
            return 0
        atwo = 1 if a % 8 in (1, 7) else -1
        if twos % 2:
            result *= atwo
    if n > 1:
        result *= jacobi_symbol(a, n)
    return result


def is_squarefree(n: int) -> bool:
    if n <= 0:
        return False
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p = 3 if p == 2 else p + 2
    return True


def is_positive_fundamental_discriminant(D: int) -> bool:
    if D <= 0:
        return False
    if D % 4 == 1:
        return is_squarefree(D)
    if D % 4 == 0:
        d = D // 4
        return d % 4 in (2, 3) and is_squarefree(d)
    return False


def newton_unit_circle_test(D: int, depth: int) -> tuple[bool, int | None, int | None]:
    """Return first exact |S_k|>D-2 violation, if found within depth."""
    degree = D - 2
    depth = min(depth, degree)
    powers = [0] * (depth + 1)
    coeff = [0] * (depth + 1)
    # P_D is reciprocal for D>0.  Its coefficient of x^(degree-j) is chi_D(j+1).
    for j in range(1, depth + 1):
        coeff[j] = kronecker_positive_denominator(D, j + 1)
    for k in range(1, depth + 1):
        subtotal = sum(coeff[j] * powers[k - j] for j in range(1, k))
        powers[k] = -(subtotal + k * coeff[k])
        if abs(powers[k]) > degree:
            return False, k, powers[k]
    return True, None, None


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        if av:
            for j, bv in enumerate(b):
                if bv:
                    out[i + j] += av * bv
    return out


def factor_one_minus_xd(d: int) -> list[int]:
    out = [0] * (d + 1)
    out[0] = 1
    out[d] = -1
    return out


def factor_power(d: int, exponent: int) -> list[int]:
    out = [1]
    for _ in range(exponent):
        out = poly_mul(out, factor_one_minus_xd(d))
    return out


def trim(poly: list[int]) -> list[int]:
    poly = poly[:]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def verify_known_cyclotomic_identity(D: int, c: dict[int, int]) -> bool:
    """Verify P_D=(1-x^D)*prod_d(1-x^d)^c_d by integer cross multiplication."""
    P = [kronecker_positive_denominator(D, a) for a in range(1, D)]
    lhs = P
    for d, exponent in c.items():
        if exponent < 0:
            lhs = poly_mul(lhs, factor_power(d, -exponent))
    rhs = factor_one_minus_xd(D)
    for d, exponent in c.items():
        if exponent > 0:
            rhs = poly_mul(rhs, factor_power(d, exponent))
    return trim(lhs) == trim(rhs)


def scan(limit: int, depth: int) -> None:
    survivors: list[int] = []
    count = 0
    latest = (0, 0, 0)  # depth, D, S_k
    for D in range(5, limit + 1):
        if not is_positive_fundamental_discriminant(D):
            continue
        count += 1
        ok, k, value = newton_unit_circle_test(D, depth)
        if ok:
            survivors.append(D)
        else:
            assert k is not None and value is not None
            if k > latest[0]:
                latest = (k, D, value)

    print(f"positive fundamental discriminants checked: {count}")
    print(f"limit={limit}, Newton depth={depth}")
    print(f"survivors: {survivors}")
    if latest[0]:
        print(f"latest rejection: D={latest[1]}, k={latest[0]}, S_k={latest[2]}, degree={latest[1]-2}")

    known = sorted(KNOWN_C)
    if survivors == known:
        print("survivors match the six known fully-cyclotomic examples")
    else:
        print("WARNING: unresolved survivors beyond the known six:", sorted(set(survivors) - set(known)))

    for D, c in KNOWN_C.items():
        if D <= limit:
            ok = verify_known_cyclotomic_identity(D, c)
            print(f"exact product identity D={D}: {'PASS' if ok else 'FAIL'}")
            if not ok:
                raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=100_000)
    parser.add_argument("--depth", type=int, default=300)
    args = parser.parse_args()
    scan(args.limit, args.depth)
