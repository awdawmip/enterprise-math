#!/usr/bin/env python3
"""Author-side exact W216/V2304 fourth-digit boundary and grade-3 companions.

Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.
This checks original coefficients, not native H0/B0 divided-power data.
"""
from math import comb, factorial
import json
from pathlib import Path

PRIMES = [7, 13, 19, 31, 37, 43, 61, 67, 73,
          97, 109, 127, 157, 163, 193, 211, 229, 373]


def original_binomial_oracle(p):
    q = p**4
    w = [(6*n+1)*comb(2*n, n)**2*comb(3*n, n)*pow(216, -n, q) % q
         for n in range(p)]
    v = [(8*n+1)*comb(4*n, 2*n)*comb(2*n, n)**2*pow(2304, -n, q) % q
         for n in range(p)]
    return w, v


def independent_unit_factorial_oracle(p):
    q = p**4
    u, e = [1]*(4*p-3), [0]*(4*p-3)
    for k in range(1, 4*(p-1)+1):
        t, r = k, 0
        while t % p == 0:
            t //= p
            r += 1
        u[k] = u[k-1]*t % q
        e[k] = e[k-1]+r
    w, v = [], []
    for n in range(p):
        a = e[2*n]+e[3*n]-5*e[n]
        b = e[4*n]-4*e[n]
        assert 0 <= a <= 3 and 0 <= b <= 3
        w.append((6*n+1)*p**a*u[2*n]*u[3*n]*pow(u[n], -5, q)
                 *pow(216, -n, q) % q)
        v.append((8*n+1)*p**b*u[4*n]*pow(u[n], -4, q)
                 *pow(2304, -n, q) % q)
    return w, v


def w_grade3_companion(p):
    m = (p-1)//6
    n0, length = 4*m+1, 2*m
    k = (-2*factorial(2*m+1)*pow(factorial(4*m+1), -5, p)
         *pow(216, -n0, p)) % p
    u, s = 1, 0
    for j in range(length):
        s = (s+(6*j+3)*u) % p
        if j+1 < length:
            u = (u*3*(6*j+5)*(3*j+2)*(j+1)
                 *pow(4*(3*j+4)**3, -1, p)) % p
    return {"start": n0, "terms": length, "K": k, "S": s, "product": k*s % p}


def v_grade3_companion(p):
    eps = p % 4
    n0, length = (3*p+eps)//4, (p-eps)//4
    k = (-6*factorial(eps)*pow(factorial(n0), -4, p)
         *pow(2304, -n0, p)) % p
    u, s = 1, 0
    for j in range(length):
        s = (s+(8*j+2*eps+1)*u) % p
        if j+1 < length:
            u = (u*(4*j+eps+1)*(4*j+eps+2)*(4*j+eps+3)
                 *pow(9*(4*j+eps+4)**3, -1, p)) % p
    return {"epsilon": eps, "start": n0, "terms": length,
            "K": k, "S": s, "product": k*s % p}


def certify(p):
    assert p > 3 and p % 6 == 1
    q, p3 = p**4, p**3
    w, v = original_binomial_oracle(p)
    assert (w, v) == independent_unit_factorial_oracle(p)
    wg, vg = [0]*4, [0]*4
    wc, vc = [0]*4, [0]*4
    for n in range(p):
        a = 2*n//p+3*n//p
        b = 4*n//p
        wg[a] = (wg[a]+w[n]) % q
        vg[b] = (vg[b]+v[n]) % q
        wc[a] += 1
        vc[b] += 1
    wp, vp = sum(wg) % q, sum(vg) % q
    d = (wp-vp) % q
    assert d % p3 == 0  # scoped finite test, not all-prime theorem
    assert wg[3] % p3 == 0 and vg[3] % p3 == 0
    w3, v3 = w_grade3_companion(p), v_grade3_companion(p)
    assert wg[3]//p3 == w3["product"]
    assert vg[3]//p3 == v3["product"]
    assert sum(vg[2:]) % p3 == 0
    low = (sum(wg[:3])-sum(vg[:2])) % q
    vtail = sum(vg[2:]) % q
    assert low % p3 == 0
    assert (low//p3+w3["product"]-vtail//p3) % p == d//p3
    return {"p": p, "m": (p-1)//6, "p4": q,
            "W_mod_p4": wp, "V_mod_p4": vp,
            "difference_mod_p4": d, "difference_over_p3_mod_p": d//p3,
            "W_grade_sums": wg, "V_grade_sums": vg,
            "W_grade_counts": wc, "V_grade_counts": vc,
            "W3": w3, "V3": v3,
            "precision4_source_channels": {
                "low_W012_minus_V01_over_p3": low//p3,
                "W_grade3_over_p3": w3["product"],
                "V_tail_over_p3": vtail//p3,
                "delta": d//p3},
            "two_independent_original_oracles_agree": True,
            "two_grade3_companions_agree": True}


def main():
    result = {"schema": "EM_D25_ORIGINAL_WV_P4_BOUNDARY_V1",
              "evidence_status": "AUTHOR_SIDE_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
              "frozen_science_pin": "c47e13e4aba0e006366f989d6334d443f6333ae3",
              "coverage": "listed 18 primes only; grade3 identities proven for all p=6m+1>3",
              "primes": [certify(p) for p in PRIMES]}
    out = Path(__file__).with_name("d25_original_w216_v2304_p4_boundary_results_20261109.json")
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    for row in result["primes"]:
        print(row["p"], row["difference_over_p3_mod_p"])
    print("PASS", len(result["primes"]), "two independent original oracles and two grade3 formula checks")
    print("p373", json.dumps(result["primes"][-1], sort_keys=True))
    print("saved", out)


if __name__ == "__main__":
    main()
