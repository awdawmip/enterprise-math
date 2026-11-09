#!/usr/bin/env python3
"""Original 2304 model grade-2 cancellation and AF4 carry diagnostic.

Exact integer modular arithmetic, original coefficients and weights.
Mathematical claims: reduction theorem is proved algebraically; vanishing,
root simplicity, and all-prime carry are finite observations only.
"""
import hashlib
import json
from math import comb, isqrt


def primes_upto(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00' * ((limit-p*p)//p + 1)
    return [p for p in range(5, limit+1) if sieve[p]]


def poly_grade2(p):
    """Compute normalized P_N(1), derivative independently modulo p."""
    lo = (p+1)//2
    hi = (3*p-1)//4
    N = hi-lo
    f = 1
    value = 0
    derivative = 0
    for j in range(N+1):
        t = ((8*j+5)*f) % p
        value = (value + t) % p
        derivative = (derivative + j*t) % p
        if j < N:
            n = lo+j
            f = f*(4*n+1)*(4*n+3)*(2*n+1)*pow(288*(n+1)**3,-1,p)%p
    return N,value,derivative


def original_grade3(p):
    """Original W=216 and V=2304 coefficient recurrences modulo p^3."""
    mod = p**3
    a = c = 1
    w0w1 = v0v1 = w2 = v2 = 0
    C_first = None
    n0=(p+1)//2
    for n in range(p):
        ga=(2*n)//p+(3*n)//p
        gc=(4*n)//p
        if ga in (0,1):
            w0w1 = (w0w1 + (6*n+1)*a)%mod
        elif ga==2:
            w2 = (w2 + (6*n+1)*a)%mod
        if gc in (0,1):
            v0v1 = (v0v1 + (8*n+1)*c)%mod
        elif gc==2:
            v2 = (v2 + (8*n+1)*c)%mod
        if n==n0:
            assert c%p**2==0
            C_first=(c//p**2)%p
        if n+1<p:
            d=pow(n+1,-1,mod)**3%mod
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*d*pow(36,-1,mod)%mod
            c=c*(4*n+1)*(4*n+3)*(2*n+1)*d*pow(288,-1,mod)%mod
    chi = 1 if pow(p-3,(p-1)//2,p)==1 else -1
    low=(w0w1-2*v0v1+p*chi)%mod
    mid=(w2-2*v2)%mod
    assert low%p**2==0 and mid%p**2==0 and v2%p**2==0
    return {
        'Kp':C_first,
        'C_grade2_p2':(v2//p**2)%p,
        'A_grade2_p2':(w2//p**2)%p,
        'ell0':low//p**2,
        'b0':mid//p**2,
        'balance_p3':(low+mid)%mod,
    }


def direct_binomial(p):
    """Independent original integer-binomial 2304 grade-2 evaluation."""
    mod = p**3
    total=0
    first=None
    for n in range((p+1)//2,(3*p-1)//4+1):
        c=comb(4*n,2*n)*comb(2*n,n)**2*pow(2304,-n,mod)%mod
        if first is None:
            first=c//p**2
        total=(total+(8*n+1)*c)%mod
    return first, total//p**2


def main(limit=10000):
    ps=primes_upto(limit)
    records=[]
    failures=[]
    samples={}
    for p in ps:
        N,P,dP=poly_grade2(p)
        q=original_grade3(p)
        carry=(q['ell0']+q['b0'])//p
        item=(p,N,q['ell0'],q['b0'],dP,q['Kp'])
        records.append(item)
        if P!=0 or q['C_grade2_p2']!=(q['Kp']*P)%p or q['balance_p3']!=0 or carry!=1 or (dP==0 and p>5):
            failures.append((p,P,dP,q,carry))
        if p in [5,7,13,19,37,43,73,373,9973]:
            samples[str(p)]={'N':N,'P1':P,'Pprime1':dP,'carry':carry, **q}
        if p in [13,19,373]:
            one,direct=direct_binomial(p)
            assert (one,direct)==(q['Kp'],q['C_grade2_p2'])
    raw=';'.join(','.join(str(z) for z in row) for row in records)
    result={
        'schema':'EM_D25_C_GRADE2_FINITE_CHECK_20261109',
        'limit':limit,'count_primes_gt3':len(ps),
        'original_coefficients':'W=(6n+1)(2n)!(3n)!/(n!^5*216^n); V=(8n+1)(4n)!/(n!^4*2304^n)',
        'p2_C_grade2_vanish_all_tested':all(r[0] not in [f[0] for f in failures] for r in records),
        'P_N_1_zero_count':len(ps)-sum(1 for f in failures if f[1]!=0),
        'P_N_derivative_nonzero_p_gt5_count':len(ps)-1-sum(1 for f in failures if f[2]==0 and f[0]>5),
        'carry1_count':sum(1 for row in records if (row[2]+row[3])//row[0]==1),
        'failures':failures,
        'samples':samples,
        'records_sha256':hashlib.sha256(raw.encode()).hexdigest(),
        'records_encoding':'p,N,ell0,b0,Pprime1,Kp; semicolon-separated in increasing p',
        'independent_direct_binomial_crosschecks':[13,19,373],
        'proof_status':'polynomial reduction algebraic; zero/simple-root/carry finite numerical observations',
        'native_H0B0':'NOT_EXECUTED',
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    assert not failures
    return result


if __name__=='__main__':
    import sys
    main(int(sys.argv[1]) if len(sys.argv)>1 else 10000)
