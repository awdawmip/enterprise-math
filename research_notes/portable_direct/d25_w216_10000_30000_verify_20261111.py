#!/usr/bin/env python3
"""Exact original W216 p^4 finite certificate.
Frozen science: c47e13e4aba0e006366f989d6334d443f6333ae3
Author-side / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
"""
import hashlib
import json
import math
from pathlib import Path

def primes_to(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[0:2] = b'\x00\x00'
    for d in range(2,math.isqrt(n)+1):
        if sieve[d]:
            sieve[d*d:n+1:d] = b'\x00'*((n-d*d)//d+1)
    return [p for p in range(n+1) if sieve[p]]

def original_w(p, exponent=4):
    """a_k=(2k)!(3k)!/(216^k(k!)^5).
    a_(k+1)/a_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3).
    All denominators used here are p-units: 1<=k<p.
    """
    q = p**exponent
    inv = [0]*p
    inv[1] = 1
    for j in range(2,p):
        inv[j] = (-(q//j)*inv[q%j])%q
    inv36 = pow(36,-1,q)
    a, W = 1, 1
    for k in range(1,p):
        r = k-1
        a = (a*(2*r+1)*(3*r+1)*(3*r+2)*inv36*pow(inv[k],3,q))%q
        W = (W+(6*k+1)*a)%q
    return W

def independently_factorial(p,exponent=4):
    """Independent p-stripped factorial, not the coefficient recurrence."""
    q = p**exponent
    U = [1]*(3*p)
    for j in range(1,3*p):
        U[j] = U[j-1]*(j//p if j%p==0 else j)%q
    F = [1]*p
    for j in range(1,p):
        F[j] = F[j-1]*j%q
    W = 0
    for k in range(p):
        v = (2*k)//p+(3*k)//p
        ak = (p**v*U[2*k]*U[3*k]*pow(216,-k,q)*pow(F[k],-5,q))%q
        W = (W+(6*k+1)*ak)%q
    return W

def run(output_file=None):
    target = [p for p in primes_to(30000) if 10000<p and p%24 in (13,19)]
    out = []
    for p in target:
        w = original_w(p,4)
        assert w%p**3 == p, ('ORIGINAL_P3_COUNTEREXAMPLE',p,w)
        out.append((p,((w-p)//p**3)%p))
    sample = [target[0],target[len(target)//2],target[-1]]
    for p in sample:
        assert original_w(p,4)==independently_factorial(p,4),('INDEPENDENT_MISMATCH',p)
    zeros=[p for p,e in out if e==0]
    assert len(out)==503
    cert={'schema':'D25_ORIGINAL_W216_10000_30000_FINITE_EXACT_V1',
          'science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
          'status':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE_H0B0',
          'prime_range':'10000 < p <= 30000',
          'target_mod24':[13,19],
          'congruence_checked':'W_p == p mod p^3',
          'digit':'epsilon_p=(W_p-p)/p^3 mod p',
          'all_503_prime_records':[{'p':p,'epsilon':e} for p,e in out],
          'independent_factorial_crosschecks':sample,
          'extra_p4_lift_primes':zeros,
          'program':'d25_w216_10000_30000_verify_20261111.py'}
    sha=None
    if output_file:
        Path(output_file).write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        sha=hashlib.sha256(Path(output_file).read_bytes()).hexdigest()
    return {'count':len(out),'p3_failures':0,'p4_extra_lift_zero_count':len(zeros),
            'factorial_crosschecks':sample,'first_records':out[:4],
            'last_records':out[-4:],'full_records_json_sha256':sha}

if __name__=='__main__':
    print(json.dumps(run('d25_w216_10000_30000_full_records.json'),sort_keys=True))
