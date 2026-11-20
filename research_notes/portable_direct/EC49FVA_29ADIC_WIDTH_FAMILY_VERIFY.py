"""EC49FVA: exact 29-adic certificate, 24 rational residue classes.
Standard-library Fraction checks; printed logarithms are diagnostic only.
"""
from fractions import Fraction as Q
from math import log
from itertools import count

P = 29
BETA = Q(3,637)
E = Q(31597745,1653649)
U0 = Q(21829245984,45529434409)
UE = Q(21829245984,45529434409-456083905*E)

def valuation(z,p=P):
    assert z
    a,b,k = z.numerator,z.denominator,0
    while a%p==0:
        a//=p
        k+=1
    while b%p==0:
        b//=p
        k-=1
    return k

def residue(z):
    assert z.denominator%P
    return (z.numerator%P)*pow(z.denominator%P,-1,P)%P

def params(x):
    t0=(1-x)*(1-BETA*x)
    te=(1-x)*(1+BETA*(E-1)*x)
    return t0,te,1-te,1-t0,1-UE*te,1-U0*t0

assert (residue(BETA),residue(E),residue(BETA*(E-1)))==(26,9,5)
assert valuation(UE)==-1
assert UE.denominator%(P*P)==P
assert 0<U0<UE<1
assert 0<BETA*(E-1)<1
assert UE < (1-BETA)/(1+BETA*(E-1))

Za={r for r in range(P) if residue(Q(r)*(1+BETA-BETA*r))==0}
Zt0={r for r in range(P) if residue((1-Q(r))*(1-BETA*r))==0}
Zte={r for r in range(P) if residue((1-Q(r))*(1+BETA*(E-1)*r))==0}
assert (Za,Zt0,Zte)==({0,20},{1,19},{1,23})
BAD=Za|Zt0|Zte
GOOD=set(range(P))-BAD
assert BAD=={0,1,19,20,23} and len(GOOD)==24

def certify(x):
    assert 0<x<1 and x.denominator%P and residue(x) in GOOD
    t0,te,am,a,b,bp=params(x)
    assert 0<am<a<b<bp<1
    assert all(valuation(z)==0 for z in (t0,te,a))
    r=t0/(UE*te)
    s=b*t0/(a*UE*te)
    assert r==(1-a)/(1-b)
    assert s==b*(1-a)/(a*(1-b))
    assert 1<r<s and (valuation(r),valuation(s))==(1,0)
    # If log(r)/log(s)=h/k in Q, r**k=s**h and valuation gives k=0.
    return r,s,log(float(r))/log(float(s))

for r in sorted(GOOD):
    x=Q(r,P+1)
    if 0<x<1 and residue(x)==r:
        certify(x)

for x in (Q(7,20),Q(1,2),Q(2,3),Q(3,4),Q(11,40),Q(100,301)):
    if x.denominator%P and residue(x) in GOOD:
        rr,ss,t=certify(x)
        print(f'CERTIFIED x={x} residue={residue(x)} '
              f'v29(R)={valuation(rr)} v29(S)={valuation(ss)} '
              f't~{t:.12f}')
    else:
        print(f'OUTSIDE_SUFFICIENT_CLASS x={x}')

for lo,hi in ((Q(1,100),Q(1,50)),
              (Q(1,3),Q(2,5)),(Q(9,10),Q(91,100))):
    witnesses=[]
    for m in count(50):
        d=29*m+1
        first=(lo.numerator*d)//lo.denominator+1
        k=first+(25-first)%P
        if Q(k,d)<hi:
            x=Q(k,d)
            assert lo<x<hi and residue(x)==25
            certify(x)
            witnesses.append(x)
        if len(witnesses)==3:
            break
    print('DENSITY_WITNESSES',lo,hi,', '.join(map(str,witnesses)))

print('ALL PASS -- exact 24/29 residue classes and rational interval witnesses')
