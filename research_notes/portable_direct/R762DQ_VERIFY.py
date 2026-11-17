#!/usr/bin/env python3
"""R762DQ: exact integer BRC convolution and one-axis 3-adic checks.
No floating point, randomness or external packages; candidate pi_XZ observer only.
"""
import json
from math import comb, gcd
from functools import reduce

AGGREGATED = ((0,0,1),(1,0,2),(0,1,2),(1,1,1))
NAMED = ((0,0),(1,0),(0,1),(1,0),(0,1),(1,1))

def advance(old, q, moves):
    out = [[0]*q for _ in range(q)]
    for i, row in enumerate(old):
        for j, v in enumerate(row):
            if v:
                for di,dj,w in moves:
                    out[(i+di)%q][(j+dj)%q] += v*w
    return out

def content(a):
    return reduce(gcd,(v for row in a for v in row),0)

def pow_cyclic_x(q, power):
    # coefficient of (X-1)^power modulo X^q-1, exact integers
    out = [0]*q
    for i in range(power+1):
        out[i%q] += comb(power,i)*(-1)**(power-i)
    return out

def expected(n,d):
    if n < 3*d: return 1
    if n < 5*d: return 9
    if n < 7*d: return 81
    return None

def check(q):
    assert q >= 9 and q%3 == 0
    d=q//3
    a=[[0]*q for _ in range(q)]
    a[0][0]=1
    cchecks=0; mchecks=0; samples={}
    selected = {1,3*d-1,3*d,5*d-1,5*d,5*d+1,6*d-1,6*d,7*d-1,7*d}
    for n in range(1,7*d+1):
        a=advance(a,q,AGGREGATED)
        assert sum(map(sum,a)) == 6**n, ('mass',q,n)
        mchecks+=1
        c=content(a)
        want=expected(n,d)
        if want is not None:
            assert c==want, ('content',q,n,c,want)
            cchecks+=1
        if n in selected:
            samples[str(n)]=str(c)
    # Verify the mod-3 1D relation x^Q/3 = -x^d(1+x^d).
    xq=pow_cyclic_x(q,q)
    assert all(v%3==0 for v in xq)
    mod3=[(v//3)%3 for v in xq]
    right=pow_cyclic_x(q,d)
    right2=pow_cyclic_x(q,2*d)
    assert mod3 == [(-(right[i]+right2[i]))%3 for i in range(q)], ('xQ/3',q)
    x5=pow_cyclic_x(q,5*d)
    assert all(v%9==0 for v in x5),('x5d /9',q)
    # Check named branch multiplicity equals aggregated after two rounds.
    b=[[0]*q for _ in range(q)]; b[0][0]=1
    v=[[0]*q for _ in range(q)]; v[0][0]=1
    for _ in range(2):
        b=advance(b,q,AGGREGATED)
        v=advance(v,q,tuple((i,j,1) for i,j in NAMED))
    assert b==v,('named projection',q)
    return {'Q':q,'d':d,'exponents_checked':[1,7*d],
            'sharp_content_checks':cchecks,'exact_mass_checks':mchecks,
            'one_axis_xQ_leading_test':True,
            'one_axis_x5d_divisible_by_9':True,
            'named_branch_projection_two_rounds':True,
            'selected_coefficient_contents':samples}

if __name__=='__main__':
    out={'theorem':'R762DQ','status':'PASS','method':'integer cyclic-convolution and binomial congruences',
         'claims':'for Q=3^a, a>=2, c_XZ(n)=1 on [0,3d), 9 on [3d,5d), 81 on [5d,7d)',
         'independent_review':'NOT_REVIEWED',
         'verification_scope':'finite Q=9,27,81; all integers; general result needs human proof',
         'results':[check(q) for q in (9,27,81)]}
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
