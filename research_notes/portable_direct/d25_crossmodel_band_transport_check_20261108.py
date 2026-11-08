#!/usr/bin/env python3
"""D25 exact original weighted-216/2304 comparison; source-graded p-adic arithmetic.
Author-side checker, not native H0/B0. No math claims beyond the declared bounds.
"""
from math import comb, factorial, isqrt
import json
import sys

def primes(limit):
    if limit < 5:
        return []
    table = bytearray([1]) * (limit + 1)
    table[:2] = b'\x00\x00'
    for q in range(2, isqrt(limit) + 1):
        if table[q]:
            table[q*q::q] = b'\x00' * (1 + (limit-q*q)//q)
    return [p for p in range(5, limit + 1) if table[p]]

def bands(p, precision=4):
    assert p > 3 and precision >= 3
    mod = p**precision
    fact = [1]*(4*p-3)
    valuation = [0]*(4*p-3)
    for k in range(1,4*p-3):
        unit = k
        exponent = 0
        while unit % p == 0:
            unit //= p
            exponent += 1
        fact[k] = fact[k-1]*unit % mod
        valuation[k] = valuation[k-1]+exponent
    inv_fact = [1]*p
    inv_fact[p-1] = pow(fact[p-1],-1,mod)
    for n in range(p-1,0,-1):
        inv_fact[n-1] = inv_fact[n]*n%mod
    inverse_bases = [pow(216,-1,mod),pow(2304,-1,mod)]
    powers = [1,1]
    output = [[0]*precision, [0]*precision]
    for n in range(p):
        e_w = valuation[2*n]+valuation[3*n]
        e_v = valuation[4*n]
        if e_w < precision:
            term = ((6*n+1)*fact[2*n]*fact[3*n]*pow(inv_fact[n],5,mod)
                    *powers[0]*pow(p,e_w,mod)) % mod
            output[0][e_w] = (output[0][e_w]+term)%mod
        if e_v < precision:
            term = ((8*n+1)*fact[4*n]*pow(inv_fact[n],4,mod)
                    *powers[1]*pow(p,e_v,mod)) % mod
            output[1][e_v] = (output[1][e_v]+term)%mod
        powers[0] = powers[0]*inverse_bases[0]%mod
        powers[1] = powers[1]*inverse_bases[1]%mod
    return [sum(v)%mod for v in output],output

def direct_original(p, precision=4):
    mod=p**precision
    w=v=0
    for n in range(p):
        w=(w+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod))%mod
        v=(v+(8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pow(2304,-n,mod))%mod
    return (w,v)

def independent_v_grade2(p):
    """Original V e=2 normalized modulo p, independently via shifted recurrence."""
    start=(p+1)//2
    stop=(3*p-1)//4
    if stop<start:
        return 0
    # 2 factorial blocks times the remaining (4*start-2*p)!.
    current=(2*factorial(4*start-2*p)*pow(factorial(start),-4,p)
             *pow(2304,-start,p))%p
    aggregate=0
    for r in range(stop-start+1):
        aggregate=(aggregate+(8*r+5)*current)%p
        if r<stop-start:
            numerator=(4*r+3)*(4*r+4)*(4*r+5)*(4*r+6)
            denominator=2304*pow((2*r+3)*pow(2,-1,p)%p,4,p)
            current=current*numerator*pow(denominator,-1,p)%p
    return aggregate

def scan(limit=2000):
    target=0
    target_nonzero_w2=0
    v2_zero=0
    character_fail=[]
    cross_model_fail=[]
    v2_fail=[]
    examples={}
    primes_checked=primes(limit)
    for p in primes_checked:
        (w,v),grade=bands(p,4)
        if (w-v)%(p**3):
            cross_model_fail.append(p)
        if (w-(p if p%3==1 else -p))%(p**3):
            character_fail.append(p)
        w2=grade[0][2]//(p*p)%p
        v2=grade[1][2]//(p*p)%p
        independent=independent_v_grade2(p)
        assert independent==v2, (p,independent,v2)
        if v2==0:
            v2_zero+=1
        else:
            v2_fail.append((p,v2))
        if p%24 in (13,19):
            target+=1
            if w2:
                target_nonzero_w2+=1
        if p in (5,11,13,19,37,43,211,373):
            assert (w,v)==direct_original(p,4), ("direct-mismatch",p)
            examples[str(p)]={
                "W_mod_p4":w,"V_mod_p4":v,
                "W_grade2_digit":w2,"V_grade2_digit":v2,
                "W_bands_mod_p3":[x%p**3 for x in grade[0][:3]],
                "V_bands_mod_p3":[x%p**3 for x in grade[1][:3]],
                "W_minus_V_over_p3_modp":((w-v)//p**3)%p if (w-v)%p**3==0 else None
            }
    return {
        "max_prime":limit,
        "checked_prime_count":len(primes_checked),
        "frozen_target_count":target,
        "frozen_target_nonzero_W_grade2":target_nonzero_w2,
        "zero_V_grade2_count":v2_zero,
        "nonzero_V_grade2":v2_fail[:20],
        "W_character_failures":character_fail[:20],
        "W_minus_V_mod_p3_failures":cross_model_fail[:20],
        "examples":examples
    }

if __name__=="__main__":
    print(json.dumps(scan(int(sys.argv[1]) if len(sys.argv)>1 else 2000),
                     ensure_ascii=False,indent=2,sort_keys=True))
