#!/usr/bin/env python3
"""Original integer-binomial W weighted p^3 stress test (portable, not native H0/B0).
Original W term = (6k+1)*binom(3k,k)*binom(2k,k)^2 / 216^k.
The modular recurrence divides only by (k+1)<p, hence valid mod p^3.
"""
from math import isqrt
import json

def primes_upto(n):
    a=bytearray(b'\x01')*(n+1);a[0:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if a[d]:
            a[d*d:n+1:d]=b'\x00'*(((n-d*d)//d)+1)
    return [p for p in range(5,n+1) if a[p] and p%24 in (13,19)]

def check_p(p):
    P=p*p*p
    x=1
    half=(p-1)//2
    Wfull=1
    Whalf=1
    for k in range(1,p):
        # A_k/A_{k-1} from factorial identity; denominator k is a unit.
        num=((2*k)*(2*k-1)*(3*k)*(3*k-1)*(3*k-2))%P
        x=x*num*pow(216*pow(k,5,P),-1,P)%P
        term=(6*k+1)*x%P
        Wfull=(Wfull+term)%P
        if k<=half: Whalf=(Whalf+term)%P
    tail=(Wfull-Whalf)%P
    assert tail%(p*p)==0, ('tail unexpected',p,tail)
    B2=(tail//(p*p))%p
    signed_second=((Whalf-p)//(p*p)+B2)%p if (Whalf-p)%(p*p)==0 else None
    return {'p':p,'full_W_mod_p3':Wfull,'full_minus_p_mod_p3':(Wfull-p)%P,
            'half_W_mod_p3':Whalf,'high_B2_mod_p':B2,
            'half_divisibility':(Whalf-p)%(p*p)==0,
            'signed_second_residue':signed_second}

if __name__=='__main__':
    bound=20000
    ps=primes_upto(bound)
    out=[check_p(p) for p in ps]
    bad=[r for r in out if r['full_minus_p_mod_p3'] or r['signed_second_residue'] is None or r['signed_second_residue']]
    result={'schema':'D25_AUTHOR_ORIGINAL_W_P3_STRESSTEST_V1',
            'status':'AUTHOR_EXECUTED_EXACT_FINITE_ONLY_UNREVIEWED_NOT_ADMITTED',
            'prime_limit':bound,'target_prime_count':len(ps),
            'all_full_w_equals_p_mod_p3':len(bad)==0,
            'exceptions':bad[:10],
            'selected':[r for r in out if r['p'] in (13,19,37,373,1171,10009,10039,19997)],
            'coverage':'all p<=20000 prime with p mod24 13 or 19',
            'original_W_term':'(6k+1)*C(3k,k)*C(2k,k)^2 /216^k',
            'derived_recurrence':'A_k=A_{k-1}*(2k)(2k-1)(3k)(3k-1)(3k-2)/(216 k^5)',
            'modulus':'p^3','universal_proof':False,'native_benchmark_executed':False}
    print(json.dumps(result,indent=2))
    assert not bad, f'{len(bad)} nonzero residues'
