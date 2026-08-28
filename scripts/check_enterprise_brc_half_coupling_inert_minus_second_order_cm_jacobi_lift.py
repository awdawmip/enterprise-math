#!/usr/bin/env python3
"""Regression checker for the inert-minus CM/Jacobi lift strict reduction.

This script proves nothing by finite search. It checks:
  1. exact rational finite-Clausen coefficient identities at small n;
  2. the exact p-adic valuation formula for the collapsed coefficients;
  3. the predicted Ramanujan-Sun weighted supercongruence on bounded primes;
  4. the observed finite bridge to Swisher's E.2-side truncation;
  5. an independent Domb-side bounded diagnostic.

No non-stdlib dependency is required.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, isqrt
import argparse


def primes_upto(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        ok = True
        for q in range(2, isqrt(x) + 1):
            if x % q == 0:
                ok = False
                break
        if ok:
            out.append(x)
    return out


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp_int(0) is not used here")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def poch(a: Fraction, k: int) -> Fraction:
    z = Fraction(1)
    for j in range(k):
        z *= a + j
    return z


def b_exact(k: int) -> Fraction:
    # (1/6)_k (1/3)_k / (k!)^2 / 2^k
    fact = 1
    for j in range(1, k + 1):
        fact *= j
    return poch(Fraction(1, 6), k) * poch(Fraction(1, 3), k) / (fact * fact * (2**k))


def collapsed_exact(n: int) -> Fraction:
    # binom(2n,n)^2 binom(3n,n) / 216^n
    return Fraction(comb(2 * n, n) ** 2 * comb(3 * n, n), 216**n)


def check_clausen(nmax: int) -> None:
    for n in range(nmax + 1):
        lhs = sum((b_exact(i) * b_exact(n - i) for i in range(n + 1)), Fraction(0))
        rhs = collapsed_exact(n)
        if lhs != rhs:
            raise AssertionError(("Clausen coefficient failure", n, lhs, rhs))


def collapsed_num(n: int) -> int:
    return comb(2 * n, n) ** 2 * comb(3 * n, n)


def valuation_formula(n: int, p: int) -> int:
    return (2 * n) // p + (3 * n) // p


def check_valuation(p: int) -> None:
    for n in range(p):
        v = vp_int(collapsed_num(n), p)
        want = valuation_formula(n, p)
        if v != want:
            raise AssertionError(("valuation failure", p, n, v, want))


def W_mod(p: int) -> int:
    mod = p**3
    inv216 = pow(216, -1, mod)
    pw = 1
    s = 0
    for k in range(p):
        a = collapsed_num(k) % mod
        s = (s + (6 * k + 1) * a * pw) % mod
        pw = pw * inv216 % mod
    return s


def E_mod(p: int) -> int:
    """Swisher E.2-side truncation for p == 2 mod 3.

    E_p = sum_{k=0}^{(2p-1)/3} (-1)^k(6k+1)(1/3)_k^3/(k!)^3.
    """
    if p % 3 != 2:
        raise ValueError("E_mod is used only for p == 2 mod 3")
    M = (2 * p - 1) // 3
    mod = p**3
    t = 1
    s = 1
    for k in range(M):
        # t_{k+1}/t_k = -(3k+1)^3/[27(k+1)^3].
        num = -((3 * k + 1) ** 3)
        den = 27 * ((k + 1) ** 3)
        t = t * (num % mod) % mod
        t = t * pow(den, -1, mod) % mod
        kk = k + 1
        s = (s + (6 * kk + 1) * t) % mod
    return s


def domb(n: int) -> int:
    return sum(
        comb(n, k) ** 2 * comb(2 * k, k) * comb(2 * n - 2 * k, n - k)
        for k in range(n + 1)
    )


def domb_weighted_mod(p: int) -> int:
    mod = p**3
    inv_minus_8 = pow(-8, -1, mod)
    pw = 1
    s = 0
    for n in range(p):
        s = (s + (2 * n + 1) * (domb(n) % mod) * pw) % mod
        pw = pw * inv_minus_8 % mod
    return s


def jacobi_p_over_3(p: int) -> int:
    if p % 3 == 1:
        return 1
    if p % 3 == 2:
        return -1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=1000)
    ap.add_argument("--domb-bound", type=int, default=100)
    ap.add_argument("--clausen-n", type=int, default=10)
    args = ap.parse_args()

    check_clausen(args.clausen_n)

    ps = [p for p in primes_upto(args.bound) if p > 3]
    all_formula = []
    inert_minus = []
    bridge = []
    for p in ps:
        check_valuation(p)
        w = W_mod(p)
        want = (p * jacobi_p_over_3(p)) % (p**3)
        if w != want:
            raise AssertionError(("bounded W formula failure", p, w, want))
        all_formula.append(p)

        if p % 24 in (17, 23):
            if w != (-p) % (p**3):
                raise AssertionError(("inert-minus target failure", p, w))
            inert_minus.append(p)

        if p % 3 == 2:
            e = E_mod(p)
            if (e - 2 * w) % (p**3) != 0:
                raise AssertionError(("Swisher bridge failure", p, e, w))
            bridge.append(p)

    domb_ps = [p for p in primes_upto(args.domb_bound) if p > 3 and p % 3 == 2]
    for p in domb_ps:
        if domb_weighted_mod(p) != (-p) % (p**3):
            raise AssertionError(("Domb diagnostic failure", p))

    print("PASS")
    print(f"clausen_coefficients=0..{args.clausen_n}")
    print(f"bounded_W_formula_primes={len(all_formula)} <= {args.bound}")
    print(f"inert_minus_primes={len(inert_minus)} <= {args.bound}")
    print(f"swisher_bridge_primes={len(bridge)} <= {args.bound}")
    print(f"domb_diagnostic_primes={len(domb_ps)} <= {args.domb_bound}")
    print("proof_status=FINITE_REGRESSION_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
