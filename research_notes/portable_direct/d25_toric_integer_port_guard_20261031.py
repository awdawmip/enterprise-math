#!/usr/bin/env python3
"""Exact integer discriminating test for the unreviewed low-jet toric port.
No formal Source research admission or native H0/B0 simulation.
"""

def weighted_scaled(l: int, base: int=2, slope: int=6):
    """return base^(2l)*sum_{n=0}^{2l}(slope*n+1)*(-1/base)^n
    *binom(3l,n)*binom(2l,n)*binom(4l,n), by exact recurrences.
    """
    assert l>=0 and base>=2
    m=2*l; h=3*l; q=4*l
    term=base**m
    value=0
    for n in range(m+1):
        value+=(slope*n+1)*term
        if n<m:
            num=term*(h-n)*(m-n)*(q-n)
            den=base*(n+1)**3
            assert num%den==0,('noninteger term',l,base,n)
            term=-(num//den)
    return value


def toric_companion_scaled(l: int):
    """Independent coefficient expansion after (1-xy/2)^(4l-1) factorization."""
    from math import comb
    m, h, q=2*l,3*l,4*l
    return sum((-1)**n*2**(m-n)*comb(h,n)*comb(m,n)
               *(comb(q-1,n)+(6*q+1)*(comb(q-1,n-1) if n else 0))
               for n in range(m+1))

def run(limit=450):
    composite=0; squared_obstructions=0; toric_checked=0
    anchors={1,2,3,4,8,20,28,40,50,100,250,400,450}
    for l in range(1,limit+1):
        p=6*l+1
        s=weighted_scaled(l)
        assert s%p==0,('PORT_DIVISIBILITY_FAIL',l,p,s%p)
        if s%(p*p):squared_obstructions+=1
        for d in range(2,1+int(p**0.5)):
            if p%d==0: composite+=1;break
        if l <= 30 or l in anchors:
            assert s == toric_companion_scaled(l), ("TORIC_COEFFICIENT",l)
            toric_checked+=1
        if l in anchors:
            print('LENGTH',l,'MODULUS',p,'S_OVER_P_MOD_P',(s//p)%p,'S_MOD_P2',s%(p*p))
    s2=weighted_scaled(2)
    from math import comb
    explicit=sum((6*n+1)*(-1)**n*2**(4-n)*comb(6,n)*comb(4,n)*comb(8,n) for n in range(5))
    assert s2==explicit==-23686, (s2,explicit)
    assert s2//13==-1822 and (s2//13)%13==11
    failed_base3 = [(l, weighted_scaled(l,3)% (6*l+1)) for l in range(1,15) if weighted_scaled(l,3)%(6*l+1)]
    failed_slope4 = [(l, weighted_scaled(l,2,4)%(6*l+1)) for l in range(1,15) if weighted_scaled(l,2,4)%(6*l+1)]
    print('TESTED_L',limit,'COMPOSITE_MODULI',composite,'NO_DIVISIBILITY_FAILURES')
    print('INDEPENDENT_TORIC_COEFFICIENT_CHECKS',toric_checked)
    print('SHARP_MOD_P2_NONZERO_CASES',squared_obstructions)
    print('BASE3_NEGATIVE_CONTROLS',failed_base3[:5])
    print('SLOPE4_NEGATIVE_CONTROLS',failed_slope4[:5])
    print('PASS_EXACT_TORIC_COMPOSITE_MODULUS_BOUND_20261031')
if __name__=='__main__':run()
