#!/usr/bin/env python3
"""Exact author-side D25 certificate, not native H0/B0 or formal admission.

No floating point. The independent oracle evaluates original integer binomials;
the compressed path uses separate p-adic hypergeometric recurrences.
"""
import json
from math import comb, factorial
from pathlib import Path

PRIMES = [7, 13, 19, 31, 37, 43, 61, 67, 73,
          97, 109, 127, 157, 163, 193, 211, 229, 373]


def w_raw(n, modulus):
    coefficient = comb(2 * n, n) ** 2 * comb(3 * n, n)
    return ((6 * n + 1) * coefficient * pow(216, -n, modulus)) % modulus


def v_raw(n, modulus):
    coefficient = comb(4 * n, 2 * n) * comb(2 * n, n) ** 2
    return ((8 * n + 1) * coefficient * pow(2304, -n, modulus)) % modulus


def grade1_jet(p):
    """Compute T_1/p mod p^2 through shifted 3F2 first jet."""
    m = (p - 1) // 6
    q = p * p
    n0 = 2 * m + 1
    coefficient0 = comb(2 * n0, n0) ** 2 * comb(3 * n0, n0)
    assert coefficient0 % p == 0 and coefficient0 % (p * p) != 0
    k1 = ((coefficient0 // p) * pow(216, -n0, q)) % q
    u, d, s0, s1 = 1, 0, 0, 0
    for j in range(m):
        weight = 6 * j + 5
        s0 = (s0 + weight * u) % q
        s1 = (s1 + (2 + weight * d) * u) % p
        if j + 1 == m:
            break
        den = 3 * j + 5
        # U_{j+1}(0)/U_j(0) exactly, over Z/p^2.
        u = (u * (6*j+7) * (3*j+3) * (3*j+4)
             * pow(4 * den**3, -1, q)) % q
        # d/d(p) log U_j(p) evaluated at p=0, modulo p.
        d = (d + 2*pow(6*j+7, -1, p)
             + pow(3*(j+1), -1, p) + pow(3*j+4, -1, p)
             - 3*pow(den, -1, p)) % p
    divided = k1 * (s0 + p * s1) % q
    return {"K1_mod_p2": k1, "S0_mod_p2": s0,
            "S1_mod_p": s1, "T1_over_p_mod_p2": divided,
            "T1_mod_p3": p * divided}


def grade2_companion(p):
    """Reuses previous p^2-grade theorem (Pochhammer form), modulo p."""
    m = (p - 1) // 6
    k2 = (factorial(3*m+2) * pow(factorial(3*m+1), -5, p)
          * pow(216, -(3*m+1), p)) % p
    u, s2 = 1, 0
    for j in range(m):
        s2 = (s2 + (6*j+4)*u) % p
        if j + 1 == m:
            break
        u = (u * (j+1)*(6*j+5)*(6*j+7)
             * pow(9*(2*j+3)**3, -1, p)) % p
    return {"K2_mod_p": k2, "S2_mod_p": s2,
            "T2_over_p2_mod_p": k2 * s2 % p,
            "T2_mod_p3": (p*p)*(k2*s2 % p)}


def certify(p):
    assert p > 3 and p % 6 == 1
    m = (p-1)//6; modulus = p**3
    w_full = sum(w_raw(n, modulus) for n in range(p)) % modulus
    v_full = sum(v_raw(n, modulus) for n in range(p)) % modulus
    w0 = sum(w_raw(n, modulus) for n in range(2*m+1)) % modulus
    w1_raw = sum(w_raw(n, modulus) for n in range(2*m+1, 3*m+1)) % modulus
    w2_raw = sum(w_raw(n, modulus) for n in range(3*m+1, 4*m+1)) % modulus
    v_half = sum(v_raw(n, modulus) for n in range(3*m+1)) % modulus
    g1, g2 = grade1_jet(p), grade2_companion(p)
    assert w1_raw == g1["T1_mod_p3"], (p, "grade1")
    assert w2_raw == g2["T2_mod_p3"], (p, "grade2")
    assert (w0 + w1_raw + w2_raw) % modulus == w_full
    assert v_half == v_full  # Prior Guo-Zudilin full/half p^3 statement, here independently tested.
    reduced = (w0 - v_half + g1["T1_mod_p3"] + g2["T2_mod_p3"]) % modulus
    assert reduced == (w_full-v_full) % modulus
    return {"p":p,"m":m,"mod_p3":modulus,"W_full":w_full,"V_full":v_full,
            "W_grade0":w0,"W_grade1_raw":w1_raw,"W_grade2_raw":w2_raw,
            "V_half":v_half,"grade1_jet":g1,"grade2_reused":g2,
            "compressed_W_minus_V":reduced,"raw_W_minus_V":(w_full-v_full)%modulus,
            "exact_checks_passed": True}


def main():
    data={"status":"AUTHOR_SIDE_COMPUTATION_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
          "scope":"All primes p=6m+1>3 for the proved formulas; the numeric checks are only the listed 18 primes.",
          "science_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
          "checks":[certify(p) for p in PRIMES]}
    path=Path(__file__).with_name("d25_w216_grade1_jet_cross_grade_results_20261109.json")
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("PASS",len(data["checks"]),"primes",PRIMES)
    print("p373:",json.dumps(data["checks"][-1],sort_keys=True))
    print("saved:",path)

if __name__=="__main__":main()
