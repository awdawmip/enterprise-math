"""D25: original finite-field weighted 3F2 third jets and signed Fricke two-leg gauge.
Executed separately as a local full verifier; code is an exact reproducible subset.
"""
from math import comb, factorial
import sympy as s
x=s.symbols("x"); R=s.sqrt(2)
z=108*x*x*(x+9)*(x+8)**2/(x+12)**6
w=256*x**3*(x+8)*(x+9)**3/(x*x+36*x+216)**4
def hg(p,which):
    a=[1]
    for j in range(p-1):
        if which=="A":u=(2*j+1)*(3*j+1)*(3*j+2);v=18*(j+1)**3
        else:u=(4*j+1)*(2*j+1)*(4*j+3);v=32*(j+1)**3
        a.append(a[-1]*u*pow(v,-1,p)%p)
    return a
def jets(a,t,p):
    return [sum(c*factorial(j)//factorial(j-d)*pow(t,j-d,p)
        for j,c in enumerate(a) if j>=d)%p for d in (1,2,3)]
for p in range(13,1200,24):
    if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
    a=hg(p,"A");b=hg(p,"B")
    av=jets([(6*j+1)*c%p for j,c in enumerate(a)],pow(2,-1,p),p)
    bv=jets([(8*j+1)*c%p for j,c in enumerate(b)],pow(9,-1,p),p)
    assert av[0]!=0 and bv[0]!=0
    assert av[1]*pow(av[0],-1,p)%p==4*pow(3,-1,p)%p
    assert av[2]*pow(av[0],-1,p)%p==116*pow(9,-1,p)%p
    assert bv[1]*pow(bv[0],-1,p)%p==-99*pow(16,-1,p)%p
    assert bv[2]*pow(bv[0],-1,p)%p==29403*pow(256,-1,p)%p
ell_expr=-s.Rational(5,4)+s.Rational(11,12)*R
m_expr=s.Rational(65,9)-s.Rational(245,48)*R
for sign in (1,-1):
    t=sign*6*R
    def at(q):return s.simplify(s.radsimp(q.subs(x,t)))
    zp,zpp,zppp=[at(s.diff(z,x,d)) for d in (1,2,3)]
    wp,wpp,wppp=[at(s.diff(w,x,d)) for d in (1,2,3)]
    ra=s.Rational(4,3)*zp+zpp/zp
    rb=-s.Rational(99,16)*wp+wpp/wp
    sa=s.Rational(116,9)*zp*zp+4*zpp+zppp/zp
    sb=s.Rational(29403,256)*wp*wp-3*s.Rational(99,16)*wpp+wppp/wp
    ell=s.simplify((ra-rb)/2)
    gam2=s.simplify((sa-sb-3*ell*rb)/3)
    assert s.simplify(ell-(-s.Rational(5,4)+sign*s.Rational(11,12)*R))==0
    assert s.simplify(gam2-(s.Rational(65,9)-sign*s.Rational(245,48)*R))==0
print("PASS: 26 exact prime-field weighted third jets and two signed Fricke symbolic gauges")
