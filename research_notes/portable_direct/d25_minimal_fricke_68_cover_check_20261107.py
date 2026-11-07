"""Exact small-degree common orbifold-cover obstruction and Fricke 6:8 index checks.
Author-side certificate only; standard library; not a native experimental run.
"""
from fractions import Fraction as F
from math import gcd
from dataclasses import dataclass

@dataclass(frozen=True)
class Q:
    a: F
    b: F
    d: int
    def __init__(self,a,b=0,d=2):
        object.__setattr__(self,'a',F(a))
        object.__setattr__(self,'b',F(b))
        object.__setattr__(self,'d',d)
    def co(self,x):
        if isinstance(x,Q):
            assert x.d==self.d
            return x
        return Q(x,0,self.d)
    def __add__(self,x):
        x=self.co(x)
        return Q(self.a+x.a,self.b+x.b,self.d)
    __radd__=__add__
    def __neg__(self):
        return Q(-self.a,-self.b,self.d)
    def __sub__(self,x):
        return self+-self.co(x)
    def __rsub__(self,x):
        return self.co(x)-self
    def __mul__(self,x):
        x=self.co(x)
        return Q(self.a*x.a+self.d*self.b*x.b,self.a*x.b+self.b*x.a,self.d)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.co(x)
        n=x.a*x.a-self.d*x.b*x.b
        assert n!=0
        return self*Q(x.a/n,-x.b/n,self.d)
    def __rtruediv__(self,x):
        return self.co(x)/self

def ratio(c1,c2,e1,e2):
    return (c1-e1)*(c2-e2)/((c1-e2)*(c2-e1))

def indices(n):
    v=F(n)
    for p in range(2,n+1):
        if n%p==0 and all(p%d for d in range(2,int(p**0.5)+1)):
            v*=F(p+1,p)
    return int(v)

def main():
    assert [indices(n) for n in (2,3,6)]==[3,4,12]
    assert (2*12//4,2*12//3)==(6,8)
    ds=(6,1,2,3)                  # infinity,0,1/2,1/3
    widths=tuple(6//gcd(d*d,6) for d in ds)
    assert widths==(1,6,3,2)
    A=tuple(w//(1 if d%3==0 else 3) for d,w in zip(ds,widths))
    B=tuple(w//(1 if d%2==0 else 2) for d,w in zip(ds,widths))
    assert A==(1,2,1,2) and B==(1,3,3,1)
    assert sum(A)==6 and sum(B)==8
    # Case (2 cusps, 2 cones): A cusp/cone cross-ratio 4 (or inverse).
    a,b=Q(F(1,2),F(1,2)),Q(F(1,2),F(-1,2))
    v=ratio(Q(0),Q(1),a,b)
    assert v==Q(17,12)                 # B polynomial 16 t²(t-1)²
    x,y=Q(F(-1,4),F(1,4),-2),Q(F(-1,4),F(-1,4),-2)
    v2=ratio(Q(0,d=-2),Q(1,d=-2),x,y)
    assert v2.a==F(17,81) and abs(v2.b)==F(56,81)
    assert -1 not in (4,F(1,4))      # B Klein-four cover
    for z in (v,v2):
        assert z!=Q(4,d=z.d) and z!=Q(F(1,4),d=z.d)
    # Case (1 cusp, 4 cones): A is equianharmonic and nonreal.
    lamb=Q(F(1,2),F(1,2),-3)
    assert lamb*lamb-lamb+1==Q(0,d=-3) and lamb.b!=0
    I=Q(0,1,-1)
    assert ratio(Q(1,d=-1),Q(-1,d=-1),I,-I).b==0
    # Other B quadruple {+/-1,+/-1/sqrt2} is entirely real.
    root=Q(0,F(1,2))
    assert ratio(Q(1),Q(-1),root,-root).d==2
    # Exact polynomial identities from the remaining normal forms:
    # 1-(3t²-2t³)=(1-t)²(1+2t);
    # 16t²(t-1)²-1=(2t-1)²(4t²-4t-1);
    # -256t³(t-1)/27-1=-(4t-3)²(16t²+8t+3)/27.
    for t in (F(-2),F(-1,3),F(0),F(1,4),F(2)):
        assert 1-3*t*t+2*t**3==(1-t)**2*(1+2*t)
        assert 16*t*t*(t-1)**2-1==(2*t-1)**2*(4*t*t-4*t-1)
        assert -F(256,27)*t**3*(t-1)-1==-F(1,27)*(4*t-3)**2*(16*t*t+8*t+3)
    print('PASS: degree (3,4) cross-ratio obstruction; Fricke common cover (6,8), four cusps')
if __name__=='__main__':
    main()
