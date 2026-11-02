#!/usr/bin/env python3
"""R489 exact rank-12 Toeplitz sign certificate for R462 signed BRC auxiliary scalar.
Scientific freeze: 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Depends on the explicitly reproduced normalization/recurrence, not a network lookup.
Only Python stdlib integers/Fraction; no floats.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd, lcm
from functools import reduce
import json

PIN="18783e01e3646c72b7aab3b16d3f565e83e6446f"
def B(n,j): return comb(n,j) if 0<=j<=n else 0
def C(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a): z[i]+=v
    for i,v in enumerate(b): z[i]+=v
    while len(z)>1 and z[-1]==0: z.pop()
    return z
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: z[i+j]+=x*y
    return z
def prod(xs):
    z=[Q(1)]
    for x in xs: z=mul(z,x)
    return z
def ev(a,k):
    z=Q(0)
    for v in reversed(a): z=z*k+v
    return z
def p(t):
    """Catalan-normalized signed convolution as exact polynomial in k."""
    z=[Q(0)]
    for q in range((t-1)//2+1):
        factors=[]
        for h in range(q): factors.extend(([-h,1],[1-h,1]))
        for e in range(2-t,t+2):
            if e not in range(1-2*q,1): factors.append([e,2])
        part=[Q(B(t-1,2*q)*4**q,factorial(2*t))*v for v in prod(factors)]
        z=add(z,part)
    return z
def exact_div(a,b):
    assert len(a)>=len(b) and b[-1]!=0
    z=a[:]; q=[Q(0)]*(len(a)-len(b)+1)
    for i in range(len(q)-1,-1,-1):
        v=z[i+len(b)-1]/b[-1]; q[i]=v
        for j,w in enumerate(b): z[i+j]-=v*w
    assert all(v==0 for v in z)
    return q
def bareiss(a):
    a=[r[:] for r in a]; n=len(a); last=1; sign=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None: return 0
            a[i],a[j]=a[j],a[i]; sign=-sign
        pivot=a[i][i]
        for j in range(i+1,n):
            for h in range(i+1,n):
                val=pivot*a[j][h]-a[j][i]*a[i][h]
                assert val%last==0
                a[j][h]=val//last
            a[j][i]=0
        last=pivot
    return sign*a[-1][-1]

# Symbolic identity in Q[k], proved by exact finite operations.
RANK=12
ps={t:p(t) for t in range(2,RANK+3)}
ds=[[Q(1)]]
for m in range(1,RANK+1):
    z=[Q(0)]
    for ell in range(1,m+1):
        term=prod([ps[ell+2]]+[ps[2]]*(ell-1)+[ds[m-ell]])
        z=add(z,[(-1)**(ell-1)*v for v in term])
    assert len(z)==6*m+1
    ds.append(z)
fac=prod([[0,1]]*RANK+[[1,1]]*RANK+[[2,1]]+[[1,2]]*RANK+[[3,2]]*RANK)
assert len(fac)==4*RANK+2
quot=exact_div(ds[RANK],fac)
assert len(quot)==2*RANK
L=reduce(lcm,(v.denominator for v in quot))
primitive=[int(v*L) for v in quot]
g=reduce(gcd,(abs(v) for v in primitive))
primitive=[v//g for v in primitive]
den=L//g
assert den==113716484215624833428648835072000000000000
assert ds[RANK]==[Q(v,den) for v in mul(fac,primitive)]

# Full shifted sign certificate: P(7+u)<0 for all integer/real u>=0.
shift=7
shifted=[sum(primitive[i]*B(i,j)*shift**(i-j) for i in range(j,len(primitive))) for j in range(len(primitive))]
assert len(shifted)==24 and all(v<0 for v in shifted)
positive_boundary={str(k):str(int(ev(primitive,k))) for k in range(1,7)}
assert all(int(v)>0 for v in positive_boundary.values())
assert int(ev(primitive,7))<0

# Original signed binomial convolution vs symbolic Catalan-normalized coefficient.
raw_checks=0
for k in range(1,41):
    for t in range(2,RANK+3):
        assert ev(ps[t],k)*C(k)==H(k,t),(k,t)
        raw_checks+=1

# Independent determinants over original integer H rather than symbolic recurrence.
ks=list(range(1,16))+[17,20,24,30,49,64,100]
direct_examples={}
for k in ks:
    det=bareiss([[H(k,3+i-j) for j in range(RANK)] for i in range(RANK)])
    rhs=ev(ds[RANK],k)*C(k)**RANK
    assert rhs.denominator==1 and det==rhs,(k,det,rhs)
    assert (det>0 if k<=6 else det<0),(k,det)
    if k in (1,6,7,8,14,64): direct_examples[str(k)]=str(det)

print(json.dumps({
  "status":"R489_EXACT_PASS",
  "scientific_pin":PIN,
  "object":"signed BRC auxiliary scalar, r=2k+1, s=3, m=12",
  "claim":"D12(k)>0 for 1<=k<=6; D12(k)<0 for all integers k>=7",
  "p12_ascending":primitive,
  "denominator":den,
  "degree_F12":len(ds[RANK])-1,
  "degree_P12":len(primitive)-1,
  "coefficient_identity_checks":len(ds[RANK]),
  "shift":shift,
  "shifted_coefficients_ascending":shifted,
  "shifted_all_strict_negative":True,
  "boundary_P_values_k1_to_k6":positive_boundary,
  "leading_r_normalized_limit":str(ds[RANK][-1]/2**(6*RANK)),
  "raw_signed_convolution_checks":raw_checks,
  "independent_original_integer_determinant_checks":len(ks),
  "direct_determinant_examples":direct_examples,
  "arithmetic":"exact Python stdlib int/Fraction, no floats",
  "admission":"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"
},sort_keys=True,ensure_ascii=False,indent=2))
