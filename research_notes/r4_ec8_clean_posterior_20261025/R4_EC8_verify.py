#!/usr/bin/env python3
"""R4-EC8 author-side exact auxiliary positive BRC verifier. Requires sympy."""
import json
from collections import defaultdict
from itertools import product
import sympy as sp

EDGES={0:((2,-1,-1),(2,1,-1)),1:((0,-1,-1),(0,1,-1)),2:((1,1,1),(2,1,-1))}
MON=((1,0),(2,0),(2,2))
PAIRS=((0,0),(1,1),(2,0),(2,1))
STATES=[(q,r,e) for q,r in PAIRS for e in (1,-1)]
INDEX={s:i for i,s in enumerate(STATES)}
# Each numerator is a finite signed Laurent impulse in x and z.
NUM={
 (0,1):{(6,0):1,(4,0):-1,(2,0):-1,(1,-1):1},
 (1,1):{(6,0):-1,(5,1):1},
 (0,-1):{(3,1):-1,(2,2):1},
 (1,-1):{(5,1):1,(4,2):-1,(3,1):1,(2,2):-1,(2,0):-1,(1,1):1},
}
def advance(q,r,e,k,a):
    qp,eta,b=EDGES[q][a]
    return qp, MON[r][a],eta*e,eta*k+b

def proof_symbolic():
    x,z=sp.symbols('x z')
    m=sp.zeros(8)
    for j,(q,r,e) in enumerate(STATES):
        for a,(qp,eta,b) in enumerate(EDGES[q]):
            rp=MON[r][a]
            if rp==2: continue
            ep=eta*e
            assert (qp,rp) in PAIRS and e*eta*b==e*(1-2*a)
            m[INDEX[(qp,rp,ep)],j]+=z**(e*eta*b)
    den=(1+x*x)*(1-x*(z+1/z)+2*x**4-x**6)
    assert sp.cancel((sp.eye(8)-x*m).det()-den)==0
    v=(sp.eye(8)-x*m).inv()*sp.Matrix([1]+[0]*7)
    numerators={}
    for (r,e),coeffs in NUM.items():
        num=sum(c*x**a*z**b for (a,b),c in coeffs.items())
        assert sp.cancel(v[INDEX[(2,r,e)]]-num/den)==0
        numerators[f'r{r}_e{e}']=str(sp.expand(num))
    assert sp.cancel(den.subs(x,z)+z*z*(1+z*z)*(1-z*z)**2)==0
    return numerators

def scalar_sequences(depth):
    seq={tag:[] for tag in NUM}
    lag_shift_coeff=((1,1,1),(1,-1,1),(2,0,-1),
                     (3,1,1),(3,-1,1),(4,0,-2),(6,0,-1),(8,0,1))
    for n in range(depth+1):
        for tag,impulse in NUM.items():
            d=defaultdict(int)
            for (i,t),coef in impulse.items():
                if i==n:d[t]+=coef
            for lag,shift,mult in lag_shift_coeff:
                if n>=lag:
                    for t,ct in seq[tag][n-lag].items():
                        d[t+shift]+=mult*ct
            row={t:ct for t,ct in d.items() if ct}
            assert all(v>0 for v in row.values()),(n,tag,row)
            seq[tag].append(row)
    return seq

def full_source_check(depth, brute_depth, seq):
    hist={(0,0,1,0):1}
    checked=0
    for n in range(depth+1):
        assert sum(hist.values())==2**n
        for (r,e) in NUM:
            got={e*k:v for (q,rr,ee,k),v in hist.items()
                 if q==2 and rr==r and ee==e}
            assert got==seq[(r,e)][n],(n,r,e,got,seq[(r,e)][n])
        if n<=brute_depth:
            raw=defaultdict(int)
            for bits in product((0,1),repeat=n):
                s=(0,0,1,0)
                for a in bits:s=advance(*s,a)
                raw[s]+=1
            assert dict(raw)==hist
            checked+=2**n
        if n<depth:
            nxt=defaultdict(int)
            for s,mult in hist.items():
                for a in (0,1):nxt[advance(*s,a)]+=mult
            hist=nxt
    return checked

def main():
    depth=128
    nums=proof_symbolic()
    scalar=scalar_sequences(depth)
    brute=full_source_check(depth,12,scalar)
    a=scalar[(0,1)][20][0]
    b=scalar[(1,1)][20][0]
    assert (a,b)==(361,102)
    report={
      'result':'PASS',
      'claim':'exact rational generating functions, eighth-order Laurent recurrence and coprime-denominator minimality',
      'symbolic_numerators':nums,
      'independent_histogram_depth':depth,
      'raw_words_checked_total':brute,
      'example_theta_n20_eps_plus_k0':f'{b}/{a+b}',
      'mathematical_scope':'declared unit-positive auxiliary ordered affine BRC; not native X6',
      'limitations':'author check only; no formal Result/Driver review/Lean execution'}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
