#!/usr/bin/env python3
"""PREFIX-434: exact rational verification for an external static five-Port complex-source model.
This is NOT a native X6 evolution or typed BRC execution.
"""
from fractions import Fraction as F

class Q:
    def __init__(self,re=0,im=0): self.re,self.im=F(re),F(im)
    def __add__(self,b):
        b=q(b);return Q(self.re+b.re,self.im+b.im)
    __radd__=__add__
    def __neg__(self): return Q(-self.re,-self.im)
    def __sub__(self,b): return self+-q(b)
    def __mul__(self,b):
        b=q(b);return Q(self.re*b.re-self.im*b.im,self.re*b.im+self.im*b.re)
    __rmul__=__mul__
    def __truediv__(self,b):
        b=q(b);d=b.abs2()
        return Q((self.re*b.re+self.im*b.im)/d,(self.im*b.re-self.re*b.im)/d)
    def abs2(self):return self.re*self.re+self.im*self.im
    def conj(self):return Q(self.re,-self.im)
    def __repr__(self):return f'({self.re},{self.im})'
def q(z):return z if isinstance(z,Q) else Q(z)
i=Q(0,1);one=Q(1);epsmax=F(1,10**6);rho=F(1,1000);eta=F(39,2000)
x=F(1,2000);y=-F(123,245)*x
v=Q(x,y)

def ports(u,v):
    h=(Q(5,9)+Q(3,7)*u)/2
    z1,z2,z3=u,one+u,v
    z4=h+Q(0,4)*v
    z5=Q(22,15)*(one+u)/8+Q(5,9)*v/4
    return z1,z2,z3,z4,z5

rows=[]
for tag,u in [('plus',i),('minus',-i)]:
    z1,z2,z3,z4,z5=ports(u,v)
    R=z1.abs2();S=z2.abs2();D=z3.abs2();Y=(one+v).abs2();F4=z4.abs2();F5=z5.abs2()
    K=abs(F4-41)
    assert R==1 and S==2
    assert D<=epsmax and D<=rho*rho
    assert abs(Y-1)<=eta and abs(F5-F(709,32))<=eta
    rows.append((R,S,D,Y,F5,F4,K))
    print(tag,'u=',u,'v=',v,'r=',R,'s=',S,'|v|^2=',D)
    print(tag,'|1+v|^2=',Y,'|z5|^2=',F5,'|z4|^2=',F4,'kappa=',K)
assert rows[0][:5]==rows[1][:5]
assert rows[0][5]!=rows[1][5]
assert rows[0][6]!=rows[1][6]
assert rows[0][5]<41<rows[1][5]
assert rows[1][6]>rows[0][6]
print('EXACT_OBJECTIVE_DIFFERENCE',rows[1][6]-rows[0][6])
print('FIFTH_PORT_OFFSET',rows[0][4]-F(709,32))
print('OBSERVED_FIBER_IDENTICAL_EXCEPT_TARGET: PASS')
print('ALL_CONSTRAINTS_AT_ETA_39_OVER_2000_EPS_ANY_IN_0_TO_1E-6: PASS')
for name,z in [('u+',i),('u-',-i),('v',v)]:
    re=((one+z).abs2()-(one-z).abs2())/4
    im=((one-Q(0,1)*z).abs2()-(one+Q(0,1)*z).abs2())/4
    assert re==z.re and im==z.im
    print('POLARIZATION_RECOVERS',name,re,im)
print('PASS_PREFIX434_EXACT_COMPLEX_RATIONAL_OBSERVER_WITNESS')
