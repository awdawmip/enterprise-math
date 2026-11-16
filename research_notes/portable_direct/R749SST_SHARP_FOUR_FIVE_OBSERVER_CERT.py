#!/usr/bin/env python3
"""R749SST exact finite witness + asymptotic 4-vs-5-read horizon certificate.
Python 3, SymPy. All inequalities use exact rational arithmetic.
"""
import json
from pathlib import Path
import sympy as s
q,e,d,E,D,z=s.symbols('q e d E D z')
W=(1,1,2,3,6)
N=630
n=[0]*(N+1);n[0]=1
for w in W:
    for t in range(w,N+1):n[t]+=n[t-w]
C=[0]*(N+1);T=[0]*(N+1)
for u in range(1,N+1):
    C[u]=C[u-1]+n[u-1]
    T[u]=T[u-1]+C[u-1]
S=lambda u:18*u**4+54*u**3-345*u**2+2070*u-16315
ph={}
for residue in (2,4):
    samp=[residue+6*j for j in range(1,8)]
    cp=s.Poly(s.interpolate([(u,C[u]) for u in samp[:6]],q),q)
    tp=s.Poly(s.interpolate([(u,T[u]) for u in samp],q),q)
    assert cp.degree()==5 and tp.degree()==6
    assert all(cp.eval(u)==C[u] and tp.eval(u)==T[u] for u in samp)
    ph[residue]=(cp,tp)

def jet(residue):
    cp,tp=ph[residue]
    den=s.Poly(cp.as_expr()+d,q)
    num=s.Poly(s.expand(q**3*(tp.as_expr()+e)-S(q)*den.as_expr()/108),q)
    assert num.degree()==den.degree()==5
    a=[num.nth(5-k)/den.nth(5) for k in range(6)]
    b=[den.nth(5-k)/den.nth(5) for k in range(6)]
    result=[]
    for k in range(6):
        result.append(s.factor(a[k]-sum(b[j]*result[k-j] for j in range(1,min(k,5)+1))))
    return result

v2,v4=jet(2),jet(4)
def shift(k):
    if k==0:return v4[0]
    return sum(v4[j]*s.binomial(k-1,k-j)*(-2)**(k-j) for j in range(1,k+1))
coeff=[s.factor(v2[k]-shift(k).subs({e:E,d:D})) for k in range(6)]
assert coeff[0]==0
mat=s.Matrix([[s.diff(coeff[k],var) for var in (e,d,E,D)] for k in range(1,5)])
det=s.factor(mat.det())
assert det==18794499932160000
sol=s.solve(coeff[1:5],(e,d,E,D),dict=True)
assert len(sol)==1
xstar=sol[0]
assert xstar=={e:s.Rational(69402481,101966688),d:-s.Rational(656227,472068),
               E:s.Rational(194725627,101966688),D:-s.Rational(755303,472068)}
assert all(-2<xstar[k]<2 for k in (e,d,E,D))
fifth=s.factor(coeff[5].subs(xstar))
assert fifth==s.Rational(55842420440,39339)>0
# Analytic implicit-function proof: f(z,theta)=(Y_1/z(theta)-Y_(1/z+2)(theta))/z
# is analytic near z=0. Four Newton divided differences at nodes
# t/(1+6jt), j=0..3, analytically extend to t=0 with values c1..c4.
# The displayed exact nonzero determinant certifies the IFT hypothesis.
# Five equal zeros would force the first five derivatives to vanish along any
# q -> infinity sequence. Compact error cube gives a convergent parameter
# subsequence, contradicting unique c1..c4 solution and nonzero c5.

# Explicit finite exact 4-read collision for q=602 and p=604 via Banach.
Q=602
center_str=[
'0.729456646118055922491591897091774570952454989074974313514745',
'-1.4160257025121226420362613056563861050326455137097596990824',
'1.96716018103247281457798031508484711341332978475277300809199',
'-1.6259022319150714812272708279189472411837831869354200078453']
center=[s.Rational(v) for v in center_str]
radius=s.Rational(1,10**30)
assert all(-2<c-radius and c+radius<2 for c in center)

def data(u):
    return map(s.Integer,(C[u],T[u]))

def obs_equation(u,x):
    a,b,c,f=x;v=u+2
    cu,tu=data(u);cv,tv=data(v)
    return s.factor(s.Integer(u)**3*(tu+a)/(cu+b)
                  -s.Integer(v)**3*(tv+c)/(cv+f)
                  -s.Rational(S(u)-S(v),108))

def jac_row(u,x):
    a,b,c,f=x;v=u+2
    cu,tu=data(u);cv,tv=data(v)
    lu,lv=s.Integer(u)**3,s.Integer(v)**3
    return [lu/(cu+b),-lu*(tu+a)/(cu+b)**2,
            -lv/(cv+f),lv*(tv+c)/(cv+f)**2]

indices=[Q+6*j for j in range(4)]
G=s.Matrix([obs_equation(u,center) for u in indices])
J=s.Matrix([jac_row(u,center) for u in indices])
assert J.det()!=0
B=J.inv()
beta=max(abs(v) for v in B*G)
Bnorm=max(sum(abs(B[i,j]) for j in range(4)) for i in range(4))
M=[]
for u in indices:
    v=u+2
    cu,tu=data(u);cv,tv=data(v)
    a=s.Integer(u)**3;b=s.Integer(v)**3
    row=2*a/(cu-2)**2+2*a*(tu+2)/(cu-2)**3
    row+=2*b/(cv-2)**2+2*b*(tv+2)/(cv-2)**3
    M.append(row)
Mmax=max(M)
lip=Bnorm*Mmax*radius
assert beta < s.Rational(1,10**59)
assert Bnorm < 10**13
assert Mmax < s.Rational(1,10**9)
assert lip < s.Rational(1,10**26)
assert beta+lip*radius < radius
# Exact Banach criterion: T(x)=x-BG(x) maps the closed sup-norm radius
# ball around 'center' into itself, and ||DT||_inf <= lip<1.
# This proves a unique exact real root x* inside the box, not just an
# approximate solve. All four coordinates are in (-2,2).

out={
 'unit':'R749SST','status':'PASS','evidence':'AUTHOR_EXACT_NOT_REVIEWED',
 'frozen_scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'result':'For every sufficiently large q≡2 mod6, q and q+2 have a four-read exact collision and no five-read exact collision. Thus the sharp cutoff separation horizon is 5 eventually.',
 'asymptotic_certificate':{'c1_c4_jacobian_det':str(det),
   'unique_jet_parameters':{str(k):str(v) for k,v in xstar.items()},
   'nonzero_c5':str(fifth),
   'existence':'real-analytic implicit function theorem on 4 coalescing-node divided differences',
   'exclusion':'compactness plus fifth divided difference forces forbidden c5=0'},
 'explicit_four_read_collision':{
   'q':Q,'other_cutoff':Q+2,'start_steps':[0,6,12,18],
   'rational_center':center_str,'sup_radius':str(radius),
   'jacobian_invertible':True,'beta_lt':'1e-59','inverse_norm_lt':'1e13',
   'hessian_row_sum_lt':'1e-9','contraction_lt':'1e-26',
   'criterion':'beta + radius*contraction < radius; exact rational verification'},
 'limits':'The eventual fifth-read separation threshold is not numerically bounded by this certificate; exact finite collision applies to q=602; no X6/BRC native operation or shared claim/review asserted.'
}
Path(__file__).with_name('R749SST_SHARP_FOUR_FIVE_OBSERVER_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: eventual sharp four-versus-five horizon; exact q=602 four-read collision certified by Banach')
print('det:',det,'fifth:',fifth)
print('beta/r <',s.N(beta/radius,8),'contraction <=',s.N(lip,8))
