#!/usr/bin/env python3
"""R490: exact rank-13 Toeplitz sign certificate for frozen R462 signed BRC auxiliary scalar.
Rebuild: python3 R490_VERIFY.py > R490_EVIDENCE.json
Scientific pin 18783e01e3646c72b7aab3b16d3f565e83e6446f.
Exact Python 3 standard-library integers and fractions; no floating point.
"""
from fractions import Fraction as Q
from math import comb, factorial, gcd, lcm
from functools import reduce
import json

PIN='18783e01e3646c72b7aab3b16d3f565e83e6446f'
RANK=13

def B(n,j): return comb(n,j) if 0<=j<=n else 0
def C(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r:return 0
    return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    while len(z)>1 and not z[-1]:z.pop()
    return z
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:z[i+j]+=x*y
    while len(z)>1 and not z[-1]:z.pop()
    return z
def prod(xs):
    z=[Q(1)]
    for x in xs:z=mul(z,x)
    return z
def ev(a,k):
    z=Q(0)
    for v in reversed(a):z=z*k+v
    return z
def p(t):
    z=[Q(0)]
    for q in range((t-1)//2+1):
        factors=[]
        for h in range(q):factors.extend(([-h,1],[1-h,1]))
        for e in range(2-t,t+2):
            if e not in range(1-2*q,1):factors.append([e,2])
        z=add(z,[Q(B(t-1,2*q)*4**q,factorial(2*t))*v for v in prod(factors)])
    return z
def exact_div(a,b):
    assert len(a)>=len(b) and b[-1]
    z=a[:];q=[Q(0)]*(len(a)-len(b)+1)
    for i in range(len(q)-1,-1,-1):
        v=z[i+len(b)-1]/b[-1];q[i]=v
        for j,w in enumerate(b):z[i+j]-=v*w
    assert all(v==0 for v in z)
    return q

def bareiss(a):
    a=[row[:] for row in a];n=len(a);last=1;sign=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None:return 0
            a[i],a[j]=a[j],a[i];sign=-sign
        pivot=a[i][i]
        for j in range(i+1,n):
            for h in range(i+1,n):
                val=pivot*a[j][h]-a[j][i]*a[i][h]
                assert val%last==0
                a[j][h]=val//last
            a[j][i]=0
        last=pivot
    return sign*a[-1][-1]

ps={t:p(t) for t in range(2,RANK+3)}
ds=[[Q(1)]]
# The exact lower-Hessenberg determinant recurrence, evaluated as Q[k] polynomials.
for m in range(1,RANK+1):
    z=[Q(0)]
    for ell in range(1,m+1):
        term=prod([ps[ell+2]]+[ps[2]]*(ell-1)+[ds[m-ell]])
        z=add(z,[(-1)**(ell-1)*v for v in term])
    assert len(z)==6*m+1,(m,len(z))
    ds.append(z)
fac=prod([[0,1]]*RANK+[[1,1]]*RANK+[[2,1]]+[[1,2]]*RANK+[[3,2]]*RANK)
assert len(fac)==4*RANK+2
quot=exact_div(ds[RANK],fac)
assert len(quot)==2*RANK
L=reduce(lcm,(v.denominator for v in quot))
primitive=[int(v*L) for v in quot]
g=reduce(gcd,(abs(v) for v in primitive))
assert g>0 and L%g==0
primitive=[v//g for v in primitive]
den=L//g
assert ds[RANK]==mul(fac,[Q(v,den) for v in primitive])

# A global certificate follows from a shift into the all-negative coefficient cone.
shift=6
shifted=[sum(primitive[i]*B(i,j)*shift**(i-j) for i in range(j,len(primitive))) for j in range(len(primitive))]
assert len(shifted)==26
assert all(v<0 for v in shifted),[(j,v) for j,v in enumerate(shifted) if v>=0]
boundary={str(k):str(int(ev(primitive,k))) for k in range(1,shift)}
assert all(int(v)>0 for v in boundary.values())
assert ev(primitive,shift)<0

# Two independent paths back to raw signed BRC integer data.
raw_checks=0
for k in range(1,41):
    for t in range(2,RANK+3):
        assert ev(ps[t],k)*C(k)==H(k,t),(k,t)
        raw_checks+=1
ks=list(range(1,17))+[17,20,24,30,49,64,100]
direct_examples={}
for k in ks:
    det=bareiss([[H(k,3+i-j) for j in range(RANK)] for i in range(RANK)])
    expected=ev(ds[RANK],k)*C(k)**RANK
    assert expected.denominator==1 and det==expected,(k,det,expected)
    assert (det>0 if k<shift else det<0),(k,det)
    if k in (1,5,6,7,14,64):direct_examples[str(k)]=str(det)

print(json.dumps({
    'status':'R490_EXACT_PASS',
    'scientific_pin':PIN,
    'object':'frozen R462 signed BRC auxiliary scalar r=2k+1, s=3, rank m=13',
    'claim':'D13(k)>0 for 1<=k<=5, D13(k)<0 for every integer k>=6',
    'p13_ascending':primitive,
    'denominator':den,
    'degree_F13':len(ds[RANK])-1,
    'degree_P13':len(primitive)-1,
    'coefficient_identity_checks':len(ds[RANK]),
    'factorization_identity_check':True,
    'shift':shift,
    'shifted_coefficients_ascending':shifted,
    'shifted_all_strict_negative':True,
    'shifted_coefficient_max':str(max(shifted)),
    'boundary_P_values':boundary,
    'asymptotic_normalized_limit':str(ds[RANK][-1]/2**(6*RANK)),
    'raw_signed_convolution_checks':raw_checks,
    'independent_original_integer_determinant_checks':len(ks),
    'direct_determinant_examples':direct_examples,
    'arithmetic':'exact stdlib int/Fraction, no floats',
    'proof_status':'AUTHOR_SIDE_EXACT_SYMBOLIC_NOT_INDEPENDENTLY_REVIEWED_NOT_ADMITTED'
},sort_keys=True,ensure_ascii=False,indent=2))
