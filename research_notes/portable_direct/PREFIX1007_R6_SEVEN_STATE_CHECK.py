#!/usr/bin/env python3
"""PREFIX-1007, exact formal-series evaluation; requires published PREFIX-1006.
Only the inherited typed BRC terminal observer is evaluated; not a native run.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import factorial
import json
from PREFIX1006_R6_MARKED_COLLISION_DP import ORBIT_POLYS, h_transfer

D=6

def add(a,b,k=1):
    z=dict(a)
    for mon,v in b.items():z[mon]=z.get(mon,0)+k*v
    return {mon:v for mon,v in z.items() if v}

def shift(a,p):return {(x,y,q+p):v for (x,y,q),v in a.items()}

def mul(a,b):
    z={}
    for (x,y,q),v in a.items():
        for (i,j,k),w in b.items():
            mon=x+i,y+j,q+k
            z[mon]=z.get(mon,0)+v*w
    return {mon:v for mon,v in z.items() if v}

@lru_cache(None)
def g(k):
    if k==0:return {(1,0,0):1}
    if k==1:return {(0,1,0):1}
    return shift(add(g(k-2),g(k-1),-(k-1)),-1)

def terms(delta):
    p=sum(max(v,0) for v in delta)
    z={(0,0,p):1}
    for v in delta:z=mul(z,g(abs(v)))
    return {(y,q):v for (x,y,q),v in z.items()}

def module(N):
    prev=[Fraction(1)]*(D+1)
    rows=[tuple(prev)]
    for m in range(1,N+1):
        cur=[Fraction(0)]*(D+1)
        cur[0]=D*prev[1]/m
        for j in range(1,D+1):
            cur[j]=((D-j)*prev[j+1] if j<D else 0)
            cur[j]=(cur[j]+j*cur[j-1])/(m+j)
        rows.append(tuple(cur));prev=cur
    return rows

def marked(m,delta,rows):
    v=sum(Fraction(c)*rows[m-q][j] for (j,q),c in terms(delta).items()
          if 0<=m-q<len(rows))
    v*=factorial(m)**2
    assert v.denominator==1
    return v.numerator

def A(m,rows):
    v=rows[m][0]*factorial(m)**2
    assert v.denominator==1
    return v.numerator

def four_shift(m,rows):
    a=[A(m+j,rows) for j in range(4)]
    c=[6*(36*m+25)**2,
       Fraction(12*(396*m**3+869*m*m+443*m+36),m+1),
       Fraction(-2*(141*m**4+614*m**3+418*m*m-827*m-706),(m+1)*(m+2)),
       Fraction(2*(2*m+3)*(m*m+2*m-6),m+2)]
    s=sum(x*y for x,y in zip(c,a))
    assert s.denominator==1
    return s.numerator

def old_observer(n,rows):
    m=n-4
    return sum((a*n*n+b*n+c)*marked(m,d,rows) for d,(a,b,c) in ORBIT_POLYS)

def run():
    rows=module(306)
    tests=0
    for d,_ in ORBIT_POLYS:
        for m in range(11):
            assert marked(m,d,rows)==h_transfer(m,d)
            tests+=1
    for n in range(5,61):assert four_shift(n-4,rows)==old_observer(n,rows)
    for n in [5,6,8,20,30]:
        numerator=four_shift(n-4,rows)
        reference=sum((a*n*n+b*n+c)*h_transfer(n-4,d)
                      for d,(a,b,c) in ORBIT_POLYS)
        assert numerator==reference
    for m in range(30):
        d=(-2,0,0,0,0,2)
        formula=Fraction(A(m,rows))-Fraction(A(m+1,rows),3*(m+1))
        formula+=Fraction(A(m+2,rows)-6*A(m+1,rows),30*(m+1)**2)
        assert formula==marked(m,d,rows)
    d1=(3,2,-2,-1,-1,-1);d2=(-3,2,2,1,-1,-1)
    for m in [5,6,10,50,100,200,300]:
        assert marked(m,d1,rows)==marked(m,d2,rows)
    selected={}
    for n in [5,6,8,20,30,50,100,200,300]:
        f=Fraction(four_shift(n-4,rows),36**n)
        txt=str(f)
        selected[str(n)]={'value':txt if n<=100 else None,
            'numerator_digits':len(str(f.numerator)),
            'denominator_digits':len(str(f.denominator)),
            'sha256_fraction':sha256(txt.encode()).hexdigest()}
    return {'schema':'PREFIX1007_R6_SEVEN_STATE_EXACT_CERT_V1',
       'prior_observer':'PREFIX-1005, PREFIX-1006 eleven exact marked orbit polynomials',
       'checks_old_transfer':tests,'checks_four_shift_n':'5..60',
       'checks_prior_observer_n':[5,6,8,20,30],
       'checks_shift_two_m':'0..29',
       'sign_redistribution_example':{'delta_1':list(d1),'delta_2':list(d2),
           'H5':marked(5,d1,rows),'H6':marked(6,d1,rows)},
       'selected_masked_probabilities':selected,
       'limits':'Exact rational post-observer coefficients; no native Stage46 run or independent Review'}

if __name__=='__main__':print(json.dumps(run(),indent=2,ensure_ascii=False))
