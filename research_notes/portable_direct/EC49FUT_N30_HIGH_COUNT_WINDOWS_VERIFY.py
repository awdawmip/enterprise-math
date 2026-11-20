#!/usr/bin/env python3
"""Exact rational interval certificate for n=30 upper-count minimax phase windows.
No third-party dependencies. Frozen BRC16943 binary observation model.
New results j=11..16 (two-endpoint windows), j=17 (pure E across crossing).
"""
from fractions import Fraction as F
from math import comb
N=30
B=F(3,637)
E=F(31597745,1653649)
U_A=F(21829245984)
U_B=F(45529434409)
U_C=F(456083905)
DEN=10**12
class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def cv(z):return z if isinstance(z,I) else I(z)
    def __add__(self,z):
        z=self.cv(z);return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,z):return self+-self.cv(z)
    def __rsub__(self,z):return self.cv(z)+-self
    def __mul__(self,z):
        z=self.cv(z);p=[a*b for a in (self.lo,self.hi) for b in (z.lo,z.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,z):
        z=self.cv(z);assert 0<z.lo or z.hi<0
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,z):return self.cv(z)/self
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        if k==0:return I(1)
        if self.lo>=0:return I(self.lo**k,self.hi**k)
        if self.hi<=0:
            return I(self.lo**k,self.hi**k) if k%2 else I(self.hi**k,self.lo**k)
        return I(self.lo**k,self.hi**k) if k%2 else I(0,max(self.lo**k,self.hi**k))
def params(x,theta):
    u=U_A/(U_B-U_C*theta)
    T=(1-x)*(1-B*x+B*x*theta)
    return 1-T,1-u*T,u,T
def delta(k,x,t):
    p,q,_,_=params(x,t)
    return comb(N,k)*(q**k*(1-q)**(N-k)-p**k*(1-p)**(N-k))
def tail(j,x,t):
    out=I(0) if isinstance(x,I) else F(0)
    for k in range(j,N+1):out+=delta(k,x,t)
    return out
def deriv_tail(j,x,t):
    p,q,u,T=params(x,t)
    Tprime=-(1-B*x+B*x*t)+(1-x)*B*(t-1)
    dp,dq=-Tprime,-u*Tprime
    return N*comb(N-1,j-1)*(q**(j-1)*(1-q)**(N-j)*dq-p**(j-1)*(1-p)**(N-j)*dp)
def gap(j,x):return tail(j,x,E)-tail(j,x,F(0))
def mix(k,x,lam):return (1-lam)*delta(k,x,F(0))+lam*delta(k,x,E)
def exact_bracket(function,pair,forward=True):
    lo,hi=[F(t,DEN) for t in pair]
    assert lo<hi
    ylo,yhi=function(lo),function(hi)
    assert ylo<0<yhi if forward else ylo>0>yhi,(pair,float(ylo),float(yhi))
def tests(j,a,b,entry,exit,slabs=128,pure=False):
    assert a<b
    exact_bracket(lambda x:gap(j,x),entry,True)
    exact_bracket(lambda x:delta(j,x,E),exit,False)
    assert (entry[1]<exit[0]) if not pure else (exit[1]<entry[0])
    minima={}
    for s in range(slabs):
        x=I(a+(b-a)*s/slabs,a+(b-a)*(s+1)/slabs)
        d={'E_prev_negative':-delta(j-1,x,E).hi,
           'Z_j_negative':-delta(j,x,F(0)).hi,
           'Z_next_negative':-delta(j+1,x,F(0)).hi,
           'E_next_positive':delta(j+1,x,E).lo,
           'H_below_minus_0.01':-F(1,100)-gap(j+1,x).hi,
           'G_prime_above_0.25':(deriv_tail(j,x,E)-deriv_tail(j,x,F(0))).lo-F(1,4)}
        if not pure:
            d['mix_j_at_0.75_negative']=-mix(j,x,F(3,4)).hi
            d['mix_next_at_0.5_positive']=mix(j+1,x,F(1,2)).lo
        for key,v in d.items():
            assert v>0,(j,s,key,float(v))
            minima[key]=min(minima.get(key,v),v)
    if pure:
        assert gap(j,F(exit[1],DEN))<0
        assert gap(j,a)<0 and gap(j,b)>0
    else:
        assert gap(j,a)<0<gap(j,b)
        assert delta(j,a,E)>0>delta(j,b,E)
        for x in (F(entry[1],DEN),(F(entry[1],DEN)+F(exit[0],DEN))/2,F(exit[0],DEN)):
            d0=delta(j,x,F(0));de=delta(j,x,E)
            lam=-d0/(de-d0)
            assert F(3,4)<lam<=1
            assert mix(j+1,x,lam)>0
        mid=(F(entry[1],DEN)+F(exit[0],DEN))/2
        d0,de=delta(j,mid,F(0)),delta(j,mid,E)
        gam=-gap(j+1,mid)/(de-d0)
        assert F(0)<gam<F(1)
    print('PASS',j,'pure-E' if pure else 'two-support','slabs',slabs,'entry',entry,'exit',exit,'min-margins',','.join(f'{k}:{float(v):.8g}' for k,v in minima.items()))
WINDOWS={
 11:(F(224,1000),F(235,1000),(225500758714,225500758715),(232493020829,232493020830)),
 12:(F(264,1000),F(273,1000),(265335976635,265335976636),(271729505923,271729505924)),
 13:(F(305,1000),F(314,1000),(306101041760,306101041761),(311606276755,311606276756)),
 14:(F(346,1000),F(354,1000),(347591154980,347591154981),(351933959535,351933959536)),
 15:(F(388,1000),F(394,1000),(389649898533,389649898534),(392569888098,392569888099)),
 16:(F(431,1000),F(435,1000),(432156258608,432156258609),(433405288408,433405288409)),
 17:(F(473,1000),F(477,1000),(475015483299,475015483300),(474356338011,474356338012))
}
if __name__=='__main__':
    for j,(a,b,entry,exit) in WINDOWS.items():
        tests(j,a,b,entry,exit,128,pure=(j==17))
    print('ALL PASS')
