#!/usr/bin/env python3
"""Exact original W216/V2304 AF4 grade-three reflection test, Python stdlib only."""
from math import comb
import json

WITNESSES = (5, 7, 11, 13, 19, 37, 43, 73, 109, 373, 997)

def prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** .5) + 1))

def reciprocal(p):
    f = [1]
    for k in range(1, p):
        f.append(f[-1] * k % p)
    wa = vc = 0
    for j in range(1, p // 3 + 1):
        if 3*j >= p: continue
        Aj = f[2*j] * f[3*j] * pow(f[j], -5, p) * pow(216, -j, p) % p
        wa = (wa - (1-6*j) * pow(18*j**3 * Aj, -1, p)) % p
    for j in range(1, p // 4 + 1):
        if 4*j >= p: continue
        Cj = f[4*j] * pow(f[j], -4, p) * pow(2304, -j, p) % p
        vc = (vc - (1-8*j) * pow(96*j**3 * Cj, -1, p)) % p
    return wa, vc, (wa-2*vc) % p

def original_grades(p):
    modulus = p**4
    i216, i2304 = pow(216, -1, modulus), pow(2304, -1, modulus)
    wa, vc = [0]*4, [0]*4
    for n in range(p):
        ga, gc = (2*n)//p + (3*n)//p, (4*n)//p
        An = comb(2*n, n)**2 * comb(3*n, n)
        Cn = comb(4*n, 2*n) * comb(2*n, n)**2
        wa[ga] = (wa[ga] + (6*n+1)*An*pow(i216, n, modulus)) % modulus
        vc[gc] = (vc[gc] + (8*n+1)*Cn*pow(i2304, n, modulus)) % modulus
    return wa, vc

def run(p):
    assert prime(p) and p > 3
    recip = reciprocal(p)
    wa, vc = original_grades(p)
    assert wa[3] % p**3 == vc[3] % p**3 == 0
    direct = (wa[3]//p**3, vc[3]//p**3, ((wa[3]-2*vc[3]) % p**4)//p**3)
    assert recip == direct, (p, recip, direct)
    chi = 1 if p % 3 == 1 else -1
    low = (sum(wa[:3])-2*sum(vc[:3])+chi*p) % p**4
    affine = (low+wa[3]-2*vc[3]) % p**4
    row = {"p":p,"W3_div_p3":direct[0],"V3_div_p3":direct[1],
           "L_grade3":direct[2],"low_div_p3":low//p**3 if low%p**3==0 else None,
           "affine_mod_p4":affine}
    if p in (13,19,37,43,73,109,373):
        assert low%p**3==0 and affine==0, row
    if p==373:
        assert wa[3]==14426842526 and vc[3]==6175518923 and low==17281073961
        assert row["L_grade3"]==40 and row["low_div_p3"]==333
    return row

if __name__ == "__main__":
    rows = [run(p) for p in WITNESSES]
    print(json.dumps({"schema":"D25_AF4_GRADE3_WITNESS_V1",
                      "proof":"general factorial reflection, above exact finite regression",
                      "witness_count":len(rows), "rows":rows}, indent=2))
    print("PASS: exact direct-binomial grade3 vs reciprocal identity, 11 primes")
