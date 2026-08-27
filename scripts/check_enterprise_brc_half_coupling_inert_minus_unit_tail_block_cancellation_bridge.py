#!/usr/bin/env python3
"""Exact/regression checker for the inert-minus unit-tail reduction.

The script checks finite identities and bounded prime instances only.
Imported CM/Legendre vanishing is theorem input in the research return;
this program does not turn finite regression into an all-prime proof.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0:1] = b"\x00"
    if n >= 1:
        sieve[1:2] = b"\x00"
    for q in range(2, int(n**0.5) + 1):
        if sieve[q]:
            sieve[q*q:n+1:q] = b"\x00" * (((n-q*q)//q)+1)
    return [i for i in range(2, n + 1) if sieve[i]]


def inv(a: int, m: int) -> int:
    return pow(a % m, -1, m)


def frac_mod(q: Fraction, m: int) -> int:
    if q.denominator % m == 0:
        raise ZeroDivisionError("fraction denominator is not a unit")
    return (q.numerator % m) * inv(q.denominator, m) % m


def harmonic(n: int, power: int = 1) -> Fraction:
    return sum((Fraction(1, k**power) for k in range(1, n + 1)), Fraction(0))


def b_list(p: int, power: int = 3) -> list[int]:
    M = p**power
    out = [1]
    for k in range(p - 1):
        num = (6*k + 1) * (3*k + 1)
        den = 36 * (k + 1) * (k + 1)
        out.append(out[-1] * (num % M) * inv(den, M) % M)
    return out


def a3_list(p: int, power: int = 3) -> list[int]:
    M = p**power
    out = [1]
    for k in range(p - 1):
        num = (2*k + 1) * (3*k + 1) * (3*k + 2)
        den = 36 * (k + 1)**3
        out.append(out[-1] * (num % M) * inv(den, M) % M)
    return out


def target_sum(p: int) -> int:
    M = p**3
    a = a3_list(p, 3)
    return sum((6*k + 1) * a[k] for k in range(p)) % M


def block_tail_minus(p: int) -> dict[str, int]:
    assert p % 6 == 5
    M = p**3
    Bv = b_list(p, 3)
    m = (p - 5)//6
    b0 = 4*m + 3
    b1 = 5*m + 4
    acc = [[0]*3 for _ in range(3)]
    for i in range(p):
        bi = 0 if i <= b0 else (1 if i <= b1 else 2)
        for j in range(p):
            if i + j < p:
                continue
            bj = 0 if j <= b0 else (1 if j <= b1 else 2)
            acc[bi][bj] = (
                acc[bi][bj] + (1 + 6*(i+j))*Bv[i]*Bv[j]
            ) % M
    return {
        "T00": acc[0][0],
        "T01": (acc[0][1] + acc[1][0]) % M,
        "T02": (acc[0][2] + acc[2][0]) % M,
        "T11": acc[1][1],
        "T12": (acc[1][2] + acc[2][1]) % M,
        "T22": acc[2][2],
        "total": sum(sum(row) for row in acc) % M,
    }


def p_poly_data(m: int, p: int) -> tuple[int, int]:
    """P_m(2), P'_m(2) for P_m(x)=2F1(-m,-m;m+2;x), modulo p."""
    value = 0
    deriv = 0
    for k in range(m + 1):
        num = 1
        den = 1
        for r in range(k):
            num = num * ((-m + r) % p) * ((-m + r) % p) % p
            den = den * ((m + 2 + r) % p) * (r + 1) % p
        coeff = num * inv(den, p) % p
        value = (value + coeff * pow(2, k, p)) % p
        if k:
            deriv = (deriv + k * coeff * pow(2, k-1, p)) % p
    return value, deriv


def reverse_tail_factor(p: int) -> int:
    """The proved mod-p one-variable factor for T00."""
    assert p % 6 == 5
    m = (p - 5)//6
    b0 = 4*m + 3
    P, Pd = p_poly_data(m, p)
    C = comb(2*m + 1, m) % p
    return (
        3
        * inv(pow(2, 2*b0, p), p)
        * C*C
        * P
        * ((5*P + 8*Pd) % p)
    ) % p


def A_m(m: int) -> int:
    return sum(
        2**(m-k) * comb(m, k) * comb(2*m + 1, k)
        for k in range(m + 1)
    )


def legendre_coeffs(n: int, p: int) -> list[int]:
    """P_n(x) coefficients modulo p, ascending powers."""
    if n == 0:
        return [1]
    P0 = [1]
    P1 = [0, 1]
    if n == 1:
        return P1
    for r in range(1, n):
        nxt = [0] * (r + 2)
        for k, c in enumerate(P1):
            nxt[k+1] = (nxt[k+1] + (2*r+1)*c) % p
        for k, c in enumerate(P0):
            nxt[k] = (nxt[k] - r*c) % p
        ir = inv(r+1, p)
        nxt = [(c*ir) % p for c in nxt]
        P0, P1 = P1, nxt
    return P1


def legendre_over_t_at_half(m: int, p: int) -> int:
    """P_{2m+1}(t)/t at t^2=1/2, root-free modulo p."""
    coeffs = legendre_coeffs(2*m + 1, p)
    t2 = inv(2, p)
    ans = 0
    for deg, c in enumerate(coeffs):
        if c == 0:
            continue
        if deg % 2 == 0:
            raise AssertionError("odd Legendre polynomial acquired even term")
        ans = (ans + c * pow(t2, (deg-1)//2, p)) % p
    return ans


def low_sum_G_mod_p(p: int) -> int:
    return sum(b_list(p, 1)) % p


def deformation_coeffs(m: int):
    p = 6*m + 5
    A = 5*m + 4
    B = 4*m + 3
    low = {}
    mid = {}
    high = {}
    HA = harmonic(A)
    HB = harmonic(B)
    HA2 = harmonic(A, 2)
    HB2 = harmonic(B, 2)
    for k in range(B + 1):
        w = Fraction(comb(A, k) * comb(B, k), 2**k)
        L = (
            -Fraction(5, 6) * (HA - harmonic(A-k))
            -Fraction(2, 3) * (HB - harmonic(B-k))
        )
        Q = Fraction(1, 2) * (
            L*L
            - Fraction(25, 36) * (HA2 - harmonic(A-k, 2))
            - Fraction(4, 9) * (HB2 - harmonic(B-k, 2))
        )
        low[k] = (w, L, Q)
    for k in range(B + 1, A + 1):
        d = Fraction(
            2 * ((-1)**(B+k)) * factorial(A) * factorial(B) * factorial(k-B-1),
            3 * factorial(A-k) * factorial(k)**2 * 2**k,
        )
        M = (
            -Fraction(5, 6) * (HA - harmonic(A-k))
            +Fraction(2, 3) * (harmonic(k-B-1) - HB)
        )
        mid[k] = (d, M)
    for k in range(A + 1, p):
        v = Fraction(
            5 * ((-1)**(A+B))
            * factorial(A) * factorial(B)
            * factorial(k-A-1) * factorial(k-B-1),
            9 * factorial(k)**2 * 2**k,
        )
        high[k] = v
    return p, A, B, low, mid, high


def deformation_sums(m: int):
    p, A, B, low, mid, high = deformation_coeffs(m)
    F0 = sum((w for w, _, _ in low.values()), Fraction(0))
    F1 = (
        sum((w*L for w, L, _ in low.values()), Fraction(0))
        + sum((d for d, _ in mid.values()), Fraction(0))
    )
    F2 = (
        sum((w*Q for w, _, Q in low.values()), Fraction(0))
        + sum((d*M for d, M in mid.values()), Fraction(0))
        + sum(high.values(), Fraction(0))
    )
    J0 = sum(((12*k+1)*low[k][0] for k in low), Fraction(0))
    J1 = (
        sum(((12*k+1)*low[k][0]*low[k][1] for k in low), Fraction(0))
        + sum(((12*k+1)*mid[k][0] for k in mid), Fraction(0))
    )
    return p, F0, F1, F2, J0, J1, low, mid, high


def tail_deformation_sums(m: int):
    p, F0, F1, F2, J0, J1, low, mid, high = deformation_sums(m)
    T000 = T001 = T002 = Fraction(0)
    for i, (wi, Li, Qi) in low.items():
        for j, (wj, Lj, Qj) in low.items():
            if i + j < p:
                continue
            W = 1 + 6*(i+j)
            T000 += W*wi*wj
            T001 += W*wi*wj*(Li+Lj)
            T002 += W*wi*wj*(Qi+Qj+Li*Lj)
    U010 = U011 = Fraction(0)
    for i, (wi, Li, _) in low.items():
        for j, (dj, Mj) in mid.items():
            if i + j < p:
                continue
            W = 1 + 6*(i+j)
            U010 += 2*W*wi*dj
            U011 += 2*W*wi*dj*(Li+Mj)
    U020 = Fraction(0)
    for i, (wi, _, _) in low.items():
        for j, vj in high.items():
            if i + j >= p:
                U020 += 2*(1+6*(i+j))*wi*vj
    U110 = Fraction(0)
    for i, (di, _) in mid.items():
        for j, (dj, _) in mid.items():
            if i + j >= p:
                U110 += (1+6*(i+j))*di*dj
    return (
        p, F0, F1, F2, J0, J1,
        T000, T001, T002, U010, U011, U020, U110,
    )


def run(bound: int) -> dict:
    rows = []
    failures = []
    all_6m5 = [p for p in primes_upto(bound) if p > 3 and p % 6 == 5]
    targets = [p for p in all_6m5 if p % 24 in (17, 23)]
    for p in all_6m5:
        m = (p - 5)//6
        blocks = block_tail_minus(p)
        factor = reverse_tail_factor(p)
        if blocks["T00"] % p != factor:
            failures.append({"kind": "T00_FACTOR", "p": p})
        A = A_m(m) % p
        L = legendre_over_t_at_half(m, p)
        if A != pow(2, m, p) * L % p:
            failures.append({"kind": "A_LEGENDRE_BRIDGE", "p": p})
        G = low_sum_G_mod_p(p)
        b0 = 4*m + 3
        if G != inv(pow(2, b0, p), p) * A % p:
            failures.append({"kind": "G_A_BRIDGE", "p": p})
        row = {
            "p": p,
            "class_mod_24": p % 24,
            "m": m,
            "T00_mod_p": blocks["T00"] % p,
            "factor_mod_p": factor,
            "A_mod_p": A,
            "legendre_over_t_mod_p": L,
            "G_mod_p": G,
        }
        if p in targets:
            if L != 0:
                failures.append({"kind": "CM_ZERO_REGRESSION", "p": p})
            if blocks["T00"] % p:
                failures.append({"kind": "T00_DIV", "p": p})
            if blocks["T01"] % p:
                failures.append({"kind": "T01_DIV", "p": p})
            if blocks["T02"] % (p*p):
                failures.append({"kind": "T02_DIV", "p": p})
            if blocks["T11"] % (p*p):
                failures.append({"kind": "T11_DIV", "p": p})
            (
                _, F0, F1, F2, J0, J1,
                T000, T001, T002, U010, U011, U020, U110,
            ) = tail_deformation_sums(m)
            M3 = p**3
            M2 = p**2
            Bv = b_list(p, 3)
            G3 = sum(Bv) % M3
            H3 = sum((12*k+1)*Bv[k] for k in range(p)) % M3
            T3 = blocks["total"]
            Gexp = (
                frac_mod(F0, M3)
                + p*frac_mod(F1, M3)
                + p*p*frac_mod(F2, M3)
            ) % M3
            Hexp = (frac_mod(J0, M2) + p*frac_mod(J1, M2)) % M2
            Texp = (
                frac_mod(T000, M3)
                + p*frac_mod(T001+U010, M3)
                + p*p*frac_mod(T002+U011+U020+U110, M3)
            ) % M3
            if G3 != Gexp:
                failures.append({"kind": "G_DEFORMATION", "p": p})
            if H3 % M2 != Hexp:
                failures.append({"kind": "H_DEFORMATION", "p": p})
            if T3 != Texp:
                failures.append({"kind": "T_DEFORMATION", "p": p})
            if F0.numerator % p or T000.numerator % p:
                failures.append({"kind": "NORMALIZATION_INTEGRALITY", "p": p})
            g0 = F0/Fraction(p) + F1
            g1 = F2
            tau0 = T000/Fraction(p) + T001 + U010
            tau1 = T002 + U011 + U020 + U110
            r0 = frac_mod(g0*J0 - tau0 + 1, p)
            r1 = frac_mod(
                (g0*J0 - tau0 + 1)/Fraction(p)
                + g0*J1 + g1*J0 - tau1,
                p,
            )
            normalized = frac_mod(
                (g0+p*g1)*(J0+p*J1) - (tau0+p*tau1) + 1,
                M2,
            )
            if r0 or r1 or normalized:
                failures.append(
                    {"kind": "NORMALIZED_CERTIFICATE", "p": p,
                     "r0": r0, "r1": r1, "full": normalized}
                )
            want = (-p) % M3
            got = target_sum(p)
            if got != want:
                failures.append({"kind": "TARGET_REGRESSION", "p": p})
            row.update({
                "T01_over_p_mod_p": (blocks["T01"]//p) % p,
                "T02_over_p2_mod_p": (blocks["T02"]//(p*p)) % p,
                "T11_over_p2_mod_p": (blocks["T11"]//(p*p)) % p,
                "R0_mod_p": r0,
                "R1_mod_p": r1,
            })
        rows.append(row)
    return {
        "schema": "ENTERPRISE_BRC_INERT_MINUS_UNIT_TAIL_REDUCTION_REGRESSION_V1",
        "bound": bound,
        "all_p_6m_plus_5_count": len(all_6m5),
        "target_prime_count": len(targets),
        "target_classes": [17, 23],
        "rows": rows,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "proof_status": "FINITE_REGRESSION_ONLY_NOT_A_PROOF",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bound", type=int, default=300)
    ap.add_argument("--json-out")
    args = ap.parse_args()
    data = run(args.bound)
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if data["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
