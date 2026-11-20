#!/usr/bin/env python3
"""EC49FUR: exact rational two-endpoint total-variation dual and phase classifier.

Assumes FUQ endpoint reduction, which is an analytic theorem, not checked by this script.
No floating-point arithmetic enters assertions or selection.
"""
from fractions import Fraction as F
from math import comb

BETA = F(3, 637)
THETA_E = F(31597745, 1653649)
UA, UB, UC = F(21829245984), F(45529434409), F(456083905)

def masses(n, x, theta):
    T = (1 - x)*(1 - BETA*x + BETA*x*theta)
    u = UA/(UB - UC*theta)
    p, q = 1 - T, 1 - u*T
    assert 0 <= p < q <= 1
    return [comb(n,k)*(q**k*(1-q)**(n-k) - p**k*(1-p)**(n-k)) for k in range(n+1)]

def positive_part(z):
    return max(F(0), z)

def dual(n, x):
    lo, hi = masses(n,x,F(0)), masses(n,x,THETA_E)
    diffs = [b-a for a,b in zip(lo,hi)]
    candidates = {F(0), F(1)}
    for a,d in zip(lo,diffs):
        if d:
            root = -a/d
            if 0 < root < 1:
                candidates.add(root)
    def obj(lam):
        return sum((positive_part(a+lam*d) for a,d in zip(lo,diffs)), F(0))
    minimum = min(map(obj,candidates))
    optimal = sorted(t for t in candidates if obj(t) == minimum)
    def right_derivative_zero():
        return sum((d if a>0 else max(F(0),d) if a==0 else F(0)
                    for a,d in zip(lo,diffs)),F(0))
    def left_derivative_one():
        return sum((d if b>0 else min(F(0),d) if b==0 else F(0)
                    for b,d in zip(hi,diffs)),F(0))
    s0, s1 = right_derivative_zero(), left_derivative_one()
    assert (s0 >= 0) == (obj(F(0)) == minimum)
    assert (s1 <= 0) == (obj(F(1)) == minimum)
    assert (s0 < 0 and s1 > 0) == (obj(F(0)) > minimum and obj(F(1)) > minimum)
    return dict(value=minimum, risk=(1-minimum)/2,
                lambda_candidates=optimal, endpoints=(obj(F(0)),obj(F(1))),
                slopes=(s0,s1), lo=lo, hi=hi)

def primal(n,x):
    lo, hi = masses(n,x,F(0)), masses(n,x,THETA_E)
    best=F(-1)
    result=None
    for j in range(n+1):
        a0, ae = sum(lo[j+1:],F(0)), sum(hi[j+1:],F(0))
        b0, be = lo[j], hi[j]
        cands=[F(0),F(1)]
        if b0!=be:
            root=(ae-a0)/(b0-be)
            if 0<root<1: cands.append(root)
        for g in cands:
            value=min(a0+g*b0,ae+g*be)
            if value>best:
                best=value;result=(j,g,value)
    return result

def verify_case(n,x):
    r=dual(n,x)
    j,g,v=primal(n,x)
    assert r['value']==v
    for lam in r['lambda_candidates']:
        signs=[(1-lam)*a+lam*b for a,b in zip(r['lo'],r['hi'])]
        seen_positive=False
        for z in signs:
            if z>0:seen_positive=True
            if seen_positive:assert z>=0,('multiple sign changes',n,x,lam)
        assert sum((max(F(0),s) for s in signs),F(0))==v
    kind = 'BOTH_REQUIRED' if r['slopes'][0]<0<r['slopes'][1] else (
        'ZERO_PURE_EXISTS' if r['slopes'][0]>=0 else 'E_PURE_EXISTS')
    return j,g,r['risk'],r['slopes'],r['lambda_candidates'],kind

def main():
    cases=[(1,F(1,2)),(2,F(1,2)),(15,F(7,25000)),
           (15,F(1,2)),(30,F(3,20)),(40,F(1,100)),(60,F(7,20))]
    for n,x in cases:
        j,g,risk,slopes,lams,kind=verify_case(n,x)
        print('n=%d x=%s j=%d gamma=%.12g risk=%.12g lambda=%s classification=%s' %
              (n,x,j,float(g),float(risk),[round(float(a),12) for a in lams],kind))
    print('PASS: exact two-endpoint TV dual, derivative classification, primal dual equality')

if __name__ == '__main__':
    main()

class Interval:
    def __init__(self, lower, upper=None):
        self.lo=F(lower)
        self.hi=F(lower if upper is None else upper)
        assert self.lo<=self.hi
    @staticmethod
    def as_i(z): return z if isinstance(z,Interval) else Interval(z)
    def __add__(self,z):
        z=self.as_i(z);return Interval(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,z):return self+-self.as_i(z)
    def __rsub__(self,z):return self.as_i(z)+-self
    def __mul__(self,z):
        z=self.as_i(z);p=[a*b for a in [self.lo,self.hi] for b in [z.lo,z.hi]]
        return Interval(min(p),max(p))
    __rmul__=__mul__
    def __pow__(self,n):
        assert int(n)==n and n>=0
        if n==0:return Interval(1)
        if self.lo>=0:return Interval(self.lo**n,self.hi**n)
        if self.hi<=0 and n%2:return Interval(self.lo**n,self.hi**n)
        if self.hi<=0:return Interval(self.hi**n,self.lo**n)
        if n%2:return Interval(self.lo**n,self.hi**n)
        return Interval(F(0),max(self.lo**n,self.hi**n))
    def __repr__(self):return f'[{float(self.lo):.12g},{float(self.hi):.12g}]'

def derivative_interval(n,j,xlo,xhi,th):
    X=Interval(xlo,xhi)
    u=UA/(UB-UC*th)
    T=(1-X)*(1-BETA*X+BETA*X*th)
    Tp=-(1-BETA*X+BETA*X*th)+(1-X)*BETA*(th-1)
    p,q=1-T,1-u*T
    pp,qp=-Tp,-u*Tp
    const=n*comb(n-1,j-1)
    return const*(q**(j-1)*(1-q)**(n-j)*qp - p**(j-1)*(1-p)**(n-j)*pp)

# Exact interval certificate for the 30-observation mixing onset.
def verify_n30_onset():
    a,b=F(749,5000),F(1499,10000)
    dlo=derivative_interval(30,9,a,b,F(0))
    dhe=derivative_interval(30,9,a,b,THETA_E)
    deriv=dhe-dlo
    assert deriv.lo>F(1,2),(dlo,dhe,deriv)
    # Exact endpoint Bayes: sign at count 8 is negative, 9 positive,
    # certified throughout interval by elementary interval enclosures.
    X=Interval(a,b)
    T=(1-X)*(1-BETA*X+BETA*X*THETA_E)
    u=UA/(UB-UC*THETA_E)
    p,q=1-T,1-u*T
    def gap_k(k):return comb(30,k)*(q**k*(1-q)**(30-k)-p**k*(1-p)**(30-k))
    assert gap_k(8).hi<0
    assert gap_k(9).lo>0
    # At both endpoints the n=30 signed gap gives a strict shift from E to mixed.
    slo=dual(30,a)['slopes'][1]
    shi=dual(30,b)['slopes'][1]
    assert slo<0<shi
    assert dual(30,a)['slopes'][0]<0 and dual(30,b)['slopes'][0]<0
    print('n30 onset: derivative lower bound >0',float(deriv.lo),
          'slope endpoints',float(slo),float(shi), 'Bayes-9 sign interval',gap_k(8),gap_k(9))
    print('PASS: unique algebraic E-to-mixed onset in (749/5000,1499/10000)')

if __name__=='__main__':
    verify_n30_onset()

def signed_mass_interval(n,k,X,th):
    u=UA/(UB-UC*th)
    T=(1-X)*(1-BETA*X+BETA*X*th)
    p,q=1-T,1-u*T
    return comb(n,k)*(q**k*(1-q)**(n-k)-p**k*(1-p)**(n-k))

def verify_n30_full_chamber():
    a,b=F(749,5000),F(1499,10000)
    X=Interval(a,b)
    # λ=0 Bayes decision is K>=11; strict signed-mass sides.
    assert signed_mass_interval(30,10,X,F(0)).hi < 0
    assert signed_mass_interval(30,11,X,F(0)).lo > 0
    # Signed directional derivative of dual at 0 is E-minus-0 tail K>=11.
    s0=sum((signed_mass_interval(30,k,X,THETA_E)-signed_mass_interval(30,k,X,F(0)) for k in range(11,31)), Interval(0))
    assert s0.hi<-F(1,20),s0
    print('n30 zero-side dual slope interval',s0)
    print('PASS: onset separates pure E on left from obligatory two-endpoint mix on right')

if __name__=='__main__':verify_n30_full_chamber()
