#!/usr/bin/env python3
"""EC49FVX: exact signed residual spectrum and delayed one-sided coding.
Scientific pin: BRC16943; parent EC49FVW@6277ba7443de4d469cbfb7e49628ae2ab3e4f9cb.
Standard-library exact arithmetic only.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd

p = 11
U, Gamma = F(4822040484, 8132285009), F(141024, 1653649)
def reduce11(x):
    return x.numerator * pow(x.denominator, -1, p) % p
u, g, inv = reduce11(U), reduce11(Gamma), pow(637, -1, p)
rows = []
for z in range(p):
    la, lb = (637 - 3*z)*inv % p, u*(1+g*z) % p
    aa, bb = (1-(1-z)*la) % p, (1-(1-z)*lb) % p
    rows.append((z, aa, bb, la, lb))
c, d = -3*inv % p, u*g % p
P10 = {(h,n) for h in range(10) for n in range(10)
       if all((pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))
              * pow((la-lb)%p,-1,p) % p
              for z,aa,bb,la,lb in rows if z != 3)
       and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p) % p}
assert len(P10) == 44

def certified(h,n):
    return (h%10,n%10) in P10 and (9*h+10*n)%11 != 0

def direct(h,n):
    for z,aa,bb,la,lb in rows:
        if z == 3:
            value = pow(la,n-1,p)*pow(aa,h-1,p)*(n*aa-h*(1-z)*la)%p
        else:
            value = (pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))*pow((la-lb)%p,-1,p)%p
        if value == 0: return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0
assert all(certified(h,n) == direct(h,n)
           for h in range(1,111) for n in range(1,111))
assert all(((-h)%10,(-n)%10) in P10 for h,n in P10)
print('PROJECTIVE_DIRECT_CHECK 12100/12100 PASS; |P10|=44; SIGN_REVERSAL_CLOSED PASS')

period = 220
R = {s: {q for q in range(1,period+1) if q%2
         and certified((q+s)//2,(q-s)//2)} for s in (-1,+1)}
assert len(R[-1]) == len(R[+1]) == 80
assert R[+1] == {(-q)%period or period for q in R[-1]}
assert R[+1] == {(q+168-1)%period+1 for q in R[-1]}
print('RESIDUE_RELATIONS Rplus=-Rminus=Rminus+168 (mod 220); 80/80 PASS')

def cyclic_max(a):
    b = sorted(a)
    return max([y-x for x,y in zip(b,b[1:])] + [b[0]+period-b[-1]])
assert all(cyclic_max(R[s]) == 6 for s in R)
def deficit(H,s):
    return next(t for t in range(6) if (H-t-1)%period+1 in R[s])
pairs = [(deficit(H,-1),deficit(H,+1)) for H in range(1,period+1)]
assert all(pairs[(H-1)%period][1] == pairs[(H-169)%period][0]
           for H in range(1,period+1))
assert next(T for T in range(1,period+1)
            if period%T==0 and all(pairs[i]==pairs[(i+T)%period] for i in range(period))) == period
print('EXACT_DELAY_CODING rplus(H)=rminus(H-168), minimal pair period=220 PASS')

joint = Counter(pairs)
rho = Counter(F(l+r,2) for l,r in pairs)
asym = Counter(F(r-l,2) for l,r in pairs)
assert len(joint) == 14
assert rho == {F(0):54,F(1):99,F(2):55,F(3):11,F(4):1}
assert asym == {F(-2):6,F(-1):48,F(0):114,F(1):44,F(2):8}
assert joint == {(0,0):54,(0,2):22,(0,4):4,(1,1):54,(1,3):22,
                 (1,5):4,(2,0):23,(2,2):3,(3,1):23,(3,3):3,
                 (4,0):3,(4,2):1,(5,1):3,(5,3):1}
print('JOINT_14_STATES', sorted(joint.items()))
print('SIGN_ASYMMETRY_HISTOGRAM', sorted((str(k),v) for k,v in asym.items()))

mL = sum((F(l) for l,r in pairs),F(0))/period
mR = sum((F(r) for l,r in pairs),F(0))/period
m_rho = sum((F(l+r,2) for l,r in pairs),F(0))/period
m_a = sum((F(r-l,2) for l,r in pairs),F(0))/period
vL = sum(((F(l)-mL)**2 for l,r in pairs),F(0))/period
covLR = sum(((F(l)-mL)*(F(r)-mR) for l,r in pairs),F(0))/period
vA = sum(((F(r-l,2)-m_a)**2 for l,r in pairs),F(0))/period
cov_rho_a = sum(((F(l+r,2)-m_rho)*(F(r-l,2)-m_a) for l,r in pairs),F(0))/period
assert (mL,mR,m_rho,m_a) == (F(123,110),F(123,110),F(123,110),F(0))
assert (vL,covLR,vA,cov_rho_a) == (F(16881,12100),F(601,12100),F(37,55),F(0))
print('MOMENTS mean_rho=123/110 mean_A=0 variance_A=37/55 Cov(rho,A)=0 Cov(rL,rR)=601/12100 PASS')

# A second-order sum/center observer requires both rho and A.
assert [pairs[(H-1)%period] for H in (221,224,233)] == [(0,2),(1,1),(2,0)]
assert all(F(sum(pairs[(H-1)%period]),2) == 1 for H in (221,224,233))
for H in (221,224,233):
    l,r = pairs[(H-1)%period]
    qL,qR = H-l,H-r
    xL, xR = F(qL-1,2*qL),F(qR+1,2*qR)
    left,right = F(1,2)-xL,xR-F(1,2)
    signed = H*H*(right-left)
    leading = F(r-l,2)
    assert signed == leading*F(H*H,(H-r)*(H-l))
    assert (signed>0)-(signed<0) == (leading>0)-(leading<0)
    assert abs(signed-leading) <= 2*(F(H,H-5)**2-1)
    print('LOSSY_SUM_WITNESS',H,'deficits',(l,r),'rho',F(l+r,2),'A',leading,
          'H2(R-L)',signed,'PASS')

# Direct full reduced-Farey scan for genuinely nearest certified neighbors.
for H in (33,82,221,224,233,302):
    below,above = None,None
    for q in range(2,H+1):
        for h in range(1,q):
            if gcd(h,q)!=1 or not certified(h,q-h): continue
            x=F(h,q)
            if x < F(1,2) and (below is None or below<x): below=x
            if x > F(1,2) and (above is None or x<above): above=x
    l,r=pairs[(H-1)%period]
    assert below == F(H-l-1,2*(H-l))
    assert above == F(H-r+1,2*(H-r))
    print('INDEPENDENT_FAREY',H,'nearest',str(below),str(above),'PASS')
print('ALL PASS')
