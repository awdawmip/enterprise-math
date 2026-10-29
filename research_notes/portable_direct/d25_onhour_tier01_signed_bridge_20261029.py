#!/usr/bin/env python3
"""Portable exact p-adic source-typed computation for D25 original signed A216/B2304.

No finite sample is asserted to prove the all-prime bridge.
"""
from math import comb, isqrt


def primes_below(limit: int):
    sieve = bytearray(b'\x01') * limit
    sieve[0:2] = b'\x00\x00'
    for q in range(2, isqrt(limit - 1) + 1):
        if sieve[q]:
            sieve[q*q:limit:q] = b'\x00' * (((limit - 1 - q*q)//q)+1)
    return [p for p in range(5, limit) if sieve[p]]


def source_tiers(p: int):
    """Each index n<p is preserved with its original weight and p-valuation."""
    modulus = p**4
    aa = [0]*4
    bb = [0]*4
    a = b = 1
    for n in range(p):
        av = (2*n)//p + (3*n)//p
        bv = (4*n)//p
        aa[av] = (aa[av] + (6*n+1)*a) % modulus
        bb[bv] = (bb[bv] + (8*n+1)*b) % modulus
        if n+1 < p:
            den = (n+1)**3
            a = (a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*den,-1,modulus)) % modulus
            b = (b*(2*n+1)*(4*n+1)*(4*n+3)*pow(288*den,-1,modulus)) % modulus
    return aa,bb


def raw_tiers(p: int):
    """Independent direct original binomial evaluation, not coefficient recurrence."""
    modulus=p**4
    ia=pow(216,-1,modulus)
    ib=pow(2304,-1,modulus)
    aa=[0]*4
    bb=[0]*4
    pa=pb=1
    for n in range(p):
        av=(2*n)//p+(3*n)//p
        bv=(4*n)//p
        aa[av] = (aa[av]+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pa)%modulus
        bb[bv] = (bb[bv]+(8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*pb)%modulus
        pa=pa*ia%modulus
        pb=pb*ib%modulus
    return aa,bb


def diagnose(p: int, verify_raw: bool=False):
    aa,bb=source_tiers(p)
    if verify_raw:
        assert (aa,bb)==raw_tiers(p), ('raw_mismatch',p)
    q=p**4
    character=1 if p%3==1 else -1
    c=[(aa[i]-2*bb[i]+(p*character if i==0 else 0))%q for i in range(4)]
    assert c[0]%p == 0, ('zeroth not divisible by p',p)
    assert c[1]%p == 0 and c[2]%(p*p)==0 and c[3]%(p**3)==0, ('valuation',p)
    L0=(c[0]//p)%(p**3)
    L1=(c[1]//p)%(p**3)
    assert (L0+L1)%p == 0, ('first carry not cancelling',p)
    E01=((c[0]+c[1])%q)//(p*p)
    Q=c[2]//(p*p)
    D=c[3]//(p**3)
    R=(E01+Q+p*D)%(p*p)
    assert R==0, ('full fourth digit bridge fails',p,R)
    return {'p':p,'class24':p%24,'chi':character,'A':aa,'B':bb,'C':c,
            'L0':L0,'L1':L1,'low_second_jet':E01,'tier2':Q,'tier3':D,
            'first_residues':[L0%p,L1%p],
            'bridge':sum(c)%q}


def main():
    P=primes_below(1500)
    results=[diagnose(p, verify_raw=p in (5,7,11,13,19,31,373)) for p in P]
    targets=[r for r in results if r['class24'] in (13,19)]
    nonzero_low0=[r for r in targets if r['first_residues'][0]!=0]
    both_nonzero=[r for r in targets if r['first_residues'][0] and r['first_residues'][1]]
    print('PASS_EXACT_ORIGINAL_TIER01_FIRST_CARRY',len(results),'primes 5<=p<1500')
    print('TARGET_CLASSES',len(targets),{s:sum(r['class24']==s for r in targets) for s in (13,19)})
    print('TARGET_NONZERO_LOW0',len(nonzero_low0),'TARGET_BOTH_NONZERO',len(both_nonzero))
    print('ALL_FIRST_CARRY_ZERO',all(sum(r['first_residues'])%r['p']==0 for r in results))
    for p in (13,19,373):
        r=next(x for x in results if x['p']==p)
        print('CERT',p,'C0=',r['C'][0],'C1=',r['C'][1],
              'L0=',r['L0'],'L1=',r['L1'],'L0%p=',r['first_residues'][0],
              'L1%p=',r['first_residues'][1],
              'C01/p2=',r['low_second_jet'],'Q=',r['tier2'],'D=',r['tier3'],
              'bridge_mod_p4=',r['bridge'])


if __name__=='__main__':
    main()
