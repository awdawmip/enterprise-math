#!/usr/bin/env python3
"""PREFIX397: exact centered multivariate coefficient certificate; Fraction arithmetic."""
from fractions import Fraction as F
from collections import defaultdict
import json
BASE=[F(1),F(121,100),F(73,36),F(532313,23400),F(11531293,748800)]
R0=F(11,10);K0=BASE[2];S40=BASE[3];S50=BASE[4]
ROOT_BINS=[(F(-9,4),F(-19,10)),(F(-7,10),F(-3,5)),(F(-1,20),F(-1,50)),(F(1,10),F(1,5)),(F(19),F(20)),(F(150),F(180))]
ABS_BINS=[(F(1,50),F(1,20)),(F(1,10),F(1,5)),(F(3,5),F(7,10)),(F(19,10),F(9,4)),(F(19),F(20)),(F(150),F(180))]
ZERO=(0,0,0,0)
class P:
    def __init__(self,c=0):
        if isinstance(c,P):self.t=dict(c.t)
        elif isinstance(c,dict):self.t={k:F(v) for k,v in c.items() if v}
        else:self.t={ZERO:F(c)} if c else {}
    def __add__(self,other):
        other=P(other);d=self.t.copy()
        for k,v in other.t.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.t.items()})
    def __sub__(self,other):return self+-P(other)
    def __rsub__(self,other):return P(other)+-self
    def __mul__(self,other):
        other=P(other);d=defaultdict(F)
        for k,v in self.t.items():
            for q,w in other.t.items():d[tuple(a+b for a,b in zip(k,q))]+=v*w
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0 and int(n)==n
        out=P(1);base=self
        while n:
            if n%2:out=out*base
            base=base*base;n//=2
        return out
    def bound(self,rad):
        center=self.t.get(ZERO,F(0))
        spread=sum((abs(c)*F(rad[0])**key[0]*F(rad[1])**key[1]*F(rad[2])**key[2]*F(rad[3])**key[3] for key,c in self.t.items() if key!=ZERO),F(0))
        return center,spread
    def term_count(self):return len(self.t)
def endpoint_poly(z):
    z=F(z);R=F(1)+z*z
    dr=P({(1,0,0,0):1});dk=P({(0,1,0,0):1})
    ds4=P({(0,0,1,0):1});ds5=P({(0,0,0,1):1})
    r=P(R0)+dr;k=P(K0)+dk;s4=P(S40)+ds4;s5=P(S50)+ds5
    U=r*(1-z*z);V=2*r*z
    l4=56*U+24*V+72*R;m4=-24*U+56*V-40*R
    n4=78*U-8*V+(32*k+29*r**2+53-2*s4)*R
    l5=980*U+492*V+980*R;m5=-492*U+980*V-492*R
    n5=1418*U+(424*k+709*r**2+709-64*s5)*R
    D=l4*m5-m4*l5;C=m4*n5-m5*n4;T=l5*n4-l4*n5
    return C**2+T**2-k*D**2
class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.a,self.b=a.a,a.b
        else:self.a,self.b=F(a),F(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,y):
        y=I(y);return I(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,y):return self+-I(y)
    def __rsub__(self,y):return I(y)+-self
    def __mul__(self,y):
        y=I(y);v=[a*b for a in (self.a,self.b) for b in (y.a,y.b)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __pow__(self,n):
        assert n==2
        if self.a<=0<=self.b:return I(0,max(self.a**2,self.b**2))
        return I(min(self.a**2,self.b**2),max(self.a**2,self.b**2))
    def __truediv__(self,y):
        y=I(y);assert y.a*y.b>0
        return self*I(F(1,y.b),F(1,y.a))
    def sign(self):return '+' if self.a>0 else '-' if self.b<0 else '?'
def cu(z,r):
    z=F(z);return 1+r**2+2*r*F(1-z*z,1+z*z)
def cert(xi,eta=F(1,200)):
    assert F(0)<=xi<F(1,100)
    rr=xi*(1+BASE[1])/(R0*(1-xi))
    radii=[rr]+[xi*(1+BASE[j])/(1-xi) for j in (2,3,4)]
    signs=[];endpoint_margins=[]
    for zl,zh in ROOT_BINS:
        vals=[]
        for z in (zl,zh):
            c,d=endpoint_poly(z).bound(radii)
            vals.append('+' if c>d else '-' if c < -d else '?')
            endpoint_margins.append(str(abs(c)-d))
        assert vals in [['+','-'],['-','+']],(xi,zl,vals)
        signs.append(vals)
    r=I(R0-rr,R0+rr);assert r.a>1
    dsigns=[];determinant_margins=[]
    for zl,zh in ROOT_BINS:
        z=I(zl,zh);R=1+z**2
        d2=(3776-4032*r**2)*R-256*r*(1-z**2)+47104*r*z
        assert d2.sign() in ['+','-'],('det',xi,zl)
        dsigns.append(d2.sign())
        determinant_margins.append(str(d2.a if d2.sign()=='+' else -d2.b))
    observers=[]
    for lo,hi in ABS_BINS:
        lower=cu(hi,I(r.a)).a;upper=cu(lo,I(r.b)).b
        assert lower<upper
        observers.append((lower,upper))
    gaps=[observers[j][0]-observers[j+1][1] for j in range(5)]
    assert min(gaps)>2*eta,('observer',xi,str(min(gaps)))
    return {'raw_intensity_radius':str(xi),'coherent_absolute_error':str(eta),
        'normalized_radii':[str(v) for v in radii],
        'endpoint_signs':signs,'endpoint_sign_margins':endpoint_margins,
        'determinant_signs':dsigns,'determinant_sign_margins':determinant_margins,
        'observer_gap_lower_bounds':[str(x) for x in gaps],
        'min_observer_gap':str(min(gaps)),
        'min_observer_gap_minus_twice_eta':str(min(gaps)-2*eta),
        'endpoint_polynomial_terms':[endpoint_poly(z).term_count() for pair in ROOT_BINS for z in pair]}
if __name__=='__main__':
    result=cert(F(1,8000))
    print('PASS_RADIUS',result['raw_intensity_radius'],'MIN_GAP',float(F(result['min_observer_gap'])))
    print('PASS_PREFIX397_CENTERED_COEFFICIENT_CERTIFICATE')
    with open(__file__.replace('.py','_results.json'),'w',encoding='utf8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
