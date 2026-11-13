#!/usr/bin/env python3
"""Exact R134 finite arithmetic checks; standard-library Fraction only."""
from fractions import Fraction as Q
from math import gcd
import json

def word(K,m,t):
    return ''.join(str(((K+i)*t).__floor__()-((K+i-1)*t).__floor__()) for i in range(m))

def direct(K,m,t):
    def frac(z): return z-z.__floor__()
    return ''.join('1' if frac((K+i)*t)<t else '0' for i in range(m))

def farey(m):
    return sorted({Q(p,q) for q in range(1,m+1) for p in range(q+1)})

def classical(m):
    out=set()
    ff=farey(m)
    for a,b in zip(ff,ff[1:]):
        alpha=(a+b)/2
        cuts=sorted({Q(0),Q(1)}|{(-j*alpha)%1 for j in range(m+1)})
        for u,v in zip(cuts,cuts[1:]):
            rho=(u+v)/2
            out.add(''.join(str((rho+(i+1)*alpha).__floor__()-(rho+i*alpha).__floor__()) for i in range(m)))
    return out

def phase(K,m):
    cuts={Q(0),Q(1)}
    for n in range(K-1,K+m):
        if n>0:cuts.update(Q(p,n) for p in range(1,n))
    cc=sorted(cuts)
    return {word(K,m,t) for t in cc[1:-1]}|{word(K,m,(a+b)/2) for a,b in zip(cc,cc[1:])}

def phi(n):
    return sum(gcd(j,n)==1 for j in range(1,n+1))

def F(m):
    return 1+sum((m+1-q)*phi(q) for q in range(1,m+1))

def balanced(w):
    for ell in range(1,len(w)+1):
        x=[w[i:i+ell].count('1') for i in range(len(w)-ell+1)]
        if max(x)-min(x)>1:return False
    return True

def run():
    counts=[]; arith=0; large=0; total=0
    for m in range(2,10):
        full=classical(m)
        assert len(full)==F(m)
        assert all(balanced(w) for w in full)
        total+=len(full)
        sizes=[]; first=None
        for K in range(1,41 if m<=7 else 26):
            actual=phase(K,m)
            assert actual<=full
            if len(actual)==len(full) and first is None:first=K
            sizes.append(len(actual))
            for t in (Q(1,K+m+1),Q(1,2*K+m+3),Q(K,K+m+2),Q(1,3),Q(2,3)):
                if 0<t<1:
                    assert word(K,m,t)==direct(K,m,t)
                    arith+=1
        assert phase(60,m)==full
        counts.append({'m':m,'Mignosi_F':len(full),'first_full_in_range':first,
                       'K1':sizes[0],'K2':sizes[1],'K10':sizes[9],
                       'K25':sizes[24],'K60':len(phase(60,m))})
    for K in (1,2,3,11,101,10**30+37):
        for m in (2,3,5,9,17):
            for t in (Q(1,K+m+1),Q(K+m,K+m+1),Q(1,2),Q(1,3),Q(17,101)):
                assert word(K,m,t)==direct(K,m,t)
                assert balanced(word(K,m,t))
                large+=1
    return {'result':'R134_STURMIAN_SATURATION_EXACT_PASS',
            'm_values':list(range(2,10)),'total_2d_distinct_words_scanned':total,
            'fixedK_exact_formula_matches':arith,'large_K_boundary_matches':large,
            'counts':counts,'sufficient_uniform_threshold':'K>=4*m^3+2',
            'arithmetic':'fractions.Fraction exact floor'}
if __name__=='__main__':print(json.dumps(run(),indent=2))
