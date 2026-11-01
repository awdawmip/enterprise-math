#!/usr/bin/env python3
"""Exact, reproducible author-side discriminant analysis for the static 5-port model.

Only rational/Gaussian rational symbolic algebra and exact Sturm root counts.
This does not call native X6/BRC time evolution, nor admit the result.
"""
import json
from pathlib import Path
import sympy as sp

I = sp.I
R = sp.Rational
t = sp.symbols('t', real=True)
u, v = sp.symbols('u v')
A = sp.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
               [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B = sp.simplify(A[3:,:] * A[:3,:].inv())
assert A[:3,:].det() != 0
assert B == sp.Matrix([[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],
                       [R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]])
# q_j(t) = Q_j(t)/59536. The common intensity scale cancels in ratios.
Q = [34000+204144*t, 3200+56336*t, 58250+1286*t,
     46600+12936*t, 31525+28011*t]
assert all(x.subs(t, 0)>0 and x.subs(t, R(1,4))>0 for x in Q)
F = []
for j in range(2):
    z=list(B.row(j))
    h=z[0]+z[1]*u+z[2]*v
    hstar=sp.conjugate(z[0])*Q[0]*u*v + sp.conjugate(z[1])*Q[1]*v + sp.conjugate(z[2])*Q[2]*u
    F.append(sp.expand(h*hstar-Q[j+3]*u*v))
(a4,b4,c4),(a5,b5,c5)=[sp.Poly(f,v).all_coeffs() for f in F]
# Closed formula for quadratic resultant (division by the known factor u).
num=sp.expand((a4*c5-c4*a5)**2-(a4*b5-b4*a5)*(b4*c5-c4*b5))
assert sp.rem(sp.Poly(num,u),sp.Poly(u,u)).is_zero
P=sp.Poly(sp.cancel(num/u),u)
assert P.degree()==6 and sp.Poly(P.as_expr(),t,u).total_degree()>0
assert sp.expand(num-sp.resultant(F[0],F[1],v))==0
D=sp.expand(a5*b4-a4*b5)
E=sp.expand(a5*c4-a4*c5)
assert sp.Poly(D,u).degree()==3

# Exact anti-holomorphic involution on P's roots for real t:
# J(u)=R2(t)/conjugate(u), where R2=Q2/Q1.
co=list(reversed(P.all_coeffs()))
C=sp.cancel(co[6]/sp.conjugate(co[0]))
for k in range(7):
    assert sp.cancel(co[k] - C*(Q[1]/Q[0])**(6-k)*sp.conjugate(co[6-k]))==0, k

Delta=sp.Poly(sp.discriminant(P.as_expr(),u),t)
assert Delta.degree()==40
const,fac=sp.factor_list(Delta.as_expr(),t)
assert len(fac)==5
factors={}
for f,e in fac:
    pp=sp.Poly(f,t)
    _, integer_poly=pp.clear_denoms(convert=True)
    integer_poly=integer_poly.primitive()[1]
    if integer_poly.LC()<0: integer_poly=-integer_poly
    key=f'degree_{integer_poly.degree()}'
    if integer_poly.degree()==1:
        key=f'linear_{len([q for q in factors if q.startswith("linear_")])+1}'
    factors[key]=(integer_poly,e)
assert sorted(e for _,e in factors.values())==[1,2,6,6,10]
assert {p.degree() for p,e in factors.values()}=={1,3,12}
L=[(p,e) for p,e in factors.values() if p.degree()==1]
assert sorted([e for p,e in L])==[6,6,10]
# Every linear factor root is strictly negative: the only real nonnegative
# discriminant candidates come from the cubic and degree-12 factors.
assert all(p.eval(0)>0 and p.LC()>0 for p,e in L)
H3=next(p for p,e in factors.values() if p.degree()==3 and e==2)
H12=next(p for p,e in factors.values() if p.degree()==12 and e==1)
assert sp.gcd(H3,H3.diff()).degree()==0
assert sp.gcd(H12,H12.diff()).degree()==0
assert H3.count_roots(R(0),R(1,4))==1
assert H12.count_roots(R(0),R(1,4))==2

BRACKETS={
 'first_ordinary_fold':('0.0140246596320690270474','0.0140246596320690270475'),
 'cubic_projection_exception':('0.0598990506977195435624','0.0598990506977195435625'),
 'second_ordinary_fold':('0.0669341021803707452694','0.0669341021803707452695')}
root_checks={}
for name,(lo,hi) in BRACKETS.items():
    left,right=R(lo),R(hi)
    H=H3 if name.startswith('cubic_') else H12
    assert right-left==R(1,10**22)
    assert H.eval(left)*H.eval(right)<0
    assert H.count_roots(left,right)==1
    root_checks[name]={'open_interval':[lo,hi], 'width':'1/10^22',
                       'factor_degree':H.degree(),'factor_root_count':1,
                       'strict_endpoint_signs':[int(sp.sign(H.eval(left))),int(sp.sign(H.eval(right)))]}
assert H12.count_roots(R(0),R(BRACKETS['first_ordinary_fold'][0]))==0
assert H12.count_roots(R(BRACKETS['first_ordinary_fold'][1]),R(BRACKETS['second_ordinary_fold'][0]))==0
assert H12.count_roots(R(BRACKETS['second_ordinary_fold'][1]),R(1,4))==0
assert H3.count_roots(R(0),R(BRACKETS['cubic_projection_exception'][0]))==0
assert H3.count_roots(R(BRACKETS['cubic_projection_exception'][1]),R(1,4))==0

# At either degree-12 simple discriminant zero, P has one double root.
# This root has unique finite v-lift because Res_u(P,D) has no H12 factor.
ResPD=sp.Poly(sp.resultant(P.as_expr(),D,u),t,extension=I)
assert ResPD.degree()==24
assert sp.gcd(ResPD,sp.Poly(H12.as_expr(),t,extension=I)).degree()==0
assert sp.gcd(ResPD,sp.Poly(H3.as_expr(),t,extension=I)).degree()==3
rd_fac=sp.factor_list(ResPD.as_expr(),t,extension=I)[1]
assert sorted((sp.Poly(f,t).degree(),e) for f,e in rd_fac)==[(1,6),(1,6),(1,6),(3,2)]
# Neither leading nor constant coefficient vanishes in 0<=t<=1/4.
for x in (P.LC(),P.TC()):
    ff=sp.factor_list(x,t,extension=I)[1]
    assert all(sp.Poly(f,t).degree()==1 and sp.re(sp.solve(f,t)[0])<0 for f,e in ff)

# Confirm that first H12 root is inside prior 6->4 endpoint interval,
# second H12 root inside prior 4->2 interval.
assert R('0.014024659632') < R(BRACKETS['first_ordinary_fold'][0])
assert R(BRACKETS['first_ordinary_fold'][1]) < R('0.014024659633')
assert R('0.066934102180') < R(BRACKETS['second_ordinary_fold'][0])
assert R(BRACKETS['second_ordinary_fold'][1]) < R('0.066934102181')

out={
 'schema':'PREFIX356_AUTHOR_EXACT_PARAMETRIC_DISCRIMINANT_V1',
 'status':'AUTHOR_SIDE_EXACT_SYMBOLIC_UNREVIEWED_NOT_ADMITTED',
 'scope':'Static auxiliary 5-Port complex 3D intensity inverse model, global phase quotient; not native X6/time/Detector',
 'frozen_input':{'A_gaussian_integer':[[str(x) for x in A.row(k)] for k in range(5)],
                 'Q_intensities_numerators':[str(q) for q in Q], 'denominator':59536},
 'identity':{'P_u_degree':6,'P_t_degree':4,'discriminant_t_degree':40,
             'discriminant_factor_pattern':[(p.degree(),e) for p,e in factors.values()],
             'root_inversion':'u -> Q2/(Q1*conjugate(u))'},
 'factors':{key:{'degree':pp.degree(),'multiplicity_in_discriminant':e,
                 'primitive_integer_coefficients_desc':[str(v) for v in pp.all_coeffs()],
                 'real_roots_in_[0,1/4]':int(pp.count_roots(0,R(1,4)))}
            for key,(pp,e) in factors.items()},
 'isolations':root_checks,
 'lift_obstruction_resultant':{'degree_t':ResPD.degree(),'gcd_with_H12_degree':0,'gcd_with_H3_degree':3,
                               'factor_degree_multiplicities':[(sp.Poly(f,t).degree(),k) for f,k in rd_fac]},
 'mathematical_consequences':[
  'The first degree-12 root is the earliest possible genuine physical Jacobian singular parameter for t>=0.',
  'Each degree-12 interval contains exactly one algebraic discriminant parameter; the simple zero and unique finite lift yield one physical ordinary fold, under the real involution.',
  'The positive cubic root is a projection/lift-degeneracy candidate: its physical status is not decided by this discriminant certificate alone.'
 ],
 'predecessor_endpoint_reference':'PREFIX-355 author-exact endpoint count certificates 6,4,4,2, not rerun here',
 'remaining':'Isolate and filter the positive cubic factor in the full (u,v) physical equations; complete independent Driver review and native X6/BRC faithful-transfer obligations.'
}
path=Path(__file__).with_name('RESULTS_PREFIX356.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('PASS_PREFIX356_EXACT_DEG40_DISCRIMINANT_TWO_ORDINARY_FOLDS_AND_ONE_PROJECTION_EXCEPTION')
for name,r in root_checks.items(): print(name,r['open_interval'])
print('Res(P,D) gcd degree-12 factor = 0; positive cubic exception retained')
