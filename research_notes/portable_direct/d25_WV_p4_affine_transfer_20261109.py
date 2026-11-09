#!/usr/bin/env python3
"""Exact, author-side W216/V2304 p^4 affine-transfer experiment.

Uses two different arithmetic implementations (modular term recurrence and
original integer binomial coefficients). No Sage, float, native H0/B0 or
Source Result/CLAIM. Observed congruence is a conjecture, NOT a theorem.
"""
import json
from math import comb
from pathlib import Path


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))


def recurrence_sums(p, precision=5):
    modulus = p**precision
    a = c = 1
    W = V = 0
    for n in range(p):
        W = (W + (6*n+1)*a) % modulus
        V = (V + (8*n+1)*c) % modulus
        if n == p-1:
            break
        j = n+1  # 1..p-1, always a p-adic unit
        a = (a * (2*n+1)*(2*n+2)*(3*n+1)*(3*n+2)*(3*n+3)
             * pow(216*j**5, -1, modulus)) % modulus
        c = (c * (4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)
             * pow(2304*j**4, -1, modulus)) % modulus
    return W, V


def original_binomial_sums(p, precision=5):
    modulus = p**precision
    W = V = 0
    for n in range(p):
        W += (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216, -n, modulus)
        V += (8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pow(2304, -n, modulus)
    return W % modulus, V % modulus


def half_direct(p):
    """Independent original-binomial half-cutoff test, NOT the frozen full sum."""
    modulus = p**4
    m = (p-1)//6
    W = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)
            *pow(216, -n, modulus) for n in range(3*m+1)) % modulus
    V = sum((8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2
            *pow(2304, -n, modulus) for n in range(3*m+1)) % modulus
    return W, V, (W-2*V+p)%modulus


def certificate(p):
    W, V = recurrence_sums(p)
    chi = 1 if p % 3 == 1 else -1   # Legendre (-3/p), p>3
    modulus = p**5
    affine = (W - 2*V + chi*p) % modulus
    direct = (W-V) % modulus
    return {
      "p":p, "p_mod_24":p%24, "legendre_minus3":chi,
      "W_mod_p5":W, "V_mod_p5":V,
      "W_mod_p3":W%p**3, "V_mod_p3":V%p**3,
      "affine_mod_p5":affine,
      "affine_p4_residue":affine % p**4,
      "affine_quotient_p4_mod_p":affine//p**4,
      "W_minus_V_quotient_p3_mod_p":((direct//p**3)%p if direct%p**3==0 else None)
    }


def main():
    primes = [p for p in range(5,1000) if is_prime(p)]
    primes += [p for p in [1009,1013,1031,1091,1201,1237,2003,2011] if is_prime(p)]
    assert len(primes)==174 and len(set(primes))==174
    checks=[certificate(p) for p in primes]
    assert all(r["affine_p4_residue"]==0 for r in checks)
    assert all(r["W_mod_p3"]==r["V_mod_p3"]==
               (r["legendre_minus3"]*r["p"])%r["p"]**3 for r in checks)
    witnesses = [5,7,13,19,37,43,61,67,73,109,139,373,997]
    for p in witnesses:
        row=next(r for r in checks if r["p"]==p)
        assert (row["W_mod_p5"],row["V_mod_p5"]) == original_binomial_sums(p)
    assert next(r for r in checks if r["p"]==373)["affine_quotient_p4_mod_p"] == 174
    assert next(r for r in checks if r["p"]==373)["W_minus_V_quotient_p3_mod_p"] == 114
    assert next(r for r in checks if r["p"]==13)["W_minus_V_quotient_p3_mod_p"] == 11
    half_witnesses = {13:(24687,4407,15886), 19:(127091,20596,85918),
                      373:(7176413322,6953946051,12625400234)}
    for p, expected in half_witnesses.items():
        assert half_direct(p) == expected
        assert expected[2] % p**2 == 0 and expected[2] % p**3 != 0
    out={"classification":"EXACT_FINITE_EXPERIMENT / CONJECTURE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE",
         "science_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
         "formula":"W_p - 2 V_p + (-3/p)*p = 0 mod p^4 (CONJECTURE ONLY)",
         "count":len(checks),"independent_direct_oracle_primes":witnesses,
         "p4_all_pass":True,"half_cutoff_counterexamples":half_witnesses,"p5_zero_primes":[r["p"] for r in checks if r["affine_mod_p5"]==0],
         "rows":checks}
    path=Path(__file__).with_name('d25_WV_p4_affine_transfer_results_20261109.json')
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS',len(checks),'primes; independent direct-binomial:',len(witnesses))
    print('p373',next(r for r in checks if r['p']==373))
    print('p13',next(r for r in checks if r['p']==13))
    print('p5 zero',out['p5_zero_primes'])

if __name__=='__main__': main()
