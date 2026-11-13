#!/usr/bin/env python3
"""Exact finite-field audit of D25/GH-151 centered parity and coefficients.

No native Enterprise Math role or review authority is inferred from this test.
Proof is in PROOF.md; finite tests only cross-check.
"""
from __future__ import annotations

import json
from math import comb

PRIMES = (11, 19, 43, 59, 67, 83, 107, 3347)


def factorial_tables(p: int):
    f = [1] * p
    for k in range(1, p):
        f[k] = (f[k - 1] * k) % p
    fi = [1] * p
    fi[-1] = pow(f[-1], -1, p)
    for k in range(p - 1, 0, -1):
        fi[k - 1] = fi[k] * k % p
    return f, fi


def binom_mod(a: int, b: int, p: int, f: list[int], fi: list[int]) -> int:
    if not 0 <= b <= a < p:
        return 0
    return f[a] * fi[b] * fi[a - b] % p


def verify_prime(p: int) -> dict:
    assert p % 8 == 3 and p >= 11
    m = (p - 3) // 8
    N = (p - 1) // 2
    degree = 2 * m
    f, fi = factorial_tables(p)
    inv8 = pow(8, -1, p)
    h = [binom_mod(N, k, p, f, fi) * binom_mod(N - k, k, p, f, fi) % p
         for k in range(degree + 1)]
    assert h[degree] != 0

    # Direct expansion of H_p(1/8 + Z): h_k=[B^k] H_p(B).
    # c_j = sum_{k>=j} h_k * binom(k,j) * (1/8)^(k-j).
    # This computes centered coefficients without solving any PF recurrence.
    powers_inv8 = [1] * (degree + 1)
    for k in range(1, degree + 1):
        powers_inv8[k] = powers_inv8[k - 1] * inv8 % p
    c = []
    for j in range(degree + 1):
        coeff = sum(h[k] * binom_mod(k, j, p, f, fi) * powers_inv8[k - j]
                    for k in range(j, degree + 1)) % p
        c.append(coeff)
    assert all(c[j] == 0 for j in range(1, degree + 1, 2)), "unexpected odd centered term"
    assert c[0] != 0, "nonzero H and even-PF uniqueness imply nonzero anchor"

    # Frobenius: rho^2=2. If B=1/8+rho*v and W=v^2,
    # G(W) coefficient g_k = 2^k * c_(2k).
    g = [pow(2, k, p) * c[2 * k] % p for k in range(m + 1)]
    g0 = g[0]
    u = [1]
    for k in range(m):
        ratio_num = 4 * (8 * k + 1) * (8 * k + 3)
        ratio_den = (k + 1) * (2 * k + 1)
        u.append(u[-1] * ratio_num * pow(ratio_den, -1, p) % p)
    assert all(g[k] == g0 * u[k] % p for k in range(m + 1))

    # Newly isolated closed finite-binomial coefficient certificate:
    # u_k * C(4m+1,k) = (-128)^k C(3m+1,k) C(m,k) mod p.
    closed = []
    for k in range(m + 1):
        lhs = u[k] * binom_mod(4 * m + 1, k, p, f, fi) % p
        rhs = (pow(-128, k, p) * binom_mod(3 * m + 1, k, p, f, fi)
               * binom_mod(m, k, p, f, fi)) % p
        assert lhs == rhs, (p, k, lhs, rhs)
        closed.append(rhs)

    # ODE over Fp in centered Z=B-1/8:
    # (1/16-4 Z^2) H'' - 8 Z H' - 3/4 H=0.
    # Coefficient recursion (j+2)(j+1)c_{j+2}
    # =4(4j+1)(4j+3)c_j, for j >=0.
    for j in range(degree + 1):
        nextc = c[j + 2] if j + 2 <= degree else 0
        assert (((j + 2) * (j + 1) * nextc
                 - 4 * (4 * j + 1) * (4 * j + 3) * c[j]) % p == 0), (p, j)
    assert all((4 * j + 1) % p and (4 * j + 3) % p
               for j in range(1, degree, 2))

    out = {
        "p": p, "m": m, "degree_H": degree,
        "odd_centered_coefficients_zero": degree // 2,
        "checked_centered_coefficients": degree + 1,
        "checked_normalized_even_coefficients": m + 1,
        "checked_binomial_coefficients": len(closed),
        "g0_mod_p": g0,
        "highest_H_coefficient_nonzero": True,
        "mode": "DIRECT_BINOMIAL_CENTERED_EXPANSION_VS_PF_AND_CLOSED_FORM",
    }
    if p == 3347:
        # Independent Fp point count only at the one anchor B=1/8.
        ap = 0
        B0 = inv8
        for x in range(p):
            rhs = (x**3 + x*x + B0*x) % p
            if rhs:
                symbol = pow(rhs, (p-1)//2, p)
                ap -= (1 if symbol == 1 else -1)
        assert ap == -114
        assert g0 == ap % p
        W0 = pow(144, -1, p)
        G = sum(g[k] * pow(W0,k,p) for k in range(m+1)) % p
        dG = sum(k * g[k] * pow(W0,k-1,p) for k in range(1,m+1)) % p
        J = G*G % p
        dJ = 2*G*dG % p
        assert (W0, G, dG, J, dJ) == (860, 783, 2824, 588, 997), (W0,G,dG,J,dJ)
        out.update({"a_p_integer_independent_anchor":ap,"W0":W0,
                    "G_W0":G,"Gprime_W0":dG,"J_W0":J,"Jprime_W0":dJ,
                    "S1_plus_rho_coefficient": dJ*pow(12,-1,p)%p})
        assert out["S1_plus_rho_coefficient"] == 362
    return out


def main():
    rows = [verify_prime(p) for p in PRIMES]
    total = sum(x["checked_centered_coefficients"] for x in rows)
    results={"result":"PASS_GH151_PARITY_RIGIDITY_EXACT",
             "scope":"8 primes p=8m+3 including p=3347; no universal theorem inferred from test alone",
             "proof_route":"highest odd centered coefficient of PF ODE; no GH-131 reflection dependency",
             "independence":"shared source context, no independent Driver review",
             "cases":rows,"total_centered_coefficients_checked":total}
    print(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
