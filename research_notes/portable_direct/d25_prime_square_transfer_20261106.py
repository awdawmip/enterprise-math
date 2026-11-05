"""D25 prime-square palindrome transport: exact finite witness checker.
Depends only on same-directory d25_lucas_q2_factorization_20261106.py.
Native CM original experiment NOT_RUN.
"""
from math import comb
from d25_lucas_q2_factorization_20261106 import (
    two_digit_certificate, original_shadow, primes
)

def high_observer(t,q):
    a=-pow(2,-1,q)%q
    return sum(pow(a,h,q)*comb(2*t,h)*comb(3*t,h)*comb(4*t,h)
               for h in range(2*t+1))%q

def run():
    tested=0
    for q in (5,7,11,13,19,23,31,37):
        n0=(q*q-1)//6
        base=two_digit_certificate(n0,q)
        assert base['L']%q==base['result']==0
        assert sorted(base['M'])==sorted(base['s'])
        for t in range(4):
            now=two_digit_certificate(n0+t*q*q,q)
            v=high_observer(t,q)
            assert now['A']==base['A'] and now['B']==base['B']
            assert now['T']%q==base['T']%q*v%q
            assert now['T1']%q==base['T1']%q*v%q
            assert now['result']==0
            tested+=1
    print('TRANSFER_CERTIFICATE_CHECK PASS',tested)
    bases=0
    for q in primes(1000):
        n0=(q*q-1)//6
        x=two_digit_certificate(n0,q)
        assert x['L']%q==0 and x['result']==0
        assert sorted(x['M'])==sorted(x['s'])
        bases+=1
    print('CERTIFIED_BASE_CASES_WITH_L_ZERO PASS',bases)
    direct=0
    for q in (5,7,11):
        n0=(q*q-1)//6
        for t in (1,2):
            n=n0+t*q*q
            assert original_shadow(n,q*q)==two_digit_certificate(n,q)['result']==0
            direct+=1
    print('LARGE_N_INDEPENDENT_ORIGINAL_SUM_CHECK PASS',direct)

if __name__=='__main__':run()
