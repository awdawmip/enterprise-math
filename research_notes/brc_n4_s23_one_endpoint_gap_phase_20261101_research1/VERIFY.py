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
    h=F(h);d=F(43)+42*h;q=lambda z:Q(z,0,d)
    l=q(F(1,2)-h);u=q(F(7,8));H=q(F(3,16)+h/2)
    V=[P(a,q(b),q(c)) for a,b,c in product(
        (l,u),(F(1,8),F(1,2)),(F(1,2),F(7,8)))]
    inputs=((l,F(1,8),F(7,8),F(4,9)),(l,F(1,2),F(1,2),F(1,18)),
            (u,F(1,8),F(7,8),F(2,9)),(u,F(1,2),F(1,2),F(5,18)))
    S=[P(a,q(b),q(c)) for a,b,c,_ in inputs]
    center=tuple(tuple(sum(q(w)*S[j][i][t] for j,(*_,w) in enumerate(inputs))
                     for t in range(4)) for i in range(6))
    assert max(D(v,center) for v in V)==H
    first=64*h*h+40*h-3<=0
    if first:
        r=(Q(0,1,d)-q(5))/8
        x=u-r;y=q(F(1,2))-q(F(4,3))*r
        c=(q(F(1,4))+q(F(7,16))*q(h))/(q(F(1,8))+r)
        assert 32*r*r+40*r-q(9+21*h)==q(0) and r>H
    else:
        r=H;x=q(F(11,16)-h/2);y=q(F(1,4)-2*h/3)
        c=q(F(1,4)+7*h/16)/q(F(5,16)+h/2)
        assert 32*r*r+40*r-q(9+21*h)>=q(0)
    assert l<=x<=u and q(F(1,8))<=y<=q(F(1,2))
    assert q(F(1,2))<=c<=q(F(7,8))
    assert max(D(v,P(x,y,c)) for v in V)==r
    return f"h={h} mode={'radical' if first else 'hull-tight'} lawful={r} hull={H} gap={r-H}"

if __name__=="__main__":
    tests=[F(0),F(1,1000),F(1,64),F(1,32),F(1,16),F(1,15),
           F(1,14),F(1,12),F(1,10),F(1,8)]
    for h in tests:print(check(h))
    h0=(Q(0,1,37)-Q(5,0,37))/16
    assert 64*h0*h0+40*h0-3==Q(0,0,37)
    assert Q(0,0,37)<h0<Q(F(1,8),0,37)
    s=Q(F(13,2),0,37)+4*h0
    assert s>Q(0,0,37) and s*s==43+42*h0
    assert (s-Q(5,0,37))/8==Q(F(3,16),0,37)+h0/2
    print("phase_boundary h*=(sqrt(37)-5)/16 exact polynomial and branch equality PASS")
    print("sources=6 rows=6 atoms=4 rational_boxes=10 vertices_per_box=8")
    print("PASS_BRC_N4_S23_ONE_ENDPOINT_EXACT_HULL_GAP_PHASE_20261101")
