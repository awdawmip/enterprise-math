#!/usr/bin/env python3
"""Exact rational certificates for EC49FUS local n=30 reentrant support window."""
from fractions import Fraction as F
from math import comb
B = F(3,637)
E = F(31597745,1653649)
U_A, U_B, U_C = F(21829245984), F(45529434409), F(456083905)
N = 30
A, C = F(749,5000), F(79,500)
XIN_LO, XIN_HI = F(149800823443,10**12), F(149800823445,10**12)
XOUT_LO, XOUT_HI = F(157052266639,10**12), F(157052266641,10**12)

class Interval:
    def __init__(self, a, b=None):
        self.lo, self.hi = F(a), F(a if b is None else b)
        assert self.lo <= self.hi
    @staticmethod
    def cv(y): return y if isinstance(y,Interval) else Interval(y)
    def __add__(self,y):
        y=self.cv(y);return Interval(self.lo+y.lo, self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,y):return self + -self.cv(y)
    def __rsub__(self,y):return self.cv(y) + -self
    def __mul__(self,y):
        y=self.cv(y); p=[a*b for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return Interval(min(p),max(p))
    __rmul__=__mul__
    def __pow__(self,k):
        assert k>=0 and isinstance(k,int)
        if k==0:return Interval(1)
        if self.lo>=0:return Interval(self.lo**k,self.hi**k)
        if self.hi<=0:
            return Interval(self.lo**k,self.hi**k) if k%2 else Interval(self.hi**k,self.lo**k)
        return Interval(self.lo**k,self.hi**k) if k%2 else Interval(0,max(self.lo**k,self.hi**k))

def params(x,theta):
    u=U_A/(U_B-U_C*theta)
    T=(1-x)*(1-B*x+B*x*theta)
    return T,u,1-T,1-u*T

def mass(k,x,theta):
    T,u,p,q=params(x,theta)
    return comb(N,k)*(q**k*(1-q)**(N-k)-p**k*(1-p)**(N-k))

def tail(j,x,theta):
    return sum((mass(k,x,theta) for k in range(j,N+1)),Interval(0) if isinstance(x,Interval) else F(0))

def derivative_tail(j,x,theta):
    T,u,p,q=params(x,theta)
    Tprime=-(1-B*x+B*x*theta)+(1-x)*B*(theta-1)
    dp,dq=-Tprime,-u*Tprime
    return N*comb(N-1,j-1)*(q**(j-1)*(1-q)**(N-j)*dq-p**(j-1)*(1-p)**(N-j)*dp)

def G(x):return tail(9,x,E)-tail(9,x,F(0))
def H(x):return tail(10,x,E)-tail(10,x,F(0))
def delta(k,x,t):return mass(k,x,t)
def mix(k,x,lam):return (1-lam)*mass(k,x,F(0))+lam*mass(k,x,E)

def test():
    assert G(XIN_LO)<0<G(XIN_HI)
    assert delta(9,XOUT_LO,E)>0>delta(9,XOUT_HI,E)
    assert delta(9,A,E)>0 and delta(9,C,E)<0
    assert G(A)<0 and G(C)>0
    min_margins={key:None for key in ['E8neg','Z9neg','Z10neg','E10pos','M3_4_9neg','M1_3_10pos','Hneg','Gprimepos']}
    slabs=128
    for i in range(slabs):
        x=Interval(A+(C-A)*i/slabs,A+(C-A)*(i+1)/slabs)
        d={
        'E8neg':-delta(8,x,E).hi,
        'Z9neg':-delta(9,x,F(0)).hi,
        'Z10neg':-delta(10,x,F(0)).hi,
        'E10pos':delta(10,x,E).lo,
        'M3_4_9neg':-mix(9,x,F(3,4)).hi,
        'M1_3_10pos':mix(10,x,F(1,3)).lo,
        'Hneg':-F(1,100)-H(x).hi,
        'Gprimepos':(derivative_tail(9,x,E)-derivative_tail(9,x,F(0))).lo-F(1,4),
        }
        for name,bound in d.items():
            if bound<=0:raise AssertionError((i,name,float(bound)))
            if min_margins[name] is None or bound<min_margins[name]:min_margins[name]=bound
    print('PASS 128 exact interval slabs; strict margins vs claimed thresholds')
    for k,v in min_margins.items():print(k,'>',round(float(v),12))
    print('onset lies in',float(XIN_LO),float(XIN_HI))
    print('exit lies in',float(XOUT_LO),float(XOUT_HI))
    for x in (A,F(3,20),F(157,1000)):
        d9=delta(9,x,E)-delta(9,x,F(0))
        lam=-delta(9,x,F(0))/d9
        gam=-H(x)/d9
        print('width',float(x),'lambda9',round(float(lam),12),'gamma9',round(float(gam),12), 'G',round(float(G(x)),12))

if __name__=='__main__':test()
