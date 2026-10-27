#!/usr/bin/env python3
"""D25 author-only weighted-216 high-band mod-p jet, not native H0/B0.

The code checks two genuinely different calculations of the SAME original
weighted binomial terms: full integers modulo p^3 and a terminating finite
field hypergeometric derivative/Legendre sign expression.
"""
import hashlib
import json
from math import comb, factorial


def prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def witness(p):
    assert prime(p) and p > 3 and p % 6 == 1
    m = (p - 1) // 6
    p2, p3 = p * p, p**3
    inv216 = pow(216, -1, p3)
    def w(n):
        # Original exact integer binomial model, only reduction mod p^3.
        return ((6*n + 1) * comb(2*n, n)**2 * comb(3*n, n)
                * pow(inv216, n, p3)) % p3

    high_start, high_end = 3*m+1, 4*m
    full_terms = [w(n) for n in range(p)]
    high = full_terms[high_start:high_end+1]
    assert len(high) == m and all(x % p2 == 0 for x in high)
    assert all(x == 0 for x in full_terms[high_end+1:])
    high_quot = [(x // p2) % p for x in high]
    high_total = sum(high) % p3

    # Wilson reduction of factorial terms; computed separately in F_p.
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i-1]*i % p
    wilson_terms = [
        (6*n+1)*fact[2*n-p]*fact[3*n-p]
        *pow(fact[n], -5, p)*pow(216, -n, p) % p
        for n in range(high_start, high_end+1)
    ]
    assert wilson_terms == high_quot

    chi_code = pow(6, (p-1)//2, p)
    assert chi_code in (1, p-1)
    chi = 1 if chi_code == 1 else -1
    t1 = 4 * pow(9, -1, p) * chi % p
    assert t1 == wilson_terms[0]

    # Ratio formula in the genuine two-parameter local field observer:
    # q_k=(k! (5/6)_k(7/6)_k/(3/2)_k^3)*2^(-k).
    # K=F(1/2)+(3/2)*(z F'(z))|z=1/2.
    t = 1
    F, z_derivative, jet_terms = 0, 0, []
    sixinv, twoinv = pow(6, -1, p), pow(2, -1, p)
    for k in range(m):
        F = (F + t) % p
        z_derivative = (z_derivative + k*t) % p
        jet_terms.append(t1*(3*k+2)*twoinv*t % p)
        if k < m-1:
            a = (k*6+5)*sixinv % p
            b = (k*6+7)*sixinv % p
            c = (2*k+3)*twoinv % p
            t = t*(k+1)*a*b*pow(c, -3, p)*twoinv % p
    K = (F+3*twoinv*z_derivative) % p
    assert jet_terms == wilson_terms
    assert (t1*K) % p == high_total // p2

    low = sum(full_terms[:high_start]) % p3
    entire = sum(full_terms) % p3
    assert entire == (low + high_total) % p3
    result = {"p": p, "m": m, "chi6": chi, "t1": t1,
              "F": F, "zFprime": z_derivative, "K": K,
              "high_quot": high_total//p2, "high_mod_p3": high_total,
              "low_mod_p3": low, "entire_mod_p3": entire}
    # Extra regression for the frozen *target* residues only; not a theorem.
    if p % 24 in (13,19):
        assert entire == p
        assert (low-p) % p2 == 0
        result["low_defect_div_p2_mod_p"] = ((low-p)//p2) % p
        assert (result["low_defect_div_p2_mod_p"] + result["high_quot"]) % p == 0
    return result


if __name__ == "__main__":
    records = [witness(p) for p in (7,13,19,31,37,43,61,67,73,211,373)]
    assert records[-1]["p"] == 373
    assert (records[-1]["chi6"], records[-1]["t1"], records[-1]["K"],
            records[-1]["high_quot"], records[-1]["high_mod_p3"],
            records[-1]["low_defect_div_p2_mod_p"]) == (-1,41,334,266,37008314,107)
    encoded = json.dumps(records, sort_keys=True, separators=(",", ":"))
    print(encoded)
    print("SHA256=" + hashlib.sha256(encoded.encode()).hexdigest())
    print("D25_WEIGHTED216_HIGH_TAIL_HYPERGEOMETRIC_JET_PASS")
