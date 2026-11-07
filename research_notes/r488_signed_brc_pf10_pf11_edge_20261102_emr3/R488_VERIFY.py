#!/usr/bin/env python3
"""R488 exact signed BRC auxiliary-scalar s=3 Toeplitz ranks 10 and 11.
Frozen model: EM R462 @ 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Standard-library exact integer/Fraction arithmetic; no native X6 inference.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
from functools import reduce
import json

def B(n,j): return comb(n,j) if 0 <= j <= n else 0
def C(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1))
                          for q in range(r-t+1))
def add(a,b):
    z=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    while len(z)>1 and z[-1]==0: z.pop()
    return z
def mul(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: z[i+j]+=x*y
    return z
def prod(xs):
    z=[F(1)]
    for f in xs: z=mul(z,f)
    return z
def ev(a,k):
    z=F(0)
    for v in reversed(a): z=z*k+v
    return z
def p(t):
    """Catalan-normalized H(2k+1,t), cross-checked against raw signed H."""
    z=[F(0)]
    for q in range((t-1)//2+1):
        factors=[]
        for h in range(q): factors.extend(([-h,1],[1-h,1]))
        for e in range(2-t,t+2):
            if e not in range(1-2*q,1): factors.append([e,2])
        part=[F(B(t-1,2*q)*4**q,factorial(2*t))*v for v in prod(factors)]
        z=add(z,part)
    return z
def exact_div(a,b):
    z=a[:]; q=[F(0)]*(len(a)-len(b)+1)
    for i in range(len(q)-1,-1,-1):
        v=z[i+len(b)-1]/b[-1]; q[i]=v
        for j,w in enumerate(b): z[i+j]-=v*w
    assert all(v==0 for v in z)
    return q
def bareiss(a):
    a=[row[:] for row in a]; n=len(a); last=1; sg=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None: return 0
            a[i],a[j]=a[j],a[i]; sg=-sg
        pivot=a[i][i]
        for j in range(i+1,n):
            for h in range(i+1,n):
                z=pivot*a[j][h]-a[j][i]*a[i][h]
                assert z%last==0
                a[j][h]=z//last
            a[j][i]=0
        last=pivot
    return sg*a[-1][-1]

ps={t:p(t) for t in range(2,15)}
Ds=[[F(1)]]
for m in range(1,12):
    z=[F(0)]
    for ell in range(1,m+1):
        term=prod([ps[ell+2]]+[ps[2]]*(ell-1)+[Ds[m-ell]])
        z=add(z,[(-1)**(ell-1)*v for v in term])
    Ds.append(z)
    assert len(z)==6*m+1

result={}
for m,shift in ((10,3),(11,14)):
    fac=prod([[0,1]]*m+[[1,1]]*m+[[2,1]]+[[1,2]]*m+[[3,2]]*m)
    assert len(fac)==4*m+2
    q=exact_div(Ds[m],fac)
    assert len(q)==2*m
    L=reduce(lcm,(v.denominator for v in q))
    P=[int(v*L) for v in q]
    g=reduce(gcd,(abs(v) for v in P))
    P=[v//g for v in P]; den=L//g
    assert Ds[m]==[F(v,den) for v in mul(fac,P)]
    shifted=[sum(P[i]*B(i,j)*shift**(i-j) for i in range(j,len(P)))
             for j in range(len(P))]
    if m==10:
        assert den==45581403004499291898608640000000000
        assert all(v>0 for v in shifted)
        boundaries=[1,2]
        assert all(ev(P,k)>0 for k in boundaries)
    else:
        assert den==4102326270404936270874777600000000000
        assert all(v<0 for v in shifted)
        boundaries=list(range(1,14))
        assert all(ev(P,k)>0 for k in boundaries)
        assert ev(P,14)<0
    result[str(m)]={"P_ascending":P,"denominator":den,"shift":shift,
                    "shift_coefficients":shifted,
                    "shift_coefficient_sign":"POSITIVE" if m==10 else "NEGATIVE",
                    "boundary_values":[str(int(ev(P,k))) for k in boundaries],
                    "leading_r_normalized_limit":str(Ds[m][-1]/2**(6*m)),
                    "degree":6*m,"polynomial_coefficient_equalities":6*m+1}

raw=0
for k in range(1,51):
    for t in range(2,15):
        assert ev(ps[t],k)*C(k)==H(k,t),(k,t)
        raw+=1
ks=list(range(1,21))+[22,24,30,49,64,100]
examples={}
for k in ks:
    for m in (10,11):
        det=bareiss([[H(k,3+i-j) for j in range(m)] for i in range(m)])
        val=ev(Ds[m],k)*C(k)**m
        assert val.denominator==1 and det==val,(m,k)
        assert (det>0 if m==10 or k<=13 else det<0),(m,k)
        if (m,k) in ((10,1),(10,9),(11,13),(11,14)):
            examples[f"m{m}_k{k}"]=str(det)

print(json.dumps({"status":"R488_EXACT_PASS",
 "scientific_pin":"18783e01e3646c72b7aab3b16d3f565e83e6446f",
 "scope":"SIGNED_BRC_AUXILIARY_SCALAR_s3_m10_m11",
 "claims":{"m10":"positive for all integer k>=1",
           "m11":"positive for k=1,...,13; negative for all integer k>=14"},
 "exact_certificates":result,"raw_signed_convolution_checks":raw,
 "direct_integer_determinant_checks":2*len(ks),
 "direct_determinant_examples":examples,
 "arithmetic":"Python stdlib int/Fraction; exact; no floating-point",
 "admission":"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"},
 sort_keys=True,ensure_ascii=False,indent=2))
