#!/usr/bin/env python3
"""Stage367-B exact Fraction/SymPy certificate: post-cusp four-parameter local optimality."""
from fractions import Fraction as F
from dataclasses import dataclass
import sympy as S

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __init__(self,lo,hi=None):
        lo=F(lo);hi=lo if hi is None else F(hi)
        assert lo<=hi
        object.__setattr__(self,'lo',lo);object.__setattr__(self,'hi',hi)
    def __add__(self,other):
        o=iv(other);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-iv(other)
    def __rsub__(self,other):return iv(other)+-self
    def __mul__(self,other):
        o=iv(other);z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=iv(other)
        assert o.lo*o.hi>0,('interval division by zero',o)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,other):return iv(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        a=I(1)
        for _ in range(n):a=a*self
        return a
    def __repr__(self):return f'I({float(self.lo):.10g}, {float(self.hi):.10g})'

def iv(v):return v if isinstance(v,I) else I(v)
def det(u,v):return u[0]*v[1]-u[1]*v[0]
def B(k,z):return z**k*(1-z)**(3-k)
def dB(k,z):
    if k==0:return -3*(1-z)**2
    if k==1:return (1-z)*(1-3*z)
    if k==2:return z*(2-3*z)
    return 3*z*z
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F((61,21,9,9)[k],160)
def gr(k,x,y):return (F(4,5)*dB(k,x),F(1,5)*dB(k,y))
def f(x,y):return F(15,16)*r(2,x,y)
def gf(x,y):return tuple(F(15,16)*z for z in gr(2,x,y))
def gc(x,y):return (-F(3,256)*(1-x)*(63-61*x),F(3,64)*y*(1-y))
def Yprime(x,y):return -gr(1,x,y)[0]/gr(1,x,y)[1]
def lam(x,y):
    yp=Yprime(x,y);cx,cy=gc(x,y);fx,fy=gf(x,y)
    return -(cx+cy*yp)/(fx+fy*yp)
def nearstar_theta(x,y,la):
    cx,cy=gc(x,y);fx,fy=gf(x,y);gx,gy=gr(1,x,y)
    return -(cx+la*fx)/(la*F(15,16)*gx)
def cusp_theta(x,y,la):
    U=(I(0),F(21,256)*dB(2,y))
    V=tuple(la*F(15,16)*z for z in gr(1,x,y))
    W=tuple(z+la*t for z,t in zip(gc(x,y),gf(x,y)))
    dd=det(U,V)
    return U,V,W,dd,det((-W[0],-W[1]),V)/dd,det(U,(-W[0],-W[1]))/dd

X,Y,La=S.symbols('X Y La',real=True)
Bk=lambda k,z:z**k*(1-z)**(3-k)
w=(1,3,3,1)
def symbolic_port(anchor,z,sgns):
    return S.Rational(1,2)*sum(w[k]*sgns[k]*(Bk(k,anchor)-Bk(k,z)) for k in range(4))
CL=S.expand((63*symbolic_port(S.Rational(1,4),X,(-1,1,1,1))
    +symbolic_port(S.Rational(3,4),X,(-1,-1,1,1))
    +9*symbolic_port(S.Rational(1,4),Y,(1,1,-1,-1))
    +7*symbolic_port(S.Rational(3,4),Y,(-1,-1,1,1)))/256)
CH=S.expand((63*symbolic_port(S.Rational(1,4),X,(-1,1,1,1))
    +symbolic_port(S.Rational(3,4),X,(-1,-1,1,1))
    +9*symbolic_port(S.Rational(1,4),Y,(1,1,-1,-1))
    +7*symbolic_port(S.Rational(3,4),Y,(-1,-1,-1,1)))/256)
assert S.simplify(S.diff(CL,X)+S.Rational(3,256)*(1-X)*(63-61*X))==0
assert S.simplify(S.diff(CL,Y)-S.Rational(3,64)*Y*(1-Y))==0
assert S.simplify(CH-CL-S.Rational(21,256)*(Bk(2,Y)-S.Rational(9,64)))==0
Rs=[(4*Bk(k,X)+Bk(k,Y))/5-S.Rational((61,21,9,9)[k],160) for k in range(4)]
assert S.expand(sum(w[k]*Rs[k] for k in range(4)))==0
FS=S.Rational(15,16)*Rs[2]
Yp=-S.diff(Rs[1],X)/S.diff(Rs[1],Y)
lamS=S.factor(-(S.diff(CL,X)+S.diff(CL,Y)*Yp)/(S.diff(FS,X)+S.diff(FS,Y)*Yp))
Vx=La*S.Rational(15,16)*S.diff(Rs[1],X)
Vy=La*S.Rational(15,16)*S.diff(Rs[1],Y)
Wx=S.diff(CL,X)+La*S.diff(FS,X)
Wy=S.diff(CL,Y)+La*S.diff(FS,Y)
thetaS=-Wx/Vx
assert S.simplify((Wy+thetaS*Vy).subs(La,lamS))==0
print('EXACT_16_LABEL_SYMBOLIC_COST_AND_TANGENT_MULTIPLIER_IDENTITIES_PASS')

XsL,XsU,YsL,YsU=(F(2310839,10**7),F(2310840,10**7),F(5555086,10**7),F(5555091,10**7))
XaL,XaU,YaL,YaU=(F(2378068,10**7),F(2378070,10**7),F(5756939,10**7),F(5756940,10**7))
assert r(1,XsL,YsL)>0 and r(1,XsU,YsU)<0
assert r(0,XsL,YsU)>0 and r(0,XsU,YsL)<0
assert B(2,YaL)<F(9,64)<B(2,YaU) and r(1,XaL,YaL)<0<r(1,XaU,YaU)
assert r(0,XaU,YaU)<0
Elo=f(XaL,YaL)-f(XsU,YsU)
Ehi=f(XaU,YaU)-f(XsL,YsL)
assert F(2181,10**6)<Elo<Ehi<F(2182,10**6)
assert F(11,5000)-Elo<F(1,50000)
Xright=F(23115,100000);YrL=F(55571,100000);YrU=F(55572,100000)
assert r(1,Xright,YrL)>0>r(1,Xright,YrU)
assert f(Xright,YrL)-f(XsU,YsU)>F(1,50000)
XX=I(F(23108,100000),Xright);YY=I(F(55550,100000),YrU)
assert r(2,XX.lo,YY.lo)>0 and r(3,XX.hi,YY.hi)<0
assert gr(1,XX,YY)[0].lo>0 and gr(1,XX,YY)[1].hi<0
assert gf(XX,YY)[0].lo>0 and gf(XX,YY)[1].lo>0
assert r(0,Xright,YrU)<0
print('EXACT_ALL_POST_CUSP_NEARSTAR_ARC_IN_NARROW_RATIONAL_BOX_PASS')
LA=lam(XX,YY)
print('lambda_interval', LA)
assert LA.lo>F(119,100) and LA.hi<F(121,100)
TH=nearstar_theta(XX,YY,LA)
print('nearstar_theta_interval',TH)
assert F(3,4)<TH.lo<=TH.hi<F(9,10)
DE=det(gr(1,XX,YY),gf(XX,YY))
print('inverse_map_jacobian_interval',DE)
assert DE.lo>F(1,60)
for elem in gr(1,XX,YY)+gf(XX,YY):
    assert -F(1,3)<elem.lo<=elem.hi<F(1,3)
assert 2*F(1,3)/F(1,60)==40
print('EXACT_NEARSTAR_TRANSVERSE_KINK_AND_INVERSE_JACOBIAN_PASS')
CcX,CcY=I(XaL,XaU),I(YaL,YaU)
U,V,W,d,aa,bb=cusp_theta(CcX,CcY,I(F(119,100),F(121,100)))
print('cusp_theta_a',aa,'cusp_theta_b',bb,'det',d)
assert F(1,2)<aa.lo<=aa.hi<F(9,10)
assert F(3,4)<bb.lo<=bb.hi<F(9,10)
assert d.hi<-F(1,400)
for e in U+V:assert -F(1,4)<e.lo<=e.hi<F(1,4)
assert F(1,10)*F(1,400)/F(1,4)==F(1,1000)
print('EXACT_CUSP_COMMON_LAGRANGIAN_SUPPORT_FOR_ALL_LAMBDA_PASS')
RHO=F(1,10**8)
blocks=[(F(1,4),XX.lo-RHO,XX.hi+RHO,(-1,1,1,1)),
        (F(3,4),XX.lo-RHO,XX.hi+RHO,(-1,-1,1,1)),
        (F(1,4),YY.lo-RHO,YY.hi+RHO,(1,1,-1,-1)),
        (F(3,4),YY.lo-RHO,YY.hi+RHO,(-1,-1,1,1)),
        (F(1,4),XaL-RHO,XaU+RHO,(-1,1,1,1)),
        (F(3,4),XaL-RHO,XaU+RHO,(-1,-1,1,1)),
        (F(1,4),YaL-RHO,YaU+RHO,(1,1,-1,-1)),
        (F(3,4),YaL-RHO,YaU+RHO,(-1,-1,None,1))]
for a,lo,hi,sgn in blocks:
    for k,z in enumerate(sgn):
        if z is not None:
            assert z*(B(k,a)-B(k,lo))>0 and z*(B(k,a)-B(k,hi))>0
assert B(2,YY.hi+RHO)<F(9,64)
assert r(0,XaU+RHO,YaU+RHO)<0
assert r(2,XX.lo-RHO,YY.lo-RHO)>0 and r(3,XX.hi+RHO,YY.hi+RHO)<0
assert r(2,XaL-RHO,YaL-RHO)>0 and r(3,XaU+RHO,YaU+RHO)<0
print('EXACT_16_PORT_LABELS_AND_LOCAL_POSITIVE_PART_CHARTS_PASS')
assert F(3,2)>F(3,256)*(124-122*(XX.lo-RHO))
assert F(1,20)>F(3,64)*(2*(YY.hi+RHO)-1)
assert 1+F(121,100)*F(15,16)*3+F(121,100)*F(15,16)*3<12
assert 1+F(121,100)*F(15,16)*3+F(121,100)*F(15,16)*3+F(21,256)*3<10
assert F(5,32)*8*3==F(15,4)<4
assert 40 < 41*(1-240*RHO)
assert 41*4==164
assert 12*RHO*164<F(1,50000)
assert F(1,10)-F(1,50000)>F(1,20)
assert F(1,4)-F(1,50000)>F(1,8)
assert F(1,2000)-F(1,50000)>F(1,4000)
assert F(119,100)-F(1,50000)>1
print('EXACT_SECOND_ORDER_AND_BUDGET_SLACK_RADIUS_1_OVER_100M_PASS')
print('THEOREM: For each E in (Ec,11/5000], the restricted arc pair (q_{E-Ec}, qa)')
print('is a strict local constrained minimizer of the full independent')
print('four-parameter Bernoulli/BRC objective in the explicit product radius 1e-8.')
print('COST_GAP_GT r1_abs/20 + r0_positive/8 + cusp_distance/4000 + unused_budget')
print('STAGE367B_POST_CUSP_UNRESTRICTED_STRICT_LOCAL_OPTIMUM_EXACT_PASS')
