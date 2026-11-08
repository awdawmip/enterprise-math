#!/usr/bin/env python3
"""Exact Q(sqrt(2)) check of original-E3 degree-two isogeny on H1_dR.
Author-side check: does NOT execute the fixed native H0/B0 divided-power object.
"""
from fractions import Fraction as F

class Q2:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=cv(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self+-cv(o)
    def __rsub__(self,o): return cv(o)-self
    def __mul__(self,o):
        o=cv(o); return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        assert d!=0
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o): return self*cv(o).inv()
    def __rtruediv__(self,o): return cv(o)/self
    def __eq__(self,o):
        o=cv(o); return self.a==o.a and self.b==o.b
    def sigma(self): return Q2(self.a,-self.b)
    def tuple(self): return (str(self.a),str(self.b))

def cv(o): return o if isinstance(o,Q2) else Q2(o)

T=Q2(0,1)
e=(2*T-3)/36
es=e.sigma()
a=T/6
b=(3-2*T)/432
assert T*T==2
assert a/2+es-e==-T/36
assert T*(a/2+es-e)==-Q2(1)/18
# d(z/u)=(u-b/u)*du/(2z), where z^2=f(u)=u^3+a*u^2+b*u
for u in [Q2(1),Q2(2),Q2(-5),Q2(3,1),Q2(2,3),Q2(1,-2)]:
    f=u*u*u+a*u*u+b*u
    fp=3*u*u+2*a*u+b
    assert (u*fp-2*f)/(u*u)==u-b/u
    U=u+a+b/u
    # Phi*beta_sigma=T*beta-omega/18-(T/2)*d(z/u)
    assert T*(U/2+es)==T*(u+e)-Q2(1)/18-(T/2)*(u-b/u)
C=((T,-Q2(1)/18),(Q2(0),T))
Cs=((T.sigma(),-Q2(1)/18),(Q2(0),T.sigma()))
prod=lambda A,B: tuple(tuple(sum((A[i][k]*B[k][j] for k in range(2)),Q2()) for j in range(2)) for i in range(2))
assert prod(C,Cs)==((Q2(-2),Q2()),(Q2(),Q2(-2)))
# The Galois-compatible basis beta_tilde=beta-(T/72)*omega
lam=-T/72
assert -Q2(1)/18+T*lam.sigma()==T*lam
print({'field':'Q[T]/(T^2-2)','off_diagonal':(-Q2(1)/18).tuple(),
       'original_basis_matrix':[[(v.tuple()) for v in row] for row in C],
       'conjugate_composition':'-2*I','diagonalizing_shift':lam.tuple(),
       'test_points':6,'status':'PASS','native_H0B0':'NOT_EXECUTED'})
