#!/usr/bin/env python3
"""PREFIX-398: exact observer eliminant, rational nominal decision and noisy five-port counterexample.
Requires Python 3.11+ and SymPy. All certified comparisons are exact rational.
"""
from fractions import Fraction as F
import sympy as sp
import json

z,w,q=sp.symbols("z w q")
d=sp.symbols("d0:4")
I0=[F(1),F(121,100),F(73,36),F(532313,23400),F(11531293,748800)]
r0,k0,s40,s50=F(11,10),I0[2],I0[3],I0[4]
xi,eta=F(1,8000),F(1,200)
ZB=[(F(-9,4),F(-19,10)),(F(-7,10),F(-3,5)),(F(-1,20),F(-1,50)),(F(1,10),F(1,5)),(F(19),F(20)),(F(150),F(180))]
AB=[(F(1,50),F(1,20)),(F(1,10),F(1,5)),(F(3,5),F(7,10)),(F(19,10),F(9,4)),(F(19),F(20)),(F(150),F(180))]
Q5=247273497*z**5-45399147334*z**4+719077831171*z**3+1525709995366*z**2-179308209566*z-8362430980
F6=sp.Poly(sp.expand((3*z+2)*Q5),z,domain=sp.QQ)
def S(x):
    return sp.Rational(x.numerator,x.denominator) if isinstance(x,F) else sp.Rational(x)
def rat(x):
    x=sp.Rational(x);return F(int(x.p),int(x.q))
def H(zv,rv,kv,v4,v5):
    R=1+zv**2;U=rv*(1-zv*zv);V=2*rv*zv
    l4=56*U+24*V+72*R;m4=-24*U+56*V-40*R
    n4=78*U-8*V+(32*kv+29*rv**2+53-2*v4)*R
    l5=980*U+492*V+980*R;m5=-492*U+980*V-492*R
    n5=1418*U+(424*kv+709*rv**2+709-64*v5)*R
    D=l4*m5-m4*l5;C=m4*n5-m5*n4;T=l5*n4-l4*n5
    return C*C+T*T-kv*D*D
def cu(zv,rv):
    return 1+rv*rv+2*rv*(1-zv*zv)/(1+zv*zv)
def nominal_cu(zv):
    return (F(441)+zv*zv)/(100*(1+zv*zv))
def centered(zv,radii):
    p=sp.Poly(sp.expand(H(S(zv),S(r0)+d[0],S(k0)+d[1],S(s40)+d[2],S(s50)+d[3])),*d,domain=sp.QQ)
    c,b=F(0),F(0)
    for powers,value in p.terms():
        if sum(powers)==0:c=rat(value)
        else:
            v=abs(rat(value))
            for j,n in enumerate(powers):v*=radii[j]**n
            b+=v
    return c,b,len(p.terms())
def nominal_decide(measured,noise,max_steps=512):
    lo,hi=measured-noise,measured+noise
    for a0,b0 in ZB:
        for t in (lo,hi):
            f=sp.Poly((441-100*S(t))+(1-100*S(t))*z*z,z,domain=sp.QQ)
            g=sp.gcd(F6,f)
            if g.degree() and g.count_roots(S(a0),S(b0))>0:
                return True,"ALGEBRAIC_BOUNDARY"
        a,b=a0,b0;fa=F6.eval(S(a))
        for step in range(max_steps+1):
            assert a*b>0
            zl,zh=min(abs(a),abs(b)),max(abs(a),abs(b))
            cmin,cmax=nominal_cu(zh),nominal_cu(zl)
            if cmin>=lo and cmax<=hi:return True,"INSIDE"
            if cmax<lo or cmin>hi:break
            if step==max_steps:raise RuntimeError("More rational halvings required")
            m=(a+b)/2;fm=F6.eval(S(m))
            if fm==0:
                if lo<=nominal_cu(m)<=hi:return True,"RATIONAL_EXACT_ROOT"
                break
            if fa*fm<0:b=m
            else:a,fa=m,fm
    return False,"ALL_SIX_EXCLUDED"
def main():
    assert sp.factor(H(z,S(r0),S(k0),S(s40),S(s50))/(1+z*z)+sp.Rational(352,950625)*F6.as_expr())==0
    R=1+z*z
    D2=(3776-4032*S(r0)**2)*R-256*S(r0)*(1-z*z)+47104*S(r0)*z
    assert sp.gcd(F6,sp.Poly(D2,z)).degree()==0
    for a,b in ZB:
        assert F6.count_roots(S(a),S(b))==1 and F6.eval(S(a))*F6.eval(S(b))<0
    e=o=0
    for (j,),v in F6.terms():
        if j%2:o+=v*w**(j//2)
        else:e+=v*w**(j//2)
    res=sp.Poly(sp.expand(e*e-w*o*o),w)
    obs=sp.Poly(sp.expand(sum(v*(441-100*q)**p[0]*(100*q-1)**(6-p[0]) for p,v in res.terms())),q)
    assert obs.degree()==6 and obs.rem(sp.Poly(1300*q-3973,q)).is_zero
    assert obs.sqf_part().degree()==6
    assert nominal_decide(F(3973,1300),F(0))[0]
    assert nominal_decide(F(3973,1300)+F(1,400),eta)[0]
    measured=F(44101,10100)
    assert not nominal_decide(measured,eta)[0]
    radii=[xi*(1+I0[1])/(r0*(1-xi))]
    radii += [xi*(1+I0[j])/(1-xi) for j in (2,3,4)]
    p,b,n=centered(F(1,8),radii);p2,b2,n2=centered(F(3,20),radii)
    assert n==n2==40 and p>b and p2<-b2
    rmin,rmax=r0-radii[0],r0+radii[0]
    assert rmin>1
    margin=measured-cu(F(1,8),rmax)-eta
    assert margin>0
    gaps=[]
    for j,(a,b) in enumerate(AB):
        low,high=cu(b,rmin),cu(a,rmax)
        if j==1:assert low<measured<high
        else:
            gap=max(low-measured,measured-high)-eta
            assert gap>0
            gaps.append(gap)
    print("PASS_PREFIX398_EXACT_SIX_SOURCE_OBSERVER_ELIMINANT_AND_RATIONAL_DECIDER")
    print("PASS_PREFIX398_STRICT_FALSE_POSITIVE_UNDER_FIVE_INTENSITY_AND_CU_NOISE")
    print("EXACT_MARGIN",margin,"FIVE_OTHER_MARGINS",",".join(map(str,gaps)))
if __name__=="__main__":
    main()
