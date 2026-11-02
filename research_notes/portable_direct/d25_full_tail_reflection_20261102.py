#!/usr/bin/env python3
"""Original W216 upper-tail (v_p >=3) reflection modulo p^4: exact integers."""
import json
from fractions import Fraction


def primes_up_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i] = b'\x00' * len(sieve[i*i::i])
    return [p for p in range(5, n+1) if sieve[p]]


def check(p):
    mod = p**4
    cap = 2*p//3
    R = (p-3)//3
    assert p-1-R == cap+1
    a = 1
    pow_two_inv = 1
    inv2 = pow(2, -1, mod)
    tail = 0
    terms = {}
    for k in range(p):
        if k:
            a = (a*(2*k-1)*(3*k-2)*(3*k-1)*pow(18*k**3,-1,mod))%mod
            pow_two_inv = (pow_two_inv*inv2)%mod
        term = ((6*k+1)*a*pow_two_inv)%mod
        if k>cap:
            assert term%(p**3)==0, (p,k,term)
            tail = (tail+term)%mod
            terms[k] = (term//p**3)%p
    d=1
    reduced=0
    last_digit=None
    for r in range(R+1):
        predicted = (6*r+5)*d%p
        assert predicted == terms[p-1-r], (p,r,predicted,terms[p-1-r])
        if r==0: last_digit=predicted
        reduced = (reduced+predicted)%p
        if r<R:
            denom=(2*r+3)*(3*r+5)*(3*r+4)
            assert denom%p
            d = d*36*(r+1)**3*pow(denom,-1,p)%p
    assert tail == (p**3*reduced)%mod, (p,tail,reduced)
    assert last_digit==5%p
    return {'p':p,'cutoff':cap,'tail_terms':R+1,'tail_mod_p4':tail,
            'tail_normalized_mod_p':reduced,'last_term_digit':last_digit}


def main():
    ps=primes_up_to(3000)
    rows=[check(p) for p in ps]
    out={
      'schema':'D25_FULL_UPPER_TAIL_P4_REFLECTION_CHECK_V1',
      'date':'2026-11-02',
      'model':'original W216 with original 6k+1 weights',
      'primes_to':3000,'primes_tested':len(ps),
      'tail_terms_checked':sum(x['tail_terms'] for x in rows),
      'assertions_passed':True,
      'samples':[x for x in rows if x['p'] in (5,7,11,13,19,37,43,109,373,1171)],
      'native_H0B0':'NOT_EXECUTED',
      'formal_mathematical_admission':'NOT_ADMITTED',
      'finite_tests_are_not_universal_proof':True
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
