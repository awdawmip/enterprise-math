#!/usr/bin/env python3
"""R749STD: exact Poincare-Miranda certificate for four-read collision (602,604).
Five distinctly labelled sources (1,1,2,3,6), real shared errors in [-2,2].
Pinned scientific model: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Author-level exact rational certificate, not independent project review.
"""
import json
import sympy as sp
from pathlib import Path

q, p = 602, 604
M = p+24
wts=(1,1,2,3,6)
a=[0]*(M+1);a[0]=1
for w in wts:
    for k in range(w,M+1): a[k]+=a[k-w]
C=[0]*(M+1); T=[0]*(M+1)
for n in range(1,M+1):
    C[n]=C[n-1]+a[n-1]
    T[n]=T[n-1]+C[n-1]
assert C[73]==707343 and T[73]==8931013
assert C[77]==906087 and T[77]==12046216

s,e,d,u,v=sp.symbols('s e d u v')
S=lambda n:18*n**4+54*n**3-345*n**2+2070*n-16315
U=[]; W=[]; t=[]
for j in range(5):
    aa,bb=q+6*j,p+6*j
    t0=C[aa]+d
    alpha=sp.Rational(aa**3,bb**3)
    beta=sp.Rational(S(bb)-S(aa),108*bb**3)
    u0=sp.expand(alpha*(T[aa]+e)+beta*t0)
    w0=sp.expand(C[bb]*u0-T[bb]*t0)
    t.append(t0);U.append(u0);W.append(w0)

# x_j=U_j/t_j, v_j=W_j/t_j; E-x_j D=v_j
A=sp.expand(W[0]*t[1]-W[1]*t[0])
B=sp.expand(U[1]*t[0]-U[0]*t[1])
En=sp.expand(W[0]*B+U[0]*A)
Ed=sp.expand(t[0]*B)
# F_j (j=2,3,4) is a determinant of three observation equations
P={}
for j in (2,3,4):
    raw=sp.expand((W[0]*t[1]-W[1]*t[0])*(U[j]*t[0]-U[0]*t[j])-
                   (W[0]*t[j]-W[j]*t[0])*(U[1]*t[0]-U[0]*t[1]))
    # cancel factor t_0 when present, retaining same zeros since t_0>0
    pol=sp.Poly(raw,e,d)
    quot,rem=sp.div(pol,sp.Poly(t[0],e,d))
    assert rem.is_zero
    P[j]=sp.expand(quot.as_expr())
assert all(sp.Poly(P[j],e,d).total_degree()<=3 for j in (2,3,4))

# Exact rational certified center, radius 1e-11.
ec=sp.Rational(7294566461180559224916,10**22)
dc=-sp.Rational(14160257025121226420360,10**22)
r=sp.Rational(1,10**11)
elo,ehi=ec-r,ec+r;dlo,dhi=dc-r,dc+r
z0={e:ec,d:dc}
J=sp.Matrix([[sp.diff(P[j],var).subs(z0) for var in (e,d)] for j in (2,3)])
assert J.det()!=0
G=list(J.inv()*sp.Matrix([P[2],P[3]]))

# Exact Bernstein tests on unit interval/square (nonnegative basis).
checks=[]
def pos(poly, name, fixed=None):
    expr=sp.expand(poly.subs({e:elo+2*r*u,d:dlo+2*r*v}))
    if fixed is not None:
        expr=sp.expand(expr.subs({u:sp.Integer(fixed[0]) if fixed[0] is not None else u,
                                   v:sp.Integer(fixed[1]) if fixed[1] is not None else v}))
    po=sp.Poly(expr,u,v)
    du,dv=po.degree_list()
    mon=dict(po.terms())
    bs=[]
    for i in range(du+1):
        for j in range(dv+1):
            beta=sum(mon.get((aa,bb),0)*sp.binomial(i,aa)*sp.binomial(j,bb)/
                     sp.binomial(du,aa)/sp.binomial(dv,bb)
                     for aa in range(i+1) for bb in range(j+1))
            assert beta.is_Rational and beta>0, (name,'Bernstein failure',i,j,beta)
            bs.append(beta)
    checks.append({'name':name, 'bidegree':[du,dv], 'coefficients':len(bs),
                  'minimum_coefficient':str(min(bs))})

# Poincare-Miranda: G1 left negative/right positive; G2 bottom negative/top positive
pos(-G[0],'G1 left negative',(0,None))
pos(G[0],'G1 right positive',(1,None))
pos(-G[1],'G2 bottom negative',(None,0))
pos(G[1],'G2 top positive',(None,1))

# Denominators positive, unique E,D from first two and all errors admissible.
pos(t[0],'t0 positive')
pos(B,'B=x1_minus_x0*denominator positive')
pos(2*B-A,'D below +2')
pos(2*B+A,'D above -2')
pos(2*Ed-En,'E below +2')
pos(2*Ed+En,'E above -2')

# Fifth residual: Y_{q+24}-Y_{p+24}= (p+24)^3 P[4]/(t[4]*(C[p+24]*B+A))
P4at=P[4].subs(z0)
assert P4at!=0
sg=1 if P4at>0 else -1
pos(sg*P[4],'fifth read residual numerator nonzero')
assert sg==1
pos(C[p+24]*B+A,'fifth alternative denominator positive')
pos(10**15*(p+24)**3*P[4]-t[4]*(C[p+24]*B+A),
    'fifth read source minus alternative gap exceeds 1e-15')

Ec=En.subs(z0)/Ed.subs(z0); Dc=A.subs(z0)/B.subs(z0)
assert all(-2<z<2 for z in (ec,dc,Ec,Dc))

out={
 'unit':'R749STD', 'evidence':'AUTHOR_EXACT_NOT_REVIEWED', 'status':'PASS',
 'frozen_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'q':q,'p':p,'source_weights':list(wts),
 'C_T_602': [C[602],T[602]], 'C_T_604':[C[604],T[604]],
 'C_T_626':[C[626],T[626]], 'C_T_628':[C[628],T[628]],
 'exact_center': {'e':str(ec),'d':str(dc),'radius':str(r)},
 'box': {'e':[str(elo),str(ehi)],'d':[str(dlo),str(dhi)]},
 'polynomial_degrees':{str(j):str(sp.Poly(P[j],e,d).total_degree()) for j in (2,3,4)},
 'poincare_miranda_orientation':'G1(left)<0<G1(right), G2(bottom)<0<G2(top), G=J(center)^(-1)*(P2,P3)',
 'jacobian_determinant_nonzero':True,
 'first_four_read_collision_exists':True,
 'all_errors_strictly_inside_minus_2_plus_2':True,
 'fifth_read_difference_nonzero_on_full_box':True,
 'strict_fifth_gap_lower_bound':'Y_626(e,d)-Y_628(E,D)>1/1000000000000000',
 'fifth_polynomial_sign':sg,
 'sign_certificates':checks,'total_positive_bernstein_coefficients':sum(ch['coefficients'] for ch in checks),
 'proof_semantics':'Exact rational bivariate Bernstein positivity over closed rectangle, Poincare-Miranda existence for continuous polynomial map. No floating point dependence.',
 'global_exact_identification_lower_bound':5,
 'global_exact_identification_previous_upper_bound':11,
 'scope_note':'Auxiliary 5-labeled-source scalar model only; not a native X6 or BRC result.',
 'next':'Seek 5-read collisions or a lower global upper bound; optimize finite-cutoff noise margin; retain provenance in a typed BRC observer.'
}
Path(__file__).with_name('R749STD_FOUR_READ_COLLISION_RESULTS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('PASS',out['total_positive_bernstein_coefficients'],'strict Bernstein coefficients;',len(checks),'polynomial certificates; four reads collide for (602,604); fifth differs')
print('center e,d,E,D',*[str(sp.N(z,24)) for z in (ec,dc,Ec,Dc)])
print('P4 sign:',sg,'P degrees:',out['polynomial_degrees'])
