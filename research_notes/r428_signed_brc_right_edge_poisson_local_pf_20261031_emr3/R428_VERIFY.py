#!/usr/bin/env python3
"""R428 author-side reproducible exact checks for signed-BRC right-edge Poisson limit.
Finite checks support, but do not replace, the analytic asymptotic and LGV proof.
Standard library only. No BRC-native/X6 attribution is asserted.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def cat(n):
    return C(2*n, n)//(n+1)

def raw_delta(r, s):
    return sum(C(r-s, t)*(C(2*s, r-2*t)-C(2*s, r-2*t-1)) for t in range(r-s+1))

def alt_delta(r, s):
    return sum(C(s-1, ell)*(2**ell)*cat((r-1-ell)//2)
               for ell in range(s) if r-1-ell >= 0 and (r-1-ell)%2 == 0)

def H(r, s):
    return C(r+s, 2*s)*raw_delta(r, s) if 2 <= s <= r else 0

def right(r, j):
    return H(r, r-j)

def det(M):
    n=len(M)
    ans=0
    for p in permutations(range(n)):
        sign=-1 if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2 else 1
        val=sign
        for i in range(n):
            val*=M[i][p[i]]
        ans+=val
    return ans

def rat(r, j):
    if j == 0:
        return Fraction(1)
    if j == 1:
        return Fraction(r-2)
    if j == 2:
        return Fraction((r-1)*(r*r-5*r+9), 2*r-1)
    if j == 3:
        return Fraction((r-4)*(r-2)*(r*r-5*r+15), 3*(2*r-1))
    raise ValueError(j)

def right_edge(r):
    b0,b1,b2,b3=[right(r,j) for j in range(4)]
    return b1**3-2*b0*b1*b2+b0*b0*b3

def test():
    independent=0
    for r in range(4,81):
        for s in range(2,r+1):
            assert raw_delta(r,s)==alt_delta(r,s),('independent signed-vs-Catalan',r,s)
            independent+=1
    ratio=0
    for r in range(4,201):
        for j in range(4):
            assert Fraction(right(r,j),cat(r))==rat(r,j),('edge ratio',r,j)
            ratio+=1
        expected=cat(r)**3*Fraction((r-2)*(r+2)*(r*r-2*r-9),3*(2*r-1))
        assert right_edge(r)==expected,('edge determinant',r)
        assert (right_edge(r)<0 if r==4 else right_edge(r)>0),('edge sign',r)
    lim_checks=0
    limit_pascal=0
    local_checks={}
    admissible=[]
    for k in range(1,5):
        for u in combinations(range(7),k):
            for v in combinations(range(7),k):
                if all(v[i]>=u[i] for i in range(k)):
                    admissible.append((u,v))
                    pas=det([[C(vj,ui) for vj in v] for ui in u])
                    assert pas>0,('Pascal strict',u,v)
                    limit_pascal+=1
    for r in (8,16,40,80):
        arr=[right(r,h) for h in range(7)]
        count=0
        for u,v in admissible:
            D=det([[arr[vj-ui] if vj>=ui else 0 for vj in v] for ui in u])
            assert D>0,('boundary minor',r,u,v,D)
            count+=1
        local_checks[str(r)]=count
    errors={}
    for r in (64,128,512):
        fracs=[]
        for j in range(7):
            z=Fraction(right(r,j),cat(r)*r**j)
            error=z-Fraction(1,factorial(j))
            fracs.append({'j':j,'error_numerator':str(error.numerator),
                          'error_denominator':str(error.denominator)})
            lim_checks+=1
        errors[str(r)]=fracs
    summary={
        'schema':'R428_SIGNED_BRC_BOUNDARY_POISSON_EVIDENCE_V1',
        'status':'EXACT_FINITE_CHECKS_NOT_ANALYTIC_PROOF',
        'source':'R427 signed BRC definition + independent direct binomial formula',
        'original_vs_catalan_checks':independent,
        'right_edge_ratio_checks':ratio,
        'right_edge_determinant_checks':197,
        'r4_negative_right_edge':right_edge(4),
        'r5_positive_right_edge':right_edge(5),
        'pascal_strict_minors_checked':limit_pascal,
        'right_edge_minor_checks':local_checks,
        'normalized_r_to_factorial_errors':errors,
        'unbounded_argument':'analytically: fixed-j signed-difference limit; LGV Pascal determinant positivity'
    }
    data=json.dumps(summary,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    target=Path(__file__).with_name('R428_EVIDENCE.json')
    target.write_text(data,encoding='utf-8')
    print('R428_EXACT_PASS',independent,ratio,197,limit_pascal,sum(local_checks.values()),
          hashlib.sha256(data.encode()).hexdigest(),flush=True)

if __name__=='__main__':
    test()
