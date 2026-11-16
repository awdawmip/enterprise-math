#!/usr/bin/env python3
"""R749SSQ exact nonadjacent cutoff horizons; standard Python 3 + SymPy.
Rebuilds five labeled source counts, determinant identities, Bernstein signs,
certified algebraic three-read collision witnesses and four-read exclusions.
"""
from fractions import Fraction as F
import json
import math
import sympy as sp
from pathlib import Path

W = (1, 1, 2, 3, 6)
N = 40
n = [0] * (N+1); n[0] = 1
for w in W:
    for k in range(w,N+1): n[k] += n[k-w]
C = [0]*(N+1); T = [0]*(N+1)
for q in range(1,N+1):
    C[q] = C[q-1]+n[q-1]
    T[q] = T[q-1]+C[q-1]
e,d = sp.symbols('e d')
S = lambda q: 18*q**4+54*q**3-345*q**2+2070*q-16315

def row(q,p,j):
    a,b=q+6*j,p+6*j
    v=sp.Integer(b)**3*(C[a]+d)
    u=sp.Integer(a)**3*(T[a]+e)+sp.Rational(S(b)-S(a),108)*(C[a]+d)
    return [v,-u,C[b]*u-T[b]*v]

def primitive(p,variables):
    p=sp.Poly(p,*variables,domain=sp.QQ)
    den=sp.ilcm(*[v.q for v in p.coeffs()])
    z=sp.Poly(den*p.as_expr(),*variables,domain=sp.ZZ)
    return z.primitive()[1]

def h(q,p,js=(0,1,2)):
    return primitive(sp.expand(sp.det(sp.Matrix([row(q,p,j) for j in js]))),(e,d))

def bernstein_bivariate(P):
    x,y=sp.symbols('x y')
    r=sp.Poly(sp.expand(P.as_expr().subs({e:4*x-2,d:4*y-2})),x,y)
    a,b=r.degree(x),r.degree(y)
    return [sp.factor(sum(r.coeff_monomial(x**u*y**v)*sp.Rational(math.comb(i,u),math.comb(a,u))*sp.Rational(math.comb(j,v),math.comb(b,v))
                  for u in range(i+1) for v in range(j+1))) for i in range(a+1) for j in range(b+1)]

class I:
    def __init__(self,a,b=None):
        self.lo=F(a);self.hi=F(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,other):
        other=other if isinstance(other,I) else I(other)
        return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-other if isinstance(other,I) else self+I(-other)
    def __rsub__(self,other):return I(other)+-self
    def __mul__(self,other):
        other=other if isinstance(other,I) else I(other)
        values=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(values),max(values))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=other if isinstance(other,I) else I(other)
        assert other.lo*other.hi>0, ('interval denominator crosses zero',other.lo,other.hi)
        inv=I(F(1,other.hi),F(1,other.lo))
        return self*inv
    def __rtruediv__(self,other):return I(other)/self

def polyI(poly,var,interval):
    coef=sp.Poly(poly,var,domain=sp.QQ).all_coeffs()
    ans=I(0)
    for x in coef:ans=ans*interval+I(F(int(x.p),int(x.q)))
    return ans

def Y(q,ee,dd):
    return I(q**3)*(I(T[q])+ee)/(I(C[q])+dd)-I(F(S(q),108))

def inversion(q,p,ee,dd):
    y0=Y(q,ee,dd); y1=Y(q+6,ee,dd)
    x0=(y0+I(F(S(p),108)))/I(p**3)
    x1=(y1+I(F(S(p+6),108)))/I((p+6)**3)
    DD=(I(T[p+6]-T[p])-x1*I(C[p+6])+x0*I(C[p]))/(x1-x0)
    EE=x0*(I(C[p])+DD)-I(T[p])
    return EE,DD

def prove_collision(q,p,dd,elo,ehi):
    P=sp.Poly(h(q,p).as_expr().subs(d,sp.Rational(dd.numerator,dd.denominator)),e)
    lo,hi=sp.Rational(elo.numerator,elo.denominator),sp.Rational(ehi.numerator,ehi.denominator)
    assert P.eval(lo)*P.eval(hi)<0
    assert P.count_roots(lo,hi)==1
    E,D=inversion(q,p,I(elo,ehi),I(dd))
    assert -2<E.lo<=E.hi<2 and -2<D.lo<=D.hi<2
    # The two-read inverse is valid because its denominators are separated from 0.
    # The third-read determinant equals zero at the isolated exact algebraic root.
    return dict(q=q,p=p,denominator_error=str(dd),numerator_root_bracket=[str(elo),str(ehi)],
                primitive_quadratic=str(P.as_expr()),
                recovered_E_bracket=[str(E.lo),str(E.hi)],
                recovered_D_bracket=[str(D.lo),str(D.hi)])

# Exact independently reconstructed two-read collisions for the pairs to be sharp at m=3.
two_read=[]
for q,p,exE,exD in [
    (6,8,F(1173149794,1356947469),F(-153764778,150771941)),
    (8,10,F(48524220279,51776767012),F(-12269249984,12944191753)),
]:
    EE,DD=inversion(q,p,I(-1),I(-1))
    assert EE.lo==EE.hi==exE and DD.lo==DD.hi==exD
    assert -2<exE<2 and -2<exD<2
    for j in range(2):
        left=Y(q+6*j,I(-1),I(-1))
        right=Y(p+6*j,I(exE),I(exD))
        assert left.lo==left.hi==right.lo==right.hi
    two_read.append({"q":q,"p":p,"left_errors":["-1","-1"],"right_errors":[str(exE),str(exD)]})
# All three-read collisions at q6/p8 or q8/p10 are excluded by exact Bernstein signs.
H68=h(6,8)
b68=bernstein_bivariate(H68)
assert all(v<0 for v in b68) or all(v>0 for v in b68)
H810=h(8,10); b810=bernstein_bivariate(H810)
assert all(v<0 for v in b810) or all(v>0 for v in b810)

c79=prove_collision(7,9,F(-3,2),F(-1173743640,10**9),F(-1173743630,10**9))
c912=prove_collision(9,12,F(-7,4),F(-759826230,10**9),F(-759826220,10**9))

four=[]
for q,p, dlo,dhi in [
    (7,9,F(660727283709,10**12),F(660727283711,10**12)),
    (9,12,F(1390693182037,10**12),F(1390693182039,10**12)),
]:
    f,g=h(q,p,(0,1,2)),h(q,p,(0,1,3))
    R=sp.factor(sp.resultant(f.as_expr(),g.as_expr(),e))
    factors=sp.factor_list(R)[1]
    assert sorted([sp.degree(z,d) for z,m in factors])==[1,1,1,5]
    for fac,mult in factors:
        if sp.degree(fac,d)==1:
            assert sp.Poly(fac,d).count_roots(-2,2)==0
    Q=next(z for z,m in factors if sp.degree(z,d)==5)
    assert sp.Poly(Q,d).count_roots(-2,2)==1
    lo=sp.Rational(dlo.numerator,dlo.denominator)
    hi=sp.Rational(dhi.numerator,dhi.denominator)
    assert sp.Poly(Q,d).count_roots(lo,hi)==1
    assert sp.expand(Q).subs(d,lo)*sp.expand(Q).subs(d,hi)<0
    subs=sp.subresultants(f.as_expr(),g.as_expr(),e)
    sub=sp.Poly(subs[-2],e)
    assert sub.degree()==1
    A,B=sub.all_coeffs()
    di=I(dlo,dhi)
    ee= -polyI(B,d,di)/polyI(A,d,di)
    assert ee.lo>2 or ee.hi<-2
    four.append(dict(q=q,p=p,resultant_factor_degrees=[int(sp.degree(z,d)) for z,m in factors],
                     unique_inner_d_root_bracket=[str(dlo),str(dhi)],
                     forced_e_outer_bracket=[str(ee.lo),str(ee.hi)],
                     resultant_quintic=str(Q),
                     subresultant_linear_E_coefficient=str(A),subresultant_linear_constant=str(B)))

result={"schema":"R749SSQ_NONADJACENT_HORIZONS_EXACT_V1", "status":"PASS",
"frozen_science_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
"weights":list(W),"error_domain":"real common per state e,d in [-2,2]",
"exact_two_read_collisions":two_read,
"six_eight":{"H_sign":"strict fixed sign on full square","bernstein_min":str(min(b68)),"bernstein_max":str(max(b68)),"H_primitive":str(H68.as_expr()),"sharp_min_horizon":3},
"eight_ten":{"H_sign":"strict fixed sign on full square","bernstein_min":str(min(b810)),"bernstein_max":str(max(b810)),"H_primitive":str(H810.as_expr()),"three_read_separated":True,"sharp_min_horizon":3},
"exact_three_read_collisions":[c79,c912],"four_read_separation":four,
"classification":{"6_8":"exactly 3","7_9":"exactly 4","8_10":"exactly 3","9_12":"exactly 4"},
"validation":"Exact source enumeration, bivariate Bernstein sign, rational real-root isolation, strict interval arithmetic and quadratic subresultants; not independently reviewed",
"boundary":"Scalar five-source observer only; no native X6/BRC Port claim"}
output=Path(__file__).with_name('R749SSQ_NONADJACENT_OBSERVER_RESULTS.json')
output.write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print('PASS; 3/4 sharp nonadjacent horizons',result['classification'])
