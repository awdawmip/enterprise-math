#!/usr/bin/env python3
"""Exact Stage338-B double-zero BRC first-order obstruction certificate."""
from fractions import Fraction as Q
import sympy as S

m=(61,21,9,9)
w=(1,3,3,1)
def B(k,z):return z**k*(1-z)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-Q(m[k],160)

xl=Q(231083,10**6);xh=Q(231085,10**6)
yll=Q(5554961,10**7);yhl=Q(5554962,10**7)
ylh=Q(5555201,10**7);yhh=Q(5555202,10**7)
for x,lo,hi,sgn in [(xl,ylh,yhh,-1),(xh,yll,yhl,1)]:
    assert r(0,x,lo)>0 and r(0,x,hi)<0
    assert sgn*r(1,x,lo)>0 and sgn*r(1,x,hi)>0
assert r(2,xl,yll)>0 and r(3,xh,yhh)<0
patterns=[]
for a,lo,hi in ((Q(1,4),xl,xh),(Q(3,4),xl,xh),(Q(1,4),yll,yhh),(Q(3,4),yll,yhh)):
    left=''.join('+' if B(k,a)-B(k,lo)>0 else '-' for k in range(4))
    right=''.join('+' if B(k,a)-B(k,hi)>0 else '-' for k in range(4))
    assert all((B(k,a)-B(k,lo))*(B(k,a)-B(k,hi))>0 for k in range(4))
    assert left==right
    patterns.append(left)
assert patterns==['-+++','--++','++--','--++']
print('DOUBLE_ZERO_UNIQUE_ROOT_ENDPOINT_RATIONAL_BRACKETS_PASS')
print('DOUBLE_ZERO_RESIDUAL_SIGN_AND_ALL_16_TAGS_PASS',tuple(patterns))

class I:
    def __init__(self,a,b=None):
        self.a=Q(a);self.b=Q(a if b is None else b)
        assert self.a<=self.b
    @staticmethod
    def asI(v):return v if isinstance(v,I) else I(v)
    def __add__(self,v):
        v=self.asI(v);return I(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,v):return self+-self.asI(v)
    def __rsub__(self,v):return self.asI(v)+-self
    def __mul__(self,v):
        v=self.asI(v);q=[a*b for a in (self.a,self.b) for b in (v.a,v.b)]
        return I(min(q),max(q))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=self.asI(v);assert v.a*v.b>0
        return self*I(1/v.b,1/v.a)
    def __pow__(self,k):
        assert k>=0
        z=I(1)
        for _ in range(k):z=z*self
        return z

x=I(xl,xh);y=I(yll,yhh)
p=(1-x)*(189-183*x)/256
q=3*y*(1-y)/64
r0x=-Q(12,5)*(1-x)**2;r0y=-Q(3,5)*(1-y)**2
r1x=Q(4,5)*(1-x)*(1-3*x);r1y=Q(1,5)*(1-y)*(1-3*y)
r3x=Q(12,5)*x*x;r3y=Q(3,5)*y*y
N=-(q*(r3x+r0x)+p*(r3y+r0y))
D=3*(q*r1x+p*r1y)
assert -Q(15,1000)<N.a and N.b<-Q(14,1000)
assert -Q(73,1000)<D.a and D.b<-Q(70,1000)
beta=N/D
assert Q(14,73)<beta.a and beta.b<Q(15,70)
bx=-Q(5,16)*(r3x+r0x+3*beta*r1x)
by=-Q(5,16)*(r3y+r0y+3*beta*r1y)
assert bx.a>0 and by.b<0
print('N_BOUNDS',N.a,N.b)
print('D_BOUNDS',D.a,D.b)
print('BETA_INTERVAL',beta.a,beta.b,'WITHIN',Q(14,73),Q(15,70))
print('SUPPORTING_GRADIENT_BX',bx.a,bx.b,'BY',by.a,by.b)

X,Y,Be=S.symbols('X Y Be', real=True)
bs=lambda k,z:z**k*(1-z)**(3-k)
rr=lambda k:(4*bs(k,X)+bs(k,Y))/5-S.Rational(m[k],160)
px=(1-X)*(189-183*X)/256;qy=3*Y*(1-Y)/64
bx0=-S.Rational(5,16)*S.diff(rr(3)+rr(0)+3*Be*rr(1),X)
by0=-S.Rational(5,16)*S.diff(rr(3)+rr(0)+3*Be*rr(1),Y)
num=S.factor(-(qy*S.diff(rr(3)+rr(0),X)+px*S.diff(rr(3)+rr(0),Y)))
den=S.factor(3*(qy*S.diff(rr(1),X)+px*S.diff(rr(1),Y)))
assert S.factor((qy*bx0+px*by0).subs(Be,num/den))==0
assert S.simplify(num + S.Rational(9,1280)*(122*X**2*Y-61*X**2-32*X*Y**2-216*X*Y+124*X+16*Y**2+110*Y-63))==0
assert S.simplify(den-S.Rational(9,1280)*(X-1)*(Y-1)*(135*X*Y-61*X-173*Y+63))==0
print('SYMPY_EXACT_STATIONARITY_IDENTITY_PASS')
print('STAGE338B_R0_R1_DOUBLE_ZERO_KKT_EXACT_PASS')
