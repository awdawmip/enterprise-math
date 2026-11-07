"""Exact Fraction and quadratic-field BRC/S23 endpoint-gap verification."""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import total_ordering
from itertools import product

@total_ordering
@dataclass(frozen=True)
class Q:
    a:F; b:F; d:F
    def __init__(self,a=0,b=0,d=1):
        object.__setattr__(self,"a",F(a))
        object.__setattr__(self,"b",F(b))
        object.__setattr__(self,"d",F(d))
        assert self.d>0
    def cv(self,x):
        if isinstance(x,Q):
            assert x.d==self.d
            return x
        return Q(x,0,self.d)
    def __add__(self,x):
        y=self.cv(x);return Q(self.a+y.a,self.b+y.b,self.d)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b,self.d)
    def __sub__(self,x):return self+-self.cv(x)
    def __rsub__(self,x):return self.cv(x)-self
    def __mul__(self,x):
        y=self.cv(x)
        return Q(self.a*y.a+self.b*y.b*self.d,self.a*y.b+self.b*y.a,self.d)
    __rmul__=__mul__
    def __truediv__(self,x):
        y=self.cv(x);z=y.a*y.a-y.b*y.b*self.d
        assert z!=0
        return Q((self.a*y.a-self.b*y.b*self.d)/z,
                 (self.b*y.a-self.a*y.b)/z,self.d)
    def __rtruediv__(self,x):return self.cv(x)/self
    def sign(self):
        a,b=self.a,self.b
        if b==0:return (a>0)-(a<0)
        if a==0:return (b>0)-(b<0)
        if (a>0)==(b>0):return (a>0)-(a<0)
        t=b*b*self.d-a*a
        if t==0:return 0
        return (t>0)-(t<0) if b>0 else (t<0)-(t>0)
    def __eq__(self,x):return (self-self.cv(x)).sign()==0
    def __lt__(self,x):return (self-self.cv(x)).sign()<0
    def __abs__(self):return self if self.sign()>=0 else -self
    def __str__(self):
        return str(self.a) if self.b==0 else f"({self.a})+({self.b})*sqrt({self.d})"

def F4(a,b,c):
    one=a.cv(1)
    return a,(one-a)*b,(one-a)*(one-b)*c,(one-a)*(one-b)*(one-c)

def P(a,b,c):
    d=a.d;q=lambda v:Q(v,0,d)
    S=[F4(a,b,q(F(1,2))),F4(a,b,q(F(1,2))),F4(a,q(0),c),
       F4(q(F(1,4)),b,q(F(1,2))),F4(q(F(1,4)),b,q(F(1,2))),
       F4(q(F(1,4)),q(F(1,3)),q(F(1,2)))]
    M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
    out=tuple(tuple(sum(q(F(M[i][j],20))*S[j][t] for j in range(6))
                        for t in range(4)) for i in range(6))
    assert all(sum(row)==q(1) and all(z>=q(0) for z in row) for row in out)
    assert out[0]==out[1] and out[3]==out[4]
    return out

def TV(x,y):return sum(abs(a-b) for a,b in zip(x,y))/2
def D(X,Y):return max(TV(x,y) for x,y in zip(X,Y))

def check(h):
    h=F(h); d=F(43)+24*h; q=lambda z:Q(z,0,d)
    lo=q(F(1,8)-h); hi=q(F(1,2))
    r=(Q(0,1,d)-q(5))/8
    H=q(F(3,16)+h/4)
    assert q(0)<=lo<=q(F(1,8)) and r>H
    assert 32*r*r+40*r-q(9+12*h)==q(0)
    s=q(F(1,8))+r
    x=q(F(7,8))-r; y=q(F(1,2))-q(F(4,3))*r
    t=q(F(1,4))/s
    assert q(F(1,2))<=x<=q(F(7,8))
    assert lo<=y<=hi and q(F(1,2))<=t<=q(F(7,8))
    V=[P(a,b,c) for a,b,c in product((q(F(1,2)),q(F(7,8))),
        (lo,hi),(q(F(1,2)),q(F(7,8))))]
    A=P(x,y,t)
    L=P(q(F(1,2)),lo,q(F(7,8)))
    U=P(q(F(7,8)),hi,q(F(1,2)))
    C=tuple(tuple((u+v)/2 for u,v in zip(row1,row2))
            for row1,row2 in zip(L,U))
    assert max(D(v,A) for v in V)==r
    assert max(D(v,C) for v in V)==H
    return f"h={h} lawful={r} hull={H} gap_positive=PASS"

if __name__=="__main__":
    tests=[F(0),F(1,4096),F(1,1024),F(1,800),F(1,256),F(1,128),
           F(1,64),F(1,32),F(1,20),F(1,16),F(1,12),F(1,10),F(1,9),F(1,8)]
    for h in tests: print(check(h))
    assert 16*46>27*27
    print("exact_cases=14 vertices_per_case=8 preparation_rows=6 atoms=4")
    print("PASS_BRC_N4_S23_SHARED_B_LOWER_FULL_ADMISSIBLE_GAP_20261101")
