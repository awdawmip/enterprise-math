#!/usr/bin/env python3
"""R749STT exact certificate for the 73/85 three-read problem.
Requires Python 3 and SymPy. No floating-point proof steps.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
import sympy as s

W=(1,1,2,3,6); N=97
part=[0]*(N+1); part[0]=1
for w in W:
    for k in range(w,N+1): part[k]+=part[k-w]
C=[0]*(N+1); T=[0]*(N+1)
for n in range(1,N+1):
    C[n]=C[n-1]+part[n-1]
    T[n]=T[n-1]+C[n-1]
assert [(C[n],T[n]) for n in (73,79,85,91,97)] == [
    (707343,8931013),(1020943,13914446),(1436968,21025004),
    (1978664,30933812),(2672553,44459556)]

def S(n): return 18*n**4+54*n**3-345*n**2+2070*n-16315
def Y(n,e,d): return Q(n**3*(T[n]+e),C[n]+d)-Q(S(n),108)
a=(Q(1),-Q(21,10),Q(11,10))
def L(n,e,d): return sum(a[j]*Y(n+6*j,e,d) for j in range(3))

# R749STR's explicit rational 2-read collision at h=2, independently checked.
e=Q(-3017722237060578733161,1527694442423074582592)
d=Q(1445925897017416432877,763847221211537291296)
E=Q(7,5); D=Q(2)
assert all(-2<z<2 for z in (e,d,E)) and D==2
assert Y(73,e,d)==Y(85,E,D)
assert Y(79,e,d)==Y(91,E,D)

# Exact positivity for derivatives via tensor Bernstein coefficients.
# x,z range over [0,1]; denominators are verified positive on this box.
u,v,x,z=s.symbols('u v x z')
def symbolic_L(n):
    return sum(s.Rational(a[j].numerator,a[j].denominator)*
               (n+6*j)**3*(T[n+6*j]+u)/(C[n+6*j]+v)
               for j in range(3))

def bernstein(poly):
    m=poly.degree(x); k=poly.degree(z)
    dct=dict(poly.terms()); ans=[]
    for i in range(m+1):
        for j in range(k+1):
            value=sum(dct.get((r,t),0)*s.Rational(s.binomial(i,r),s.binomial(m,r)) *
                      s.Rational(s.binomial(j,t),s.binomial(k,t))
                      for r in range(i+1) for t in range(j+1))
            ans.append(value)
    return ans

checks={}; total=0
for n in (73,85):
    g=symbolic_L(n)
    for label,expr in [('positive_d_e',s.diff(g,u)),
                       ('positive_signed_d_d',-s.diff(g,v) if n==73 else s.diff(g,v))]:
        # For 73: u=-2+4x. For 85: u=2-4x. In both v=-2+4z.
        expr=s.cancel(expr.subs({u:(-2+4*x if n==73 else 2-4*x),v:-2+4*z}))
        numerator,denominator=s.fraction(expr)
        poly=s.Poly(s.expand(numerator),x,z)
        den=s.Poly(s.expand(denominator),x,z)
        b=bernstein(poly)
        assert b and all(w>0 for w in b)
        assert all(w>0 for w in den.coeffs())
        checks[f'{n}_{label}']={'bernstein_count':len(b),
            'strictly_positive':len(b), 'min_bernstein':str(min(b)),
            'denominator_coefficients_positive':len(den.coeffs())}
        total+=len(b)

# L_73 increases in e, decreases in d; L_85 increases in E and D.
# This sharp lower bound is attained at (-2,2,2,2).
delta=L(73,Q(-2),Q(2))-L(85,Q(2),Q(2))
assert delta==Q(67536937868192626099237277,18291917078444373205412530425)
assert delta>0
noise=delta/Q(42,5)
assert noise>0
output={
 'unit':'R749STT','frozen_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'model':'five distinct labeled sources, weights (1,1,2,3,6)',
 'candidates':[73,85], 'read_indices':[0,1,2],
 'status':'AUTHOR_EXACT_NOT_REVIEWED',
 'two_read_exact_collision':{'e':str(e),'d':str(d),'E':str(E),'D':str(D),
  'equalities':['Y_73(e,d)=Y_85(E,D)','Y_79(e,d)=Y_91(E,D)']},
 'linear_three_read_statistic_coefficients':['1','-21/10','11/10'],
 'exact_attained_lower_bound':str(delta),
 'attaining_parameters':[-2,2,2,2],
 'strict_additive_noise_per_raw_read':'eta < '+str(noise),
 'derivative_sign_checks':checks, 'total_positive_bernstein_coefficients':total,
 'counts':{str(n):{'C':C[n],'T':T[n]} for n in (73,79,85,91,97)},
 'conclusion':'m_initial({73,85})=3 for candidate-wise fixed real nuisance pairs in [-2,2]^2',
 'scope':'Auxiliary scalar observer only; no native X6/Port/Cell correspondence.',
 'open_problem':'Determine exact first-horizon for pair 73/79; retain full source provenance in any BRC lift.'
}
Path(__file__).with_name('R749STT_THREE_READ_73_85_RESULTS.json').write_text(
    json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: exact 2-read collision; 4 gradient Bernstein boxes;',total,'positive coefficients; exact 3-read margin')
print('delta =',delta,'noise eta <',noise)
