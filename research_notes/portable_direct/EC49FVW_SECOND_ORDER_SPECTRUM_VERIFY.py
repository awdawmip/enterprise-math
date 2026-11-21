#!/usr/bin/env python3
"""EC49FVW: exact second-order residual spectrum of mod-11 certified rational neighbors.
Frozen scientific parent: EC49FVU@ac3bdb073b8ccd821cd23e830bcb9ccaf8d09529.
All arithmetic exact; standard library only.
"""
from collections import Counter
from fractions import Fraction
from math import gcd

p = 11
U = Fraction(4822040484, 8132285009)
Gamma = Fraction(141024, 1653649)
def mod_fraction(x):
    return x.numerator * pow(x.denominator, -1, p) % p
u, g, inv = mod_fraction(U), mod_fraction(Gamma), pow(637, -1, p)
rows = []
for z in range(p):
    la, lb = (637 - 3*z)*inv % p, u*(1+g*z) % p
    aa, bb = (1-(1-z)*la) % p, (1-(1-z)*lb) % p
    rows.append((z, aa, bb, la, lb))
c, d = -3*inv % p, u*g % p
P10 = {(h,n) for h in range(10) for n in range(10)
       if all((pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))
              * pow((la-lb)%p, -1, p) % p
              for z,aa,bb,la,lb in rows if z != 3)
       and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p) % p}
assert len(P10) == 44

def C(h,n):
    return (h%10, n%10) in P10 and (9*h+10*n)%11 != 0

def direct(h,n):
    for z,aa,bb,la,lb in rows:
        if z == 3:
            v = pow(la,n-1,p)*pow(aa,h-1,p)*(n*aa-h*(1-z)*la)%p
        else:
            v = (pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p)) * pow((la-lb)%p,-1,p)%p
        if v == 0: return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0
assert all(C(h,n)==direct(h,n) for h in range(1,111) for n in range(1,111))
print('PROJECTIVE_CROSSCHECK 12100/12100 PASS; P10=44')

# For 1/2, all determinant-one denominators are odd. The admissible q residues
# are periodic modulo 220; q is positive and actual for the H>32 theorem domain.
period = 220
R = {s: {q for q in range(1,period+1) if q%2 and
         C((q+s)//2,(q-s)//2)} for s in (-1,1)}
def cyclic_max(values,mod):
    a=sorted(values)
    return max([y-x for x,y in zip(a,a[1:])] + [a[0]+mod-a[-1]])
assert all(len(R[s])==80 and cyclic_max(R[s], period)==6 for s in (-1,1))
print('DET1_RESIDUE_SETS 2x80/220; max cyclic denominator step=6 PASS')

def deficit(H,s):
    return next(t for t in range(6) if (H-t-1)%period+1 in R[s])
residual = {h:(deficit(h,-1),deficit(h,1)) for h in range(1,period+1)}
sigma = [Fraction(sum(residual[h]),2) for h in range(1,period+1)]
hist = Counter(sigma)
assert hist == {Fraction(0):54, Fraction(1):99, Fraction(2):55,
                Fraction(3):11, Fraction(4):1}
assert residual[3] == (0,0) and residual[82] == (5,3)
assert all(any(sigma[i] != sigma[(i+k)%period] for i in range(period))
           for k in range(1,period) if period%k==0)
mean = sum(sigma, Fraction(0)) / period
variance = sum(((z-mean)**2 for z in sigma), Fraction(0)) / period
assert mean==Fraction(123,110) and variance==Fraction(8741,12100)
print('SECOND_ORDER_SPECTRUM', sorted((str(k),v) for k,v in hist.items()))
print('MINIMAL_PERIOD',period,'MEAN',mean,'VARIANCE',variance,
      'H=3 RESIDUAL',residual[3],'H=82 RESIDUAL',residual[82])

# Direct checks: independently enumerate every certified reduced fraction.
for H in (33,82,223,302):
    below, above = None, None
    for q in range(2,H+1):
        for h in range(1,q):
            if gcd(h,q) != 1 or not C(h,q-h): continue
            x = Fraction(h,q)
            if x < Fraction(1,2) and (below is None or x>below): below=x
            if x > Fraction(1,2) and (above is None or x<above): above=x
    rL,rR = residual[(H-1)%period+1]
    predicted_left = Fraction(H-rL-1, 2*(H-rL))
    predicted_right = Fraction(H-rR+1, 2*(H-rR))
    assert (below,above)==(predicted_left,predicted_right)
    gap = above-below
    assert gap == Fraction(1,2)*(Fraction(1,H-rL)+Fraction(1,H-rR))
    print('FAREY_CROSSCHECK',H,'qL',H-rL,'qR',H-rR,'gap',gap,'PASS')

# Generic rational anchors: exact periodic denominators inherited from EC49FVU.
for a,b in ((1,3),(2,3),(3,7),(5,11)):
    Q = 110*b
    def anchor_deficit(H,sgn):
        for t in range(8*b+1):
            q=H-t
            if (a*q+sgn)%b: continue
            h=(a*q+sgn)//b
            if 0<h<q and C(h,q-h): return t
        raise AssertionError((a,b,H,sgn))
    H0=Q*20
    residuals=[(anchor_deficit(H0+i,-1),anchor_deficit(H0+i,1)) for i in range(Q)]
    for i in range(Q):
        assert residuals[i] == (anchor_deficit(H0+Q+i,-1),anchor_deficit(H0+Q+i,1))
    print('GENERIC_PERIOD',f'{a}/{b}','period_divides',Q,
          'range', min(sum(z) for z in residuals),max(sum(z) for z in residuals),'PASS')
print('ALL PASS')
